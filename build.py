import os
from datetime import date

from core.renderer import render_page
from core.schema import website_schema, organization_schema, collection_schema
from core.seo import canonical_url, hreflang_tags, build_title, build_description
from core.build_content import build_content

# =========================================================
# CONFIG
# =========================================================

SITE_URL = "https://brightlane.github.io/Costumes-Halloween-Wizard"
OUTPUT_DIR = "dist"
TODAY = str(date.today())
SITE_NAME = "Halloween Costumes 2026"

# =========================================================
# ROUTES (SINGLE SOURCE OF TRUTH)
# =========================================================

ROUTES = [
    {
        "slug": "index",
        "title": "Halloween Costumes 2026",
        "description": "The best Halloween costumes for 2026",
    },
    {
        "slug": "womens-costumes-2026",
        "title": "Women's Halloween Costumes",
        "description": "Top trending women's costumes for Halloween 2026",
    },
    {
        "slug": "mens-costumes-online",
        "title": "Men's Halloween Costumes",
        "description": "Best men's Halloween costumes and ideas",
    },
    {
        "slug": "kids-halloween-outfits",
        "title": "Kids Halloween Costumes",
        "description": "Best kids Halloween costumes for all ages",
    },
    {
        "slug": "infant-baby-costumes",
        "title": "Baby Halloween Costumes",
        "description": "Cute and safe baby Halloween costumes",
    }
]

# =========================================================
# OUTPUT HELPERS
# =========================================================

def output_path(slug):
    if slug == "index":
        return f"{OUTPUT_DIR}/index.html"
    return f"{OUTPUT_DIR}/{slug}.html"


def ensure_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================================================
# SEO MESH (SAFE INTERNAL LINK SYSTEM)
# =========================================================

def build_internal_links(current_slug):
    return [
        {
            "label": r["title"],
            "url": f"{r['slug']}.html"
        }
        for r in ROUTES if r["slug"] != current_slug
    ]

# =========================================================
# PAGE BUILD
# =========================================================

def build_pages():
    ensure_dir()

    for page in ROUTES:
        slug = page["slug"]

        canonical = canonical_url(SITE_URL, "en", slug)

        internal_links = build_internal_links(slug)

        affiliate_url = f"{SITE_URL}/{slug}.html?aff=1"

        content_html = build_content(page, internal_links, affiliate_url)

        context = {
            "site_name": SITE_NAME,
            "title": build_title(page["title"]),
            "description": build_description(page["description"]),
            "canonical": canonical,

            "schema_website": website_schema(SITE_NAME, SITE_URL),
            "schema_org": organization_schema(SITE_NAME, SITE_URL),
            "schema_collection": collection_schema(
                page["title"],
                page["description"],
                canonical
            ),

            "hreflang": hreflang_tags(SITE_URL, slug),

            # CORE CONTENT PIPELINE (ONLY SOURCE)
            "content": content_html
        }

        render_page("page.html", output_path(slug), context)

        print(f"✔ Built page: {slug}")

# =========================================================
# BLOG (SAFE STUB)
# =========================================================

def build_blog():
    blog_dir = f"{OUTPUT_DIR}/blog"
    os.makedirs(blog_dir, exist_ok=True)

    with open(f"{blog_dir}/index.html", "w", encoding="utf-8") as f:
        f.write("<h1>Blog Index</h1>")

    print("✔ Blog built")

# =========================================================
# GLOBAL FILES
# =========================================================

def build_global_files():
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

    for page in ROUTES:
        url = canonical_url(SITE_URL, "en", page["slug"])

        sitemap += f"""
<url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
</url>
"""

    sitemap += "\n</urlset>"

    with open(f"{OUTPUT_DIR}/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

    robots = f"""
User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

    with open(f"{OUTPUT_DIR}/robots.txt", "w", encoding="utf-8") as f:
        f.write(robots)

    print("✔ SEO files built")

# =========================================================
# MAIN PIPELINE
# =========================================================

def build_all():
    print("🚀 Starting LOCKED SEO build system...")
    build_pages()
    build_blog()
    build_global_files()
    print("🏁 Build complete")

if __name__ == "__main__":
    build_all()
