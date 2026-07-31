# Product reference build

The product reference source is maintained in Markdown under `chapters/`. Document
metadata and chapter order are defined in `book.yml`.

## Local build

Requirements:

- Pandoc
- WeasyPrint

Run from the repository root:

```bash
./tools/product-reference/build.sh
```

Generated files are written to `build/product-reference/`:

```text
unit_product_reference_v_0_1_2_ue0072_touch_dot_s3.md
unit_product_reference_v_0_1_2_ue0072_touch_dot_s3.docx
unit_product_reference_v_0_1_2_ue0072_touch_dot_s3.html
unit_product_reference_v_0_1_2_ue0072_touch_dot_s3.pdf
```

The Markdown chapters are the source of truth. Product values and pin mappings
must be taken from the released files in `hardware/` or the maintained TouchDot
documentation; do not infer electrical limits that are not documented.
