import os
import re

from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape
)

# =========================================================
# TEMPLATE ENGINE CONFIG
# =========================================================

env = Environment(

    loader=FileSystemLoader("templates"),

    autoescape=select_autoescape([
        "html",
        "xml"
    ]),

    trim_blocks=True,

    lstrip_blocks=True
)

# =========================================================
# GLOBAL TEMPLATE HELPERS
# =========================================================

def money(value):

    return f"${value:,.2f}"

env.filters["money"] = money

# =========================================================
# HTML MINIFIER
# =========================================================

def minify_html(html):

    # remove comments
    html = re.sub(
        r"<!--.*?-->",
        "",
        html,
        flags=re.DOTALL
    )

    # collapse whitespace
    html = re.sub(
        r">\s+<",
        "><",
        html
    )

    # collapse multi spaces
    html = re.sub(
        r"\s{2,}",
        " ",
        html
    )

    return html.strip()

# =========================================================
# TEMPLATE RENDERER
# =========================================================

def render(
    template_name,
    context=None,
    minify=False
):
    """
    Render a template with context.
    """

    if context is None:

        context = {}

    template = env.get_template(
        template_name
    )

    html = template.render(
        **context
    )

    if minify:

        html = minify_html(html)

    return html

# =========================================================
# FILE WRITER
# =========================================================

def ensure_directory(path):

    os.makedirs(
        path,
        exist_ok=True
    )

def write_html(
    output_path,
    html,
    minify=True
):
    """
    Writes HTML safely to disk.
    """

    directory = os.path.dirname(
        output_path
    )

    ensure_directory(directory)

    if minify:

        html = minify_html(html)

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

# =========================================================
# BULK PAGE RENDERER
# =========================================================

def render_page(
    template_name,
    output_path,
    context
):
    """
    Render + write helper.
    """

    html = render(
        template_name,
        context=context,
        minify=True
    )

    write_html(
        output_path,
        html,
        minify=False
    )

# =========================================================
# SEO HELPERS
# =========================================================

def canonical_url(
    site_url,
    lang,
    slug
):

    if slug == "index":

        return f"{site_url}/{lang}/"

    return f"{site_url}/{lang}/{slug}/"

def hreflang_map(
    site_url,
    languages,
    slug
):

    hreflangs = []

    for lang in languages:

        hreflangs.append({

            "lang": lang,

            "url": canonical_url(
                site_url,
                lang,
                slug
            )
        })

    return hreflangs

# =========================================================
# RELATED CONTENT ENGINE
# =========================================================

def related_pages(
    pages,
    current_slug,
    limit=8
):
    """
    Returns related pages excluding current page.
    """

    related = []

    for page in pages:

        if page["slug"] == current_slug:

            continue

        related.append({

            "title": page["title"],

            "slug": page["slug"]
        })

    return related[:limit]

# =========================================================
# SEARCH INDEX HELPER
# =========================================================

def build_search_record(
    title,
    url,
    description=""
):

    return {

        "title": title,

        "url": url,

        "description": description
    }

# =========================================================
# RSS ITEM HELPER
# =========================================================

def build_rss_item(
    title,
    url,
    description=""
):

    return {

        "title": title,

        "url": url,

        "description": description
    }

# =========================================================
# SAFE TEXT CLEANER
# =========================================================

def clean_text(text):

    text = text.strip()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text

# =========================================================
# SLUGIFY
# =========================================================

def slugify(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s-]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        "-",
        text
    )

    return text.strip("-")

# =========================================================
# DEBUG TEST
# =========================================================

if __name__ == "__main__":

    sample = render(
        "base.html",
        {
            "title": "Test Page",
            "description": "Testing renderer."
        }
    )

    print(sample[:500])
