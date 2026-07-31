#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BOOK_FILE="$PROJECT_DIR/tools/product-reference/book.yml"
REFERENCE_DOC="$PROJECT_DIR/tools/product-reference/reference-a4.docx"
HTML_TEMPLATE="$PROJECT_DIR/tools/product-reference/templates/product-reference.html"
HTML_STYLESHEET="$PROJECT_DIR/tools/product-reference/styles/product-reference.css"
OUTPUT_DIR="${1:-$PROJECT_DIR/build/product-reference}"
OUTPUT_BASENAME="unit_product_reference_v_0_1_2_ue0072_touch_dot_s3"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: required command not found: pandoc" >&2
  exit 1
fi

if command -v weasyprint >/dev/null 2>&1; then
  WEASYPRINT=(weasyprint)
else
  BUNDLED_SITE_PACKAGES="$PROJECT_DIR/tools/product-reference/venv/lib/python3.12/site-packages"
  if [[ -d "$BUNDLED_SITE_PACKAGES" ]] && \
    PYTHONPATH="$BUNDLED_SITE_PACKAGES" python3 -c 'import weasyprint' 2>/dev/null; then
    WEASYPRINT=(env "PYTHONPATH=$BUNDLED_SITE_PACKAGES" python3 -m weasyprint)
  else
    echo "Error: required command not found: weasyprint" >&2
    exit 1
  fi
fi

for required_file in \
  "$BOOK_FILE" \
  "$REFERENCE_DOC" \
  "$HTML_TEMPLATE" \
  "$HTML_STYLESHEET"; do
  if [[ ! -f "$required_file" ]]; then
    echo "Error: required file not found: $required_file" >&2
    exit 1
  fi
done

mapfile -t CHAPTERS < <(
  awk '
    /^chapters:/ { in_chapters=1; next }
    in_chapters && /^  - / { sub(/^  - /, ""); print; next }
    in_chapters && !/^  - / { exit }
  ' "$BOOK_FILE"
)

if [[ "${#CHAPTERS[@]}" -eq 0 ]]; then
  echo "Error: book.yml does not contain any chapters." >&2
  exit 1
fi

CHAPTER_PATHS=()
for chapter in "${CHAPTERS[@]}"; do
  if [[ ! -f "$PROJECT_DIR/$chapter" ]]; then
    echo "Error: chapter not found: $chapter" >&2
    exit 1
  fi
  CHAPTER_PATHS+=("$PROJECT_DIR/$chapter")
done

while IFS= read -r asset; do
  if [[ ! -f "$PROJECT_DIR/$asset" ]]; then
    echo "Error: a chapter references a missing asset: $asset" >&2
    exit 1
  fi
done < <(
  grep -hEo '!\[[^]]*\]\([^)]*\)' "${CHAPTER_PATHS[@]}" |
    sed 's/^.*](//;s/)$//' |
    sort -u
)

mkdir -p "$OUTPUT_DIR"

TEMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TEMP_DIR"' EXIT

CONTENTS_FILE="$TEMP_DIR/contents.md"
{
  printf '%s\n' \
    '```{=openxml}' \
    '<w:p><w:r><w:br w:type="page"/></w:r></w:p>' \
    '```' \
    '' \
    '## Contents' \
    ''

  awk '
    /^## / {
      text=$0
      sub(/^## /, "", text)
      gsub(/\*\*/, "", text)
      sub(/[[:space:]]+$/, "", text)
      print "- [" text "]{.toc-entry}"
    }
    /^### / {
      text=$0
      sub(/^### /, "", text)
      gsub(/\*\*/, "", text)
      sub(/[[:space:]]+$/, "", text)
      print "  - [" text "]{.toc-entry}"
    }
  ' "${CHAPTER_PATHS[@]}"

  printf '%s\n' \
    '' \
    '```{=openxml}' \
    '<w:p><w:r><w:br w:type="page"/></w:r></w:p>' \
    '```'
} >"$CONTENTS_FILE"

DOCUMENT_INPUTS=("$CONTENTS_FILE" "${CHAPTER_PATHS[@]}")

MARKDOWN_FILE="$OUTPUT_DIR/$OUTPUT_BASENAME.md"
DOCX_FILE="$OUTPUT_DIR/$OUTPUT_BASENAME.docx"
HTML_FILE="$OUTPUT_DIR/$OUTPUT_BASENAME.html"
PDF_FILE="$OUTPUT_DIR/$OUTPUT_BASENAME.pdf"

pandoc \
  --from=markdown \
  --to=gfm \
  --metadata-file="$BOOK_FILE" \
  "${DOCUMENT_INPUTS[@]}" \
  --output="$MARKDOWN_FILE"

pandoc \
  --from=markdown \
  --to=docx \
  --standalone \
  --metadata-file="$BOOK_FILE" \
  --reference-doc="$REFERENCE_DOC" \
  --resource-path="$PROJECT_DIR" \
  "${DOCUMENT_INPUTS[@]}" \
  --output="$DOCX_FILE"

pandoc \
  --from=markdown \
  --to=html5 \
  --standalone \
  --toc \
  --toc-depth=3 \
  --embed-resources \
  --metadata-file="$BOOK_FILE" \
  --template="$HTML_TEMPLATE" \
  --css="$HTML_STYLESHEET" \
  --resource-path="$PROJECT_DIR" \
  "${CHAPTER_PATHS[@]}" \
  --output="$HTML_FILE"

"${WEASYPRINT[@]}" "$HTML_FILE" "$PDF_FILE"

if [[ ! -s "$PDF_FILE" ]]; then
  echo "Error: WeasyPrint did not generate the PDF." >&2
  exit 1
fi

echo "Product reference built successfully:"
echo "  Markdown: $MARKDOWN_FILE"
echo "  DOCX:     $DOCX_FILE"
echo "  HTML:     $HTML_FILE"
echo "  PDF:      $PDF_FILE"
