import os
from datetime import date

from core.renderer import render_page
from core.schema import (
    website_schema,
    organization_schema,
    collection_schema
)
from core.seo import (
    canonical_url,
    hreflang_tags,
    build_title,
    build_description
)
from core.blog_engine import (
    generate_all_articles,
    build_blog_index
)

# =========================================================
# CONFIG (HARDENED)
# =========================================================

SITE_URL = "https://brightlane.github.io/Costumes-Halloween-Wizard"
OUTPUT_DIR = "dist"
SITE_NAME = "Halloween Costumes 2026"
TODAY = str(date.today())

# =========================================================
# CORE PAGES
# =========================================================

PAGES = [
    {
        "slug": "index",
        "title": "Halloween Costumes",
        "description": "Best Halloween costumes for 2026",
        "template": "page.html"
    },
    {
        "slug": "womens-costumes",
        "title": "Women's Costumes",
        "description": "Top women's Halloween costumes",
        "template": "page.html"
    },
    {
        "slug": "mens-costumes",
        "title": "Men's Costumes",
        "description": "Top men's Halloween costumes",
        "template": "page.html"
    },
    {
        "slug": "kids-costumes",
        "title": "Kids Costumes",
        "description": "Best costumes for kids",
        "template": "page.html"
    }
]

# =========================================================
# SAFETY INIT (NO-BREAK LAYER)
# =========================================================

def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(f"{OUTPUT_DIR}/blog", exist_ok=True)

# =========================================================
# OUTPUT PATH
# =========================================================

def output_path(slug):
    return f"{OUTPUT_DIR}/{slug}.html"

# =========================================================
# PAGE BUILDER (SAFE MODE)
# =========================================================

def build_pages():
    print("🚀 Building pages...")

    for page in PAGES:

        slug = page["slug"]

        url = canonical_url(SITE_URL, "en", slug)

        context = {
            "site_name": SITE_NAME,
            "title": build_title(page["title"]),
            "description": build_description(page["description"]),
            "canonical": url,

            "schema_website": website_schema(SITE_NAME, SITE_URL),
            "schema_org": organization_schema(SITE_NAME, SITE_URL),
            "schema_collection": collection_schema(
                page["title"],
                page["description"],
                url
            ),

            "hreflang": hreflang_tags(SITE_URL, slug),

            "content": f"<h1>{page['title']}</h1><p>{page['description']}</p>"
        }

        render_page(
            page["template"],
            output_path(slug),
            context
        )

        print(f"✔ Page built: {slug}")

# =========================================================
# BLOG BUILDER (ISOLATED)
# =========================================================

def build_blog():
    print("🚀 Building blog...")

    articles = generate_all_articles()

    blog_dir = f"{OUTPUT_DIR}/blog"

    # INDEX
    index_html = build_blog_index(articles)

    with open(f"{blog_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    # POSTS
    for article in articles:

        path = f"{blog_dir}/{article['slug']}.html"

        html = f"""
        <html>
        <head>
            <title>{article['title']}</title>
            <meta name="description" content="{article['description']}">
        </head>
        <body>
            <h1>{article['title']}</h1>
            {article['body']}
        </body>
        </html>
        """

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"✔ Blog: {article['slug']}")

# =========================================================
# SEO FILES
# =========================================================

def build_global_files():

    print("🚀 Building SEO files...")

    # sitemap
    sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

    for page in PAGES:
        url = canonical_url(SITE_URL, "en", page["slug"])

        sitemap += f"""
<url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
</url>
"""

    sitemap += "\n</urlset>"

    with open(f"{OUTPUT_DIR}/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

    # robots
    robots = f"""
User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

    with open(f"{OUTPUT_DIR}/robots.txt", "w", encoding="utf-8") as f:
        f.write(robots)

    print("✔ SEO files built")

# =========================================================
# VALIDATION LAYER (NEW NO-BREAK ENGINE)
# =========================================================

def validate_output():

    print("🔍 Validating build output...")

    required = [
        f"{OUTPUT_DIR}/index.html",
        f"{OUTPUT_DIR}/sitemap.xml",
        f"{OUTPUT_DIR}/robots.txt"
    ]

    missing = [f for f in required if not os.path.exists(f)]

    if missing:
        raise RuntimeError(f"Missing required outputs: {missing}")

    print("✔ Output validation passed")

# =========================================================
# MAIN PIPELINE
# =========================================================

def build_all():

    print("🚀 Starting NO-BREAK SEO build system...")

    ensure_dirs()

    build_pages()
    build_blog()
    build_global_files()
    validate_output()

    print("🏁 Build complete - stable output generated")

# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    build_all()
