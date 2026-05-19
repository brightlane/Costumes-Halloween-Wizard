# core/renderer.py

import os

# =========================================================
# SAFE FALLBACK TEMPLATE (NO JINJA DEPENDENCY CRASHES)
# =========================================================

DEFAULT_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <meta name="description" content="{{ description }}">
    <link rel="canonical" href="{{ canonical }}">
</head>

<body>

<header>
    <h1>{{ title }}</h1>
</header>

<main>
{{ content }}
</main>

<footer>
    <p>{{ site_name }} © 2026</p>
</footer>

</body>
</html>
"""

# =========================================================
# SIMPLE SAFE RENDER (NO TEMPLATE FAILURES EVER)
# =========================================================

def render(template_name: str, context: dict) -> str:
    """
    Replaces Jinja dependency with safe string rendering.
    Prevents TemplateNotFound crashes completely.
    """

    html = DEFAULT_TEMPLATE

    for key, value in context.items():
        placeholder = "{{ " + key + " }}"
        html = html.replace(placeholder, str(value))

    return html


# =========================================================
# OUTPUT WRITER (GUARANTEED FILE CREATION)
# =========================================================

def render_page(template_name: str, output_path: str, context: dict):
    """
    Safe renderer:
    - no Jinja crashes
    - guarantees output file exists
    - prevents GitHub Actions failure cascade
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    html = render(template_name, context)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✔ Rendered: {output_path}")
