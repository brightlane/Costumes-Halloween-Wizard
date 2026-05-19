#!/usr/bin/env python3

import os
import json
from datetime import date

from core.renderer import render
from core.affiliate import affiliate_url
from core.schema import faq_schema

TODAY = date.today().isoformat()

SITE_URL = "https://brightlane.github.io/Costumes-Halloween-Wizard"

OUTPUT_DIR = "output"

LANGUAGES = ["en", "es", "fr", "de"]

# =========================================================
# LOAD DATA
# =========================================================

with open("data/pages.json", encoding="utf-8") as f:
    PAGES = json.load(f)

with open("data/blog_topics.json", encoding="utf-8") as f:
    BLOGS = json.load(f)

# =========================================================
# HELPERS
# =========================================================

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_file(path, content):

    ensure_dir(os.path.dirname(path))

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def page_output_path(lang, slug):

    if slug == "index":
        return f"{OUTPUT_DIR}/{lang}/index.html"

    return f"{OUTPUT_DIR}/{lang}/{slug}/index.html"

# =========================================================
# CATEGORY PAGE GENERATION
# =========================================================

search_index = []

sitemap_urls = []

rss_items = []

for lang in LANGUAGES:

    for page in PAGES:

        slug = page["slug"]

        title = page["title"]

        description = page["description"]

        body = page["body"]

        category = page["category"]

        related_pages = []

        for rel in PAGES[:8]:

            if rel["slug"] != slug:

                related_pages.append({
                    "title": rel["title"],
                    "url": f"/{lang}/{rel['slug']}/"
                })

        affiliate_link = affiliate_url(cat_key=category)

        faq = [
            {
                "q": f"What are the best {title}?",
                "a": f"Our {title} collection includes trending and best-selling styles for 2026."
            },
            {
                "q": f"Where can I buy {title}?",
                "a": f"You can browse top-rated selections online with worldwide shipping available."
            }
        ]

        faq_json = faq_schema(faq)

        html = render(
            "category.html",
            {
                "lang": lang,
                "title": title,
                "description": description,
                "canonical": f"{SITE_URL}/{lang}/{slug}/",
                "h1": title,
                "subtitle": "Trending Halloween Styles for 2026",
                "body": body,
                "affiliate_link": affiliate_link,
                "related_pages": related_pages,
                "faq_schema": faq_json,
                "nav_links": [
                    {
                        "name": "Home",
                        "url": f"/{lang}/"
                    },
                    {
                        "name": "Blog",
                        "url": f"/{lang}/blog/"
                    }
                ],
                "hreflangs": [
                    {
                        "lang": l,
                        "url": f"{SITE_URL}/{l}/{slug}/"
                    }
                    for l in LANGUAGES
                ]
            }
        )

        out_path = page_output_path(lang, slug)

        write_file(out_path, html)

        sitemap_urls.append(
            f"{SITE_URL}/{lang}/{slug}/"
        )

        search_index.append({
            "title": title,
            "url": f"/{lang}/{slug}/"
        })

# =========================================================
# BLOG POSTS
# =========================================================

for lang in LANGUAGES:

    for blog in BLOGS:

        slug = blog["slug"]

        title = blog["title"]

        category = blog["category"]

        affiliate_link = affiliate_url(cat_key=category)

        products = [
            "Premium Deluxe Costume",
            "LED Accessory Kit",
            "Movie Replica Edition",
            "Collector Cosplay Version"
        ]

        html = render(
            "blog.html",
            {
                "lang": lang,
                "title": title,
                "description": title,
                "canonical": f"{SITE_URL}/{lang}/blog/{slug}/",
                "h1": title,
                "subtitle": "Complete Buyer Guide",
                "intro": f"Discover the best {title.lower()} available this season.",
                "products": products,
                "affiliate_link": affiliate_link,
                "nav_links": [
                    {
                        "name": "Home",
                        "url": f"/{lang}/"
                    }
                ],
                "hreflangs": [
                    {
                        "lang": l,
                        "url": f"{SITE_URL}/{l}/blog/{slug}/"
                    }
                    for l in LANGUAGES
                ]
            }
        )

        out_path = f"{OUTPUT_DIR}/{lang}/blog/{slug}/index.html"

        write_file(out_path, html)

        sitemap_urls.append(
            f"{SITE_URL}/{lang}/blog/{slug}/"
        )

        rss_items.append({
            "title": title,
            "url": f"{SITE_URL}/{lang}/blog/{slug}/"
        })

# =========================================================
# RSS FEED
# =========================================================

rss_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>

<rss version="2.0">

<channel>

<title>Halloween Costumes 2026</title>

<link>{SITE_URL}</link>

<description>Latest Halloween costume guides and trend reports.</description>

"""

for item in rss_items:

    rss_xml += f"""

<item>
<title>{item["title"]}</title>
<link>{item["url"]}</link>
</item>

"""

rss_xml += """

</channel>

</rss>
"""

write_file(
    f"{OUTPUT_DIR}/rss.xml",
    rss_xml
)

# =========================================================
# SITEMAP
# =========================================================

sitemap = """<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

for url in sitemap_urls:

    sitemap += f"""

<url>
<loc>{url}</loc>
<lastmod>{TODAY}</lastmod>
<changefreq>weekly</changefreq>
<priority>0.8</priority>
</url>

"""

sitemap += "</urlset>"

write_file(
    f"{OUTPUT_DIR}/sitemap.xml",
    sitemap
)

# =========================================================
# SEARCH INDEX
# =========================================================

write_file(
    f"{OUTPUT_DIR}/search.json",
    json.dumps(search_index, indent=2)
)

# =========================================================
# ROBOTS.TXT
# =========================================================

robots = f"""
User-agent: *

Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

write_file(
    f"{OUTPUT_DIR}/robots.txt",
    robots
)

# =========================================================
# LLMS.TXT
# =========================================================

llms = f"""
# Halloween Costumes 2026

Site: {SITE_URL}

Generated: {TODAY}

"""

for page in PAGES:

    llms += f"""

- {page["title"]}

"""

write_file(
    f"{OUTPUT_DIR}/llms.txt",
    llms
)

print("✅ BUILD COMPLETE")
