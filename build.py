import os
from datetime import date
from itertools import product

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
# CONFIG
# =========================================================

SITE_URL = "https://brightlane.github.io/Costumes-Halloween-Wizard"
OUTPUT_DIR = "dist"
TODAY = str(date.today())
SITE_NAME = "Halloween Costumes 2026"

# =========================================================
# CORE BASE TOPICS
# =========================================================

BASE_CATEGORIES = [
    "womens", "mens", "kids", "baby", "toddler",
    "teen", "adult", "couples", "group"
]

FANDOMS = [
    "anime", "gaming", "horror", "movies", "tvshows",
    "superhero", "fantasy", "wizard"
]

INTENTS = [
    "cheap",
    "last-minute",
    "best",
    "trending",
    "2026",
    "group",
    "funny",
    "scary"
]

LOCATIONS = [
    "near-me",
    "usa",
    "uk",
    "canada",
    "australia"
]

# =========================================================
# OUTPUT
# =========================================================

def output_path(slug):
    return f"{OUTPUT_DIR}/{slug}.html"

def ensure_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================================================
# SLUG BUILDER (ANTI-DUPLICATE SAFE)
# =========================================================

def build_slug(*parts):
    return "-".join([p.lower().replace(" ", "-") for p in parts])

# =========================================================
# PAGE FACTORY
# =========================================================

def generate_pages():

    pages = []

    # -----------------------------
    # 1. BASE CATEGORY PAGES
    # -----------------------------
    for cat in BASE_CATEGORIES:
        pages.append({
            "slug": build_slug(cat, "costumes"),
            "title": f"{cat.title()} Halloween Costumes",
            "description": f"Best {cat} Halloween costumes for 2026",
            "type": "collection"
        })

    # -----------------------------
    # 2. FANDOM PAGES
    # -----------------------------
    for fandom in FANDOMS:
        pages.append({
            "slug": build_slug(fandom, "costumes"),
            "title": f"{fandom.title()} Costumes",
            "description": f"Top {fandom} Halloween costume ideas",
            "type": "fandom"
        })

    # -----------------------------
    # 3. INTENT PAGES (SEO BOOSTERS)
    # -----------------------------
    for cat, intent in product(BASE_CATEGORIES, INTENTS):
        pages.append({
            "slug": build_slug(intent, cat, "costumes"),
            "title": f"{intent.title()} {cat.title()} Costumes",
            "description": f"{intent} {cat} Halloween costumes for 2026",
            "type": "intent"
        })

    # -----------------------------
    # 4. LOCATION PAGES
    # -----------------------------
    for cat, loc in product(BASE_CATEGORIES, LOCATIONS):
        pages.append({
            "slug": build_slug(cat, "costumes", loc),
            "title": f"{cat.title()} Costumes {loc.replace('-', ' ').title()}",
            "description": f"{cat} Halloween costumes available {loc}",
            "type": "geo"
        })

    return pages

# =========================================================
# PAGE BUILDER
# =========================================================

def build_pages():

    ensure_dir()

    pages = generate_pages()

    print(f"🚀 Generating {len(pages)} SEO pages...")

    for page in pages:

        url = canonical_url(SITE_URL, "en", page["slug"])

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

            "hreflang": hreflang_tags(SITE_URL, page["slug"]),

            "content": f"""
                <h1>{page['title']}</h1>
                <p>{page['description']}</p>
                <p>Explore premium 2026 costume collections updated daily.</p>
            """
        }

        render_page(
            "page.html",
            output_path(page["slug"]),
            context
        )

        print(f"✔ {page['slug']}")

# =========================================================
# BLOG SYSTEM (EXPANDABLE TO 200+ POSTS)
# =========================================================

def build_blog():

    articles = generate_all_articles()

    blog_dir = f"{OUTPUT_DIR}/blog"
    os.makedirs(blog_dir, exist_ok=True)

    # Index
    index_html = build_blog_index(articles)

    with open(f"{blog_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    # Posts
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

    pages = generate_pages()

    # sitemap
    sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

    for p in pages:

        url = canonical_url(SITE_URL, "en", p["slug"])

        sitemap += f"""
<url>
  <loc>{url}</loc>
  <lastmod>{TODAY}</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.7</priority>
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
# MASTER RUNNER
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
