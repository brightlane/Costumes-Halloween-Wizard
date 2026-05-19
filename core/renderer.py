import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

# =========================================================
# TEMPLATE CONFIG (ROBUST PATH HANDLING)
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

if not os.path.exists(TEMPLATE_DIR):
    raise FileNotFoundError(
        f"[Renderer] Missing template directory: {TEMPLATE_DIR}\n"
        "Expected structure:\n"
        "core/templates/page.html"
    )

# =========================================================
# JINJA ENV SETUP
# =========================================================

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape(["html", "xml"])
)

# =========================================================
# CORE RENDER FUNCTION
# =========================================================

def render(template_name: str, context: dict) -> str:
    """
    Render a Jinja template safely with debugging support.
    """

    try:
        template = env.get_template(template_name)
    except Exception as e:
        available = os.listdir(TEMPLATE_DIR)

        raise FileNotFoundError(
            f"[Renderer] Template not found: {template_name}\n"
            f"Available templates: {available}\n"
            f"Expected path: {TEMPLATE_DIR}/{template_name}"
        ) from e

    return template.render(**context)

# =========================================================
# PAGE WRAPPER (USED BY build.py)
# =========================================================

def render_page(template_name: str, output_path: str, context: dict):
    """
    Renders template and writes HTML output.
    """

    html = render(template_name, context)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✔ Rendered: {output_path}")
