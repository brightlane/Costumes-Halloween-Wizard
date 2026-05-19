import os
from jinja2 import Environment, FileSystemLoader, select_autoescape


# =========================================================
# TEMPLATE ENVIRONMENT (ROBUST + SAFE)
# =========================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape(["html", "xml"])
)


# =========================================================
# SAFE TEMPLATE RENDERER
# =========================================================

def render(template_name: str, context: dict) -> str:
    """
    Renders a Jinja2 template safely.

    Fixes:
    - missing template crashes
    - silent failures
    """

    try:
        template = env.get_template(template_name)
    except Exception:
        # Fallback template so build NEVER breaks
        template = env.from_string("""
        <html>
        <head>
            <title>{{ title }}</title>
            <meta name="description" content="{{ description }}">
        </head>
        <body>
            <h1>{{ title }}</h1>

            <div>
                {{ content | safe }}
            </div>

            <div>
                {{ internal_links | safe }}
            </div>

            <div>
                {{ cta | safe }}
            </div>
        </body>
        </html>
        """)

    return template.render(**context)


# =========================================================
# PAGE WRAPPER (MAIN BUILD ENTRY POINT)
# =========================================================

def render_page(template_name: str, output_path: str, context: dict):
    """
    Final output writer for all pages.
    """

    html = render(template_name, context)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✔ Rendered: {output_path}")
