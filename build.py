import os
from datetime import date
from urllib.parse import quote

# =========================================================
# CONFIG
# =========================================================

SITE_URL        = "https://brightlane.github.io/Costumes-Halloween-Wizard"
OUTPUT_DIR      = "dist"
TODAY           = str(date.today())
SITE_NAME       = "Halloween Costumes 2026"
OWNER           = "Benny Palmarino"
YEAR            = "2026"

# ── Affiliate (LinkConnector) ──────────────────────────────
AFFILIATE_ID    = "7949"
AFFILIATE_LC    = "007949060109004909"
AFFILIATE_ATID  = "WebCostume"
AFFILIATE_BASE  = "https://www.linkconnector.com/ta.php"

# Base merchant category URLs on halloweencostumes.com
MERCHANT_BASE   = "https://www.halloweencostumes.com"

def aff(dest_path=""):
    """Build a full LinkConnector tracking URL for a given merchant path."""
    dest = f"{MERCHANT_BASE}{dest_path}"
    encoded = quote(dest, safe="")
    return f"{AFFILIATE_BASE}?lc={AFFILIATE_LC}&atid={AFFILIATE_ATID}&url={encoded}"


# =========================================================
# FULL PAGE ROSTER  (slug → metadata + merchant path)
# =========================================================

PAGES = [
    {
        "slug":        "index",
        "filename":    "index.html",
        "title":       f"Halloween Costumes {YEAR}",
        "h1":          f"🎃 Halloween Costumes {YEAR} — World's #1 Store",
        "description": f"Halloween costumes {YEAR} — the world's best deals. Kids, adults, scary, funny, sexy, couples, group, wholesale, pet, accessories and decorations. Ships to 200+ countries.",
        "merchant":    "/",
        "emoji":       "🏠",
        "label":       "Main Showcase",
        "priority":    "1.0",
    },
    {
        "slug":        "womens-costumes-2026",
        "filename":    "womens-costumes-2026.html",
        "title":       f"Women's Halloween Costumes {YEAR}",
        "h1":          f"👩 Women's Halloween Costumes {YEAR}",
        "description": f"Shop the hottest women's Halloween costumes {YEAR}. Sexy, funny, scary, classic and group styles. Fast shipping.",
        "merchant":    "/womens-halloween-costumes.html",
        "emoji":       "👩",
        "label":       "Women's",
        "priority":    "0.9",
    },
    {
        "slug":        "mens-costumes-online",
        "filename":    "mens-costumes-online.html",
        "title":       f"Men's Halloween Costumes {YEAR}",
        "h1":          f"👨 Men's Halloween Costumes {YEAR}",
        "description": f"Best men's Halloween costumes {YEAR}. Superheroes, horror, funny, historical and more. Ships worldwide.",
        "merchant":    "/mens-halloween-costumes.html",
        "emoji":       "👨",
        "label":       "Men's",
        "priority":    "0.9",
    },
    {
        "slug":        "girls-costumes-and-dresses",
        "filename":    "girls-costumes-and-dresses.html",
        "title":       f"Girls' Halloween Costumes {YEAR}",
        "h1":          f"👧 Girls' Halloween Costumes & Dresses {YEAR}",
        "description": f"Adorable girls' Halloween costumes {YEAR}. Princesses, witches, animals, superheroes and more.",
        "merchant":    "/girls-halloween-costumes.html",
        "emoji":       "👧",
        "label":       "Girls'",
        "priority":    "0.85",
    },
    {
        "slug":        "boys-superhero-ninja-costumes",
        "filename":    "boys-superhero-ninja-costumes.html",
        "title":       f"Boys' Halloween Costumes {YEAR}",
        "h1":          f"👦 Boys' Halloween Costumes — Superheroes & Ninjas {YEAR}",
        "description": f"Top boys' Halloween costumes {YEAR}. Superheroes, ninjas, monsters, pirates and more for every age.",
        "merchant":    "/boys-halloween-costumes.html",
        "emoji":       "👦",
        "label":       "Boys'",
        "priority":    "0.85",
    },
    {
        "slug":        "kids-halloween-outfits",
        "filename":    "kids-halloween-outfits.html",
        "title":       f"Kids Halloween Costumes {YEAR}",
        "h1":          f"👶 Kids Halloween Costumes {YEAR}",
        "description": f"Huge selection of kids Halloween costumes {YEAR}. All ages, all styles, all budgets. Fast shipping.",
        "merchant":    "/kids-halloween-costumes.html",
        "emoji":       "👶",
        "label":       "Kids",
        "priority":    "0.85",
    },
    {
        "slug":        "cool-teen-costumes",
        "filename":    "cool-teen-costumes.html",
        "title":       f"Teen Halloween Costumes {YEAR}",
        "h1":          f"🧑 Teen Halloween Costumes {YEAR} — Cool & Trendy",
        "description": f"Cool teen Halloween costumes {YEAR}. Trending pop culture, scary, funny, group costumes and more.",
        "merchant":    "/teen-halloween-costumes.html",
        "emoji":       "🧑",
        "label":       "Teens",
        "priority":    "0.8",
    },
    {
        "slug":        "cute-toddler-costumes",
        "filename":    "cute-toddler-costumes.html",
        "title":       f"Toddler Halloween Costumes {YEAR}",
        "h1":          f"🍼 Cute Toddler Halloween Costumes {YEAR}",
        "description": f"Adorable toddler Halloween costumes {YEAR}. Soft, safe, comfortable and so cute. Ships worldwide.",
        "merchant":    "/toddler-halloween-costumes.html",
        "emoji":       "🍼",
        "label":       "Toddlers",
        "priority":    "0.8",
    },
    {
        "slug":        "infant-baby-costumes",
        "filename":    "infant-baby-costumes.html",
        "title":       f"Baby Halloween Costumes {YEAR}",
        "h1":          f"👼 Baby & Infant Halloween Costumes {YEAR}",
        "description": f"Sweet baby Halloween costumes {YEAR}. Soft fabrics, easy snaps, adorable styles for infants 0–24 months.",
        "merchant":    "/baby-halloween-costumes.html",
        "emoji":       "👼",
        "label":       "Babies",
        "priority":    "0.8",
    },
]


