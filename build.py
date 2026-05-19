import os
from datetime import date
from urllib.parse import quote

from core.renderer import render_page
from core.schema import website_schema, organization_schema, collection_schema
from core.seo import canonical_url, hreflang_tags, build_title, build_description

# =========================================================
# CONFIG
# =========================================================

SITE_URL = "https://brightlane.github.io/Costumes-Halloween-Wizard"
OUTPUT_DIR = "dist"
TODAY = str(date.today())
SITE_NAME = "Halloween Costumes 2026"

# IMPORTANT: SINGLE SOURCE OF TRUTH ROUTING TABLE
ROUTES = [
    {
        "slug": "index",
        "title": "Halloween Costumes 2026",
        "description": "The best Halloween costumes for 2026",
        "primary_keyword": "halloween costumes"
    },
    {
        "slug": "womens-costumes-2026",
        "title": "Women's Halloween Costumes 2026",
        "description": "Top trending women's costumes for Halloween 2026",
        "primary_keyword": "women halloween costumes"
    },
    {
        "slug": "mens-costumes-online",
        "title": "Men's Halloween Costumes 2026",
        "description": "Best men's Halloween costumes and ideas",
        "primary_keyword": "mens halloween costumes"
    },
    {
        "slug": "kids-halloween-outfits",
        "title": "Kids Halloween Costumes 2026",
        "description": "Best kids Halloween costumes for all ages",
        "primary_keyword": "kids halloween costumes"
    },
    {
        "slug": "infant-baby-costumes",
        "title": "Baby Halloween Costumes 2026",
        "description": "Cute and safe baby Halloween costumes",
        "primary_keyword": "baby halloween costumes"
    }
]

# =========================================================
# AFFILIATE SYSTEM (FORCE CONSISTENCY)
# =========================================================

AFFILIATE_ID = "your-affiliate-id"

def affiliate_link(base_url: str, slug: str) -> str:
    """
    ALWAYS preserves affiliate tracking across all pages
    """
    return f"{base_url}/{slug}.html?aff={AFFILIATE_ID}"

# =========================================================
# SEO MESH SYSTEM (INTERNAL LINK GRAPH)
# =========================================================

def build_internal_links(current_slug: str):
    links = []

    for route in ROUTES:
        if route["slug"] != current_slug:
            links.append({
                "label": route["title"],
                "url": f"{route['slug']}.html?aff={AFFILIATE_ID}"
            })

    return links

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
# PAGE BUILDER
# =========================================================

def build_pages():
    ensure_dir()

    for page in ROUTES:
        slug = page["slug"]

        canonical = canonical_url(SITE_URL, "en", slug)

        internal_links = build_internal_links(slug)

        context = {
            "site_name": SITE_NAME,
            "title": build_title(page["title"]),
            "description": build_description(page["description"]),
            "canonical": canonical,

            # schemas
            "schema_website": website_schema(SITE_NAME, SITE_URL),
            "schema_org": organization_schema(SITE_NAME, SITE_URL),
            "schema_collection": collection_schema(
                page["title"],
                page["description"],
                canonical
            ),

            "hreflang": hreflang_tags(SITE_URL, slug),

            # CORE CONTENT
            "content": f"""
                <h1>{page['title']}</h1>
                <p>{page['description']}</p>

                <h2>Recommended Vault Categories</h2>
                <ul>
                    {''.join([f"<li><a href='{link['url']}'>{link['label']}</a></li>" for link in internal_links])}
                </ul>

                <a href="{affiliate_link(SITE_URL, slug)}">
                    Shop {page['title']} Deals ➜
                </a>
            """
        }

        render_page(page["template"], output_path(slug), context)

        print(f"✔ Built page: {slug}")

# =========================================================
# BLOG SAFE PLACEHOLDER (NO BREAKS)
# =========================================================

def build_blog():
    blog_dir = f"{OUTPUT_DIR}/blog"
    os.makedirs(blog_dir, exist_ok=True)

    with open(f"{blog_dir}/index.html", "w", encoding="utf-8") as f:
        f.write("<h1>Blog Index</h1>")

    print("✔ Blog built (safe stub)")

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

    print("✔ Global SEO files built")

# =========================================================
# MAIN PIPELINE
# =========================================================

def build_all():
    print("🚀 Starting stable SEO build system...")
    build_pages()
    build_blog()
    build_global_files()
    print("🏁 Build complete")

if __name__ == "__main__":
    build_all()
