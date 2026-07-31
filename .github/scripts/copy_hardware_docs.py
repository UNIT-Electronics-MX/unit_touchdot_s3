#!/usr/bin/env python3
"""Publish hardware resources and generate a static download page."""

import html
import os
import shutil
from pathlib import Path
from urllib.parse import quote

BASE_DIR = Path(__file__).resolve().parent.parent.parent
HARDWARE_DIR = BASE_DIR / "hardware"
DOCS_DIR = BASE_DIR / "docs"
DOCS_HARDWARE_DIR = DOCS_DIR / "hardware"
PRODUCT_REFERENCE_BUILD_DIR = BASE_DIR / "build" / "product-reference"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"}
DOCUMENT_EXTENSIONS = {".pdf", ".docx", ".doc", ".txt", ".md"}
CAD_EXTENSIONS = {
    ".step",
    ".stp",
    ".iges",
    ".igs",
    ".stl",
    ".obj",
    ".3mf",
    ".dxf",
    ".dwg",
}
DESIGN_EXTENSIONS = {
    ".kicad_pcb",
    ".kicad_sch",
    ".kicad_pro",
    ".brd",
    ".sch",
}
MANUFACTURING_EXTENSIONS = {
    ".gbr",
    ".gtl",
    ".gbl",
    ".gts",
    ".gbs",
    ".gto",
    ".gbo",
    ".drl",
    ".xln",
    ".pos",
    ".bom",
    ".ipc",
}
ARCHIVE_EXTENSIONS = {".zip", ".7z", ".tar", ".gz", ".tgz"}

CATEGORY_ORDER = {
    "Product documents": 0,
    "Pinouts": 1,
    "Board views": 2,
    "CAD and design files": 3,
    "Manufacturing files": 4,
    "Other resources": 5,
}