# =========================================================
# STYLES  (shared CSS injected into every page)
# =========================================================

SHARED_CSS = """
  :root {
    --orange: #ff6600;
    --dark:   #111;
    --light:  #f9f9f9;
    --card:   #fff;
    --radius: 8px;
  }
  * { box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.7;
    color: #333;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background: var(--light);
  }
  header {
    background: var(--dark);
    color: #fff;
    padding: 36px 30px;
    text-align: center;
    border-radius: var(--radius);
    margin-bottom: 28px;
  }
  header h1 { color: var(--orange); margin: 0 0 8px; font-size: 2rem; }
  header p  { margin: 0; color: #ccc; font-size: 1rem; }

  .nav-zone {
    background: var(--card);
    border-radius: var(--radius);
    box-shadow: 0 2px 6px rgba(0,0,0,.07);
    padding: 16px 20px;
    margin-bottom: 28px;
  }
  .nav-label {
    font-size: .8rem;
    font-weight: 700;
    color: var(--orange);
    text-transform: uppercase;
    letter-spacing: .6px;
    margin-bottom: 10px;
  }
  nav { display: flex; flex-wrap: wrap; gap: 8px; }
  .nav-link {
    text-decoration: none;
    color: #444;
    padding: 7px 12px;
    background: #eee;
    border-radius: 4px;
    font-size: .88rem;
    transition: background .18s, color .18s;
  }
  .nav-link:hover, .nav-link.active {
    background: var(--orange);
    color: #fff;
  }

  main {
    background: var(--card);
    padding: 40px 44px;
    border-radius: var(--radius);
    box-shadow: 0 2px 6px rgba(0,0,0,.07);
  }
  main h2 { color: var(--orange); margin-top: 2rem; }

  .cta-btn {
    display: inline-block;
    background: var(--orange);
    color: #fff;
    text-decoration: none;
    padding: 16px 34px;
    font-weight: 700;
    border-radius: 5px;
    font-size: 1.15rem;
    margin: 22px 0;
    transition: background .18s, transform .12s;
  }
  .cta-btn:hover { background: #e05500; transform: translateY(-2px); }

  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 18px;
    margin: 28px 0;
  }
  .feature-card {
    background: #fff8f3;
    border: 1px solid #ffe0cc;
    border-radius: 6px;
    padding: 18px;
    text-align: center;
  }
  .feature-card .icon { font-size: 2rem; margin-bottom: 8px; }
  .feature-card h3 { margin: 0 0 6px; font-size: 1rem; color: var(--dark); }
  .feature-card p  { margin: 0; font-size: .88rem; color: #666; }

  .faq { margin-top: 2rem; }
  .faq details {
    border: 1px solid #eee;
    border-radius: 5px;
    margin-bottom: 10px;
    padding: 12px 16px;
  }
  .faq summary { font-weight: 600; cursor: pointer; color: var(--dark); }
  .faq p { margin: 8px 0 0; color: #555; font-size: .93rem; }

  footer {
    margin-top: 30px;
    text-align: center;
    padding: 20px;
    color: #999;
    font-size: .82rem;
  }

  @media (max-width: 600px) {
    main { padding: 24px 18px; }
    header h1 { font-size: 1.4rem; }
  }
"""


