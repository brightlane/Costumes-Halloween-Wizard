import os
from datetime import date

from core.renderer import render_page
from core.schema import (
    website_schema,
    organization_schema,
    collection_schema
)
from core.seo import canonical_url, hreflang_tags, build_title, build_description

from core.blog_engine import generate_all_articles, build_blog_index

from core.seo_mesh import enrich_page


# =========================================================
# CONFIG
# =========================================================

SITE_URL = "https://brightlane.github.io/Costumes-Halloween-Wizard"
OUTPUT_DIR = "dist"
TODAY = str(date.today())

SITE_NAME = "Halloween Costumes 2026"


# =========================================================
# CORE PAGE DEFINITIONS (SOURCE OF TRUTH)
# =========================================================

PAGES = [
    {
        "slug": "index",
        "title": "Halloween Costumes",
        "description": "Best Halloween costumes for 2026",
        "template": "page.html",
        "category_key": "main"
    },
    {
        "slug": "womens-costumes",
        "title": "Women's Costumes",
        "description": "Top women's Halloween costumes",
        "template": "page.html",
        "category_key": "women"
    },
    {
        "slug": "mens-costumes",
        "title": "Men's Costumes",
        "description": "Top men's Halloween costumes",
        "template": "page.html",
        "category_key": "men"
    },
    {
        "slug": "kids-costumes",
        "title": "Kids Costumes",
        "description": "Best costumes for kids",
        "template": "page.html",
        "category_key": "kids"
    },
    {
        "slug": "baby-costumes",
        "title": "Baby Costumes",
        "description": "Cute baby Halloween costumes",
        "template": "page.html",
        "category_key": "baby"
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
# PAGE BUILDER (NOW FULLY MESH-AWARE)
# =========================================================

def build_pages():
    ensure_dir()

    for page in PAGES:

        slug = page["slug"]
        category_key = page.get("category_key", "main")

        url = canonical_url(SITE_URL, "en", slug)

        base_content = f"""
        <h1>{page['title']}</h1>
        <p>{page['description']}</p>
        """

        # ✅ THIS IS THE KEY FIX
        # Everything becomes structured BEFORE rendering
        enriched = enrich_page(
            SITE_URL,
            category_key,
            base_content
        )

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

            # =================================================
            # STRUCTURED CONTENT (IMPORTANT FIX)
            # =================================================
            "content": enriched["content"],
            "internal_links": enriched["internal_links"],
            "cta": enriched["cta"],
        }

        render_page(
            page["template"],
            output_path(slug),
            context
        )

        print(f"✔ Built page: {slug}")


# =========================================================
# BLOG BUILD (UNCHANGED BUT STABLE)
# =========================================================

def build_blog():
    articles = generate_all_articles()

    blog_dir = f"{OUTPUT_DIR}/blog"
    os.makedirs(blog_dir, exist_ok=True)

    index_html = build_blog_index(articles)

    with open(f"{blog_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

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

        print(f"✔ Blog post: {article['slug']}")


# =========================================================
# GLOBAL FILES (SITEMAP + ROBOTS FIXED)
# =========================================================

def build_global_files():

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
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
    print("🚀 Starting MASS SEO build system...")

    build_pages()
    build_blog()
    build_global_files()

    print("🏁 Build complete")


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    build_all()
