#!/bin/bash

# Build the static hardware documentation site.

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: Python 3 is required." >&2
    exit 1
fi

python3 .github/scripts/copy_hardware_docs.py

if [[ ! -s docs/hardware/index.html || \
      ! -s docs/hardware/unit_product_reference_v_0_1_2_ue0072_touch_dot_s3.pdf ]]; then
    echo "Error: documentation output was not generated." >&2
    exit 1
fi

echo "Hardware documentation built successfully."
echo "Open docs/hardware/index.html in a browser to review it."