# =========================================================
# SCHEMA HELPERS
# =========================================================

def website_schema():
    return f"""{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "{SITE_NAME}",
  "url": "{SITE_URL}/index.html",
  "potentialAction": {{
    "@type": "SearchAction",
    "target": "{SITE_URL}/index.html?q={{search_term_string}}",
    "query-input": "required name=search_term_string"
  }}
}}"""


def breadcrumb_schema(page):
    slug = page["slug"]
    url  = f"{SITE_URL}/{page['filename']}"
    items = [
        f'{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/index.html"}}',
    ]
    if slug != "index":
        items.append(
            f'{{"@type":"ListItem","position":2,"name":"{page["title"]}","item":"{url}"}}'
        )
    return f"""{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [{", ".join(items)}]
}}"""


def faq_schema(faqs):
    entities = []
    for q, a in faqs:
        entities.append(
            f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        )
    return f"""{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{", ".join(entities)}]
}}"""


# =========================================================
# NAV BUILDER
# =========================================================

def build_nav(current_slug):
    links = []
    for p in PAGES:
        active = ' active' if p["slug"] == current_slug else ''
        # nav links are LOCAL (same site), not affiliate links
        href = p["filename"]
        links.append(f'<a href="{href}" class="nav-link{active}">{p["emoji"]} {p["label"]}</a>')
    return "\n".join(links)


# =========================================================
# CONTENT BUILDER  (per-page body)
# =========================================================

def build_content(page):
    title       = page["title"]
    h1          = page["h1"]
    description = page["description"]
    cta_url     = aff(page["merchant"])

    # Feature cards shared across all pages
    features = [
        ("🚀", "Fast Shipping", "Ships to 200+ countries. Get your costume in time."),
        ("💰", "Best Prices",   "Cheap to premium — every budget covered."),
        ("🎭", "Huge Selection","Thousands of styles updated daily."),
        ("⭐", "Top Rated",     "Millions of happy customers worldwide."),
    ]
    feature_html = ""
    for icon, heading, body in features:
        feature_html += f"""
        <div class="feature-card">
          <div class="icon">{icon}</div>
          <h3>{heading}</h3>
          <p>{body}</p>
        </div>"""

    # Page-specific FAQs
    faqs = [
        (f"Where can I buy {title.lower()}?",
         f"You can shop {title.lower()} at HalloweenCostumes.com — the world's largest selection."),
        ("Do you ship internationally?",
         "Yes! Orders ship to 200+ countries worldwide with fast delivery options."),
        ("Are there cheap costume options?",
         "Absolutely. There are hundreds of costumes under $20, $30, and $50 to fit every budget."),
        ("When should I order my Halloween costume?",
         "Order by mid-October to guarantee delivery before Halloween. Early orders get the best selection."),
    ]
    faq_html = ""
    for q, a in faqs:
        faq_html += f"""
        <details>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>"""

    return f"""
      <h1>{h1}</h1>
      <p>{description}</p>

      <center>
        <a href="{cta_url}" class="cta-btn" target="_blank" rel="nofollow noopener">
          Shop {title} Deals Online ➔
        </a>
      </center>

      <h2>Why Shop With Us?</h2>
      <div class="feature-grid">{feature_html}
      </div>

      <h2>About {title}</h2>
      <p>
        Whether you're looking for last-minute deals or planning the perfect look months in advance,
        our curated collection of {title.lower()} has you covered. We partner with
        HalloweenCostumes.com — the internet's #1 Halloween store — to bring you the widest
        selection, the fastest shipping, and the best prices available anywhere online in {YEAR}.
      </p>
      <p>
        From classic scary looks to trending pop-culture characters, budget-friendly options to
        premium exclusive designs, you'll find exactly what you need. New arrivals are added daily
        and inventory moves fast — don't wait!
      </p>

      <center>
        <a href="{cta_url}" class="cta-btn" target="_blank" rel="nofollow noopener">
          Browse All {title} Now ➔
        </a>
      </center>

      <div class="faq">
        <h2>Frequently Asked Questions</h2>
        {faq_html}
      </div>
    """