def format_size(size_bytes):
    """Return a compact, human-readable file size."""
    size = float(size_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024


def classify_resource(name, extension):
    """Classify known hardware formats without requiring a file manifest."""
    lower_name = name.lower()
    category = "Other resources"
    title = Path(name).stem.replace("_", " ").replace("-", " ").title()
    description = "Hardware resource"

    if "product_reference" in lower_name or "product-reference" in lower_name:
        category = "Product documents"
        title = "Product Reference"
        description = (
            "Publication-ready product reference"
            if extension == ".pdf"
            else "Editable product reference"
        )
    elif "_sch_" in lower_name or "schematic" in lower_name:
        category = "Product documents"
        title = "Schematic"
        description = "Electrical schematic"
    elif "pinout" in lower_name:
        category = "Pinouts"
        language = "Spanish" if "_es." in lower_name else "English"
        title = f"Pinout — {language}"
        description = f"Connector and signal reference in {language}"
    elif "dimension" in lower_name:
        category = "Board views"
        title = "Mechanical Dimensions"
        description = "Board outline and dimensions"
    elif "topology" in lower_name:
        category = "Board views"
        title = "Board Topology"
        description = "Functional board layout"
    elif "_top_" in lower_name:
        category = "Board views"
        title = "Top View"
        description = "Top-side board view"
    elif "_btm_" in lower_name or "_bottom_" in lower_name:
        category = "Board views"
        title = "Bottom View"
        description = "Bottom-side board view"
    elif extension in CAD_EXTENSIONS:
        category = "CAD and design files"
        cad_labels = {
            ".step": ("3D CAD Model", "STEP mechanical model"),
            ".stp": ("3D CAD Model", "STEP mechanical model"),
            ".iges": ("3D CAD Model", "IGES mechanical model"),
            ".igs": ("3D CAD Model", "IGES mechanical model"),
            ".stl": ("3D Printable Model", "STL mesh model"),
            ".obj": ("3D Model", "OBJ mesh model"),
            ".3mf": ("3D Printable Model", "3MF model"),
            ".dxf": ("Mechanical Drawing", "DXF drawing"),
            ".dwg": ("Mechanical Drawing", "DWG drawing"),
        }
        title, description = cad_labels[extension]
    elif extension in DESIGN_EXTENSIONS:
        category = "CAD and design files"
        design_labels = {
            ".kicad_pcb": ("KiCad PCB Layout", "Editable PCB layout source"),
            ".kicad_sch": ("KiCad Schematic Source", "Editable schematic source"),
            ".kicad_pro": ("KiCad Project", "KiCad project configuration"),
            ".brd": ("PCB Layout Source", "Editable board layout source"),
            ".sch": ("Schematic Source", "Editable schematic source"),
        }
        title, description = design_labels[extension]
    elif extension in MANUFACTURING_EXTENSIONS:
        category = "Manufacturing files"
        if extension == ".bom" or "bom" in lower_name:
            title = "Bill of Materials"
            description = "Manufacturing bill of materials"
        elif extension == ".pos" or "pick" in lower_name or "place" in lower_name:
            title = "Pick-and-Place Data"
            description = "Component placement data"
        elif extension in {".drl", ".xln"}:
            title = "Drill File"
            description = "PCB drilling data"
        else:
            title = "Gerber File"
            description = "PCB fabrication layer"
    elif extension in ARCHIVE_EXTENSIONS:
        if any(word in lower_name for word in ("gerber", "fabrication", "manufacturing")):
            category = "Manufacturing files"
            title = "Manufacturing Package"
            description = "Compressed PCB fabrication files"
        elif any(word in lower_name for word in ("cad", "step", "model", "design")):
            category = "CAD and design files"
            title = "Design Package"
            description = "Compressed design resources"
        else:
            title = "Hardware Resource Package"
            description = "Compressed hardware resources"
    elif lower_name == "readme.md":
        title = "Hardware README"
        description = "Hardware overview and source notes"
    elif "schematics_icon" in lower_name:
        title = "Schematic Icon"
        description = "Artwork used by the hardware README"

    return category, title, description


def describe_file(file_path):
    """Build user-facing metadata from a published hardware filename."""
    name = file_path.name
    extension = file_path.suffix.lower()
    category, title, description = classify_resource(name, extension)
    relative_path = file_path.relative_to(DOCS_HARDWARE_DIR).as_posix()
    return {
        "name": name,
        "title": title,
        "description": description,
        "category": category,
        "extension": extension,
        "type": "image" if extension in IMAGE_EXTENSIONS else "document",
        "size": file_path.stat().st_size,
        "size_human": format_size(file_path.stat().st_size),
        "path": relative_path,
        "display_path": relative_path,
        "url": quote(relative_path, safe="/"),
    }


def copy_hardware_files():
    """Copy released hardware files and generated product reference outputs."""
    if not HARDWARE_DIR.is_dir():
        raise FileNotFoundError(f"Hardware directory not found: {HARDWARE_DIR}")

    if DOCS_HARDWARE_DIR.exists():
        shutil.rmtree(DOCS_HARDWARE_DIR)
    shutil.copytree(HARDWARE_DIR, DOCS_HARDWARE_DIR)

    if PRODUCT_REFERENCE_BUILD_DIR.is_dir():
        for generated_file in sorted(PRODUCT_REFERENCE_BUILD_DIR.iterdir()):
            if generated_file.suffix.lower() in {".pdf", ".docx"}:
                shutil.copy2(generated_file, DOCS_HARDWARE_DIR / generated_file.name)


def scan_published_files():
    """Return deterministic metadata for every published hardware file."""
    files = []
    for root, dirs, names in os.walk(DOCS_HARDWARE_DIR):
        dirs.sort()
        for name in sorted(names):
            if name.lower() == "schematics_icon.jpg":
                continue
            files.append(describe_file(Path(root) / name))
    return sorted(
        files,
        key=lambda item: (
            CATEGORY_ORDER[item["category"]],
            item["title"].lower(),
            item["extension"],
        ),
    )


def render_resource(item):
    """Render one accessible horizontal resource row."""
    title = html.escape(item["title"])
    description = html.escape(item["description"])
    filename = html.escape(item["display_path"])
    extension = html.escape(item["extension"].lstrip(".").upper() or "FILE")
    size = html.escape(item["size_human"])
    url = html.escape(item["url"], quote=True)

    return f"""
        <article class="resource-item" data-search="{html.escape((item['title'] + ' ' + item['path'] + ' ' + item['description']).lower(), quote=True)}">
          <div class="file-meta">
            <strong class="file-type">{extension}</strong>
            <span class="file-size">{size}</span>
          </div>
          <div class="resource-details">
            <h3>{title}</h3>
            <p>{description}</p>
            <code title="{filename}">{filename}</code>
          </div>
          <div class="actions">
            <button class="button primary copy-link" type="button" data-url="{url}">Copy link</button>
            <a class="button" href="{url}" target="_blank" rel="noopener">Open file</a>
          </div>
        </article>"""


def generate_html_page(files):
    """Generate a responsive, dependency-free hardware resource page."""
    grouped = {category: [] for category in CATEGORY_ORDER}
    for item in files:
        grouped[item["category"]].append(item)

    sections = []
    for category in CATEGORY_ORDER:
        items = grouped[category]
        if not items:
            continue
        rows = "\n".join(render_resource(item) for item in items)
        sections.append(
            f"""
      <section class="resource-section">
        <div class="section-heading">
          <h2>{html.escape(category)}</h2>
          <span>{len(items)} {"file" if len(items) == 1 else "files"}</span>
        </div>
        <div class="resource-list">{rows}
        </div>
      </section>"""
        )

    total_size = format_size(sum(item["size"] for item in files))
    images = sum(item["type"] == "image" for item in files)
    formats = len({item["extension"] for item in files})
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="TouchDot S3 hardware documentation and downloads">
  <title>TouchDot S3 | Hardware Resources</title>
  <style>
    :root {{
      --ink: #17202a;
      --muted: #667085;
      --line: #dfe3e8;
      --brand: #e53b2c;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font: 16px/1.5 Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
    }}
    .site-header {{ border-bottom: 1px solid var(--line); }}
    .header-content, main {{
      width: min(1100px, calc(100% - 32px));
      margin: 0 auto;
    }}
    .header-content {{ padding: 28px 0; }}
    .eyebrow {{
      margin: 0 0 4px;
      color: var(--brand);
      font-size: .8rem;
      font-weight: 700;
    }}
    h1 {{ margin: 0; font-size: 1.8rem; }}
    .subtitle {{ margin: 5px 0 0; color: var(--muted); }}
    .summary {{
      display: flex;
      flex-wrap: wrap;
      gap: 18px;
      margin-top: 14px;
      color: var(--muted);
      font-size: .85rem;
    }}
    .summary strong {{ color: var(--ink); }}
    main {{ padding: 24px 0 48px; }}
    .toolbar {{ margin-bottom: 24px; }}
    .search {{
      width: 100%;
      padding: 10px 12px;
      border: 1px solid var(--line);
      border-radius: 4px;
      color: var(--ink);
      font: inherit;
    }}
    .search:focus {{ outline: 2px solid #f6c4bf; border-color: var(--brand); }}
    .resource-section {{ margin-top: 24px; }}
    .section-heading {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      margin-bottom: 8px;
      border-bottom: 1px solid var(--line);
    }}
    .section-heading h2 {{ margin: 0 0 7px; font-size: 1.05rem; }}
    .section-heading span {{ color: var(--muted); font-size: .85rem; }}
    .resource-list {{ border-top: 1px solid var(--line); }}
    .resource-item {{
      display: grid;
      grid-template-columns: 70px minmax(0, 1fr) auto;
      align-items: center;
      gap: 16px;
      padding: 14px 8px;
      border: 1px solid var(--line);
      border-top: 0;
    }}
    .file-meta {{ display: grid; gap: 4px; text-align: center; }}
    .file-type {{
      color: var(--brand);
      font-size: .78rem;
    }}
    .file-size {{ color: var(--muted); font-size: .78rem; }}
    .resource-details {{ min-width: 0; }}
    .resource-item h3 {{ margin: 0; font-size: 1rem; }}
    .resource-item p {{
      display: inline;
      margin: 0 8px 0 0;
      color: var(--muted);
      font-size: .85rem;
    }}
    .resource-item code {{
      display: block;
      overflow: hidden;
      margin-top: 3px;
      color: var(--muted);
      font-size: .7rem;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .actions {{ display: flex; gap: 6px; }}
    .button {{
      display: inline-flex;
      justify-content: center;
      padding: 7px 10px;
      border: 1px solid var(--line);
      border-radius: 4px;
      color: var(--ink);
      background: #fff;
      cursor: pointer;
      text-decoration: none;
      font-size: .8rem;
      font-weight: 600;
      font-family: inherit;
    }}
    .button:hover {{ border-color: #aeb4bd; }}
    .button.primary {{ color: #fff; border-color: var(--brand); background: var(--brand); }}
    .empty-state {{ display: none; padding: 32px 0; color: var(--muted); text-align: center; }}
    footer {{ padding: 24px 16px; border-top: 1px solid var(--line); color: var(--muted); text-align: center; font-size: .82rem; }}
    [hidden] {{ display: none !important; }}
    .visually-hidden {{
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }}
    @media (max-width: 680px) {{
      .resource-item {{ grid-template-columns: 52px minmax(0, 1fr); }}
      .actions {{ grid-column: 1 / -1; padding-left: 68px; }}
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-content">
      <p class="eyebrow">UNIT Electronics · UE0072</p>
      <h1>TouchDot S3</h1>
      <p class="subtitle">Direct links to hardware documentation and product files for use in external platforms.</p>
      <div class="summary" aria-label="Resource summary">
        <span><strong>{len(files)}</strong> files</span>
        <span><strong>{images}</strong> images</span>
        <span><strong>{formats}</strong> formats</span>
        <span><strong>{html.escape(total_size)}</strong> total</span>
      </div>
    </div>
  </header>
  <main>
    <div class="toolbar">
      <label for="resource-search" class="visually-hidden">Search hardware resources</label>
      <input id="resource-search" class="search" type="search" placeholder="Search hardware resources…" autocomplete="off">
    </div>
    {"".join(sections)}
    <p id="empty-state" class="empty-state">No resources match your search.</p>
  </main>
  <footer>UNIT Electronics hardware resources</footer>
  <script>
    const search = document.getElementById('resource-search');
    const sections = [...document.querySelectorAll('.resource-section')];
    const emptyState = document.getElementById('empty-state');
    const copyText = async (text) => {{
      try {{
        await navigator.clipboard.writeText(text);
      }} catch (error) {{
        const input = document.createElement('textarea');
        input.value = text;
        input.style.position = 'fixed';
        input.style.opacity = '0';
        document.body.appendChild(input);
        input.select();
        document.execCommand('copy');
        input.remove();
      }}
    }};
    document.querySelectorAll('.copy-link').forEach((button) => {{
      button.addEventListener('click', async () => {{
        const absoluteUrl = new URL(button.dataset.url, window.location.href).href;
        await copyText(absoluteUrl);
        const originalLabel = button.textContent;
        button.textContent = 'Copied';
        setTimeout(() => {{ button.textContent = originalLabel; }}, 1600);
      }});
    }});
    search.addEventListener('input', () => {{
      const query = search.value.trim().toLowerCase();
      let visibleCards = 0;
      sections.forEach((section) => {{
        let sectionCards = 0;
        section.querySelectorAll('.resource-item').forEach((card) => {{
          const match = card.dataset.search.includes(query);
          card.hidden = !match;
          sectionCards += Number(match);
        }});
        section.hidden = sectionCards === 0;
        visibleCards += sectionCards;
      }});
      emptyState.style.display = visibleCards ? 'none' : 'block';
    }});
  </script>
</body>
</html>
"""

    DOCS_HARDWARE_DIR.mkdir(parents=True, exist_ok=True)
    page = "\n".join(line.rstrip() for line in page.splitlines()).strip() + "\n"
    (DOCS_HARDWARE_DIR / "index.html").write_text(page, encoding="utf-8")


def main():
    """Publish the hardware resources and index page."""
    copy_hardware_files()
    files = scan_published_files()
    generate_html_page(files)
    print(f"Published {len(files)} hardware files to {DOCS_HARDWARE_DIR}")
    print(f"Generated {DOCS_HARDWARE_DIR / 'index.html'}")


if __name__ == "__main__":
    main()