# =========================================================
# PAGE RENDERER
# =========================================================

def render_page(page):
    slug     = page["slug"]
    title    = page["title"]
    desc     = page["description"]
    canonical = f"{SITE_URL}/{page['filename']}"
    nav_html  = build_nav(slug)
    content   = build_content(page)

    schemas = "\n".join([
        f'<script type="application/ld+json">{website_schema()}</script>',
        f'<script type="application/ld+json">{breadcrumb_schema(page)}</script>',
    ])

    faqs_for_schema = [
        (f"Where can I buy {title.lower()}?",
         f"Shop {title.lower()} at HalloweenCostumes.com."),
        ("Do you ship internationally?",
         "Yes, ships to 200+ countries."),
    ]
    schemas += f'\n<script type="application/ld+json">{faq_schema(faqs_for_schema)}</script>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | {SITE_NAME}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title"       content="{title} | {SITE_NAME}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url"         content="{canonical}">
  <meta property="og:type"        content="website">
  <meta name="twitter:card"       content="summary">
  <meta name="twitter:title"      content="{title} | {SITE_NAME}">
  <meta name="twitter:description" content="{desc}">
  {schemas}
  <style>{SHARED_CSS}</style>
</head>
<body>
  <header>
    <h1>🎃 {SITE_NAME}</h1>
    <p>The World's #1 Halloween Store</p>
  </header>

  <div class="nav-zone">
    <div class="nav-label">Browse All Categories</div>
    <nav>
      {nav_html}
    </nav>
  </div>

  <main>
    {content}
  </main>

  <footer>
    <p>&copy; {YEAR} {OWNER} | Affiliate Platform Portfolio | Powered by Vulture Engine</p>
    <p style="font-size:.75rem; color:#bbb;">
      This site contains affiliate links. We earn a commission when you purchase through our links,
      at no extra cost to you.
    </p>
  </footer>
</body>
</html>"""


# =========================================================
# SITEMAP + ROBOTS
# =========================================================

def build_sitemap():
    urls = ""
    for page in PAGES:
        url = f"{SITE_URL}/{page['filename']}"
        urls += f"""
  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{page['priority']}</priority>
  </url>"""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""


def build_robots():
    return f"""User-agent: *
Allow: /
Disallow: /dist/

Sitemap: {SITE_URL}/sitemap.xml
"""


# =========================================================
# MAIN PIPELINE
# =========================================================

def build_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("🚀 Starting Vulture Engine build...\n")

    # Pages
    for page in PAGES:
        html  = render_page(page)
        path  = os.path.join(OUTPUT_DIR, page["filename"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✔  {page['filename']}")

    # SEO files
    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(build_sitemap())
    print("  ✔  sitemap.xml")

    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(build_robots())
    print("  ✔  robots.txt")

    print(f"\n🏁 Build complete — {len(PAGES)} pages written to /{OUTPUT_DIR}/")
    print(f"   Affiliate ID : {AFFILIATE_ID}")
    print(f"   ATID         : {AFFILIATE_ATID}")
    print(f"   LC           : {AFFILIATE_LC}")


if __name__ == "__main__":
    build_all()
