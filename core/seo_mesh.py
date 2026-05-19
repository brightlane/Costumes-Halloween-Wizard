from core.routes import slug_url


# =========================================================
# MASTER CATEGORY MAP (SINGLE SOURCE OF TRUTH)
# =========================================================
# This is what fixes your “wrong landing page” issue permanently.
# Every internal link and CTA MUST come from here.

CATEGORY_MAP = {
    "main": {
        "title": "Main Showcase",
        "slug": "index",
    },

    "women": {
        "title": "Women's Halloween Costumes 2026",
        "slug": "womens-costumes",
    },

    "men": {
        "title": "Men's Halloween Costumes 2026",
        "slug": "mens-costumes",
    },

    "girls": {
        "title": "Girls' Halloween Costumes 2026",
        "slug": "girls-costumes",
    },

    "boys": {
        "title": "Boys' Halloween Costumes 2026",
        "slug": "boys-costumes",
    },

    "kids": {
        "title": "Kids Halloween Costumes 2026",
        "slug": "kids-costumes",
    },

    "teen": {
        "title": "Teen Halloween Costumes 2026",
        "slug": "teen-costumes",
    },

    "toddler": {
        "title": "Toddler Halloween Costumes 2026",
        "slug": "toddler-costumes",
    },

    "baby": {
        "title": "Baby Halloween Costumes 2026",
        "slug": "baby-costumes",
    },

    "adult": {
        "title": "Adult Halloween Costumes 2026",
        "slug": "adult-costumes",
    },
}


# =========================================================
# INTERNAL LINK GENERATOR (SEO MESH ENGINE)
# =========================================================

def build_mesh(site_url: str, active_key: str = None):
    """
    Builds consistent internal navigation across ALL pages.

    This solves:
    - wrong landing pages
    - inconsistent navigation blocks
    - broken internal SEO structure
    """

    links = []

    for key, data in CATEGORY_MAP.items():

        url = slug_url(site_url, data["slug"])

        links.append({
            "key": key,
            "title": data["title"],
            "url": url,
            "active": (key == active_key)
        })

    return links


# =========================================================
# RENDERED HTML BLOCK (USED IN TEMPLATES)
# =========================================================

def render_mesh_block(site_url: str, active_key: str = None) -> str:
    """
    Converts mesh into safe HTML block for templates.
    Keeps affiliate links untouched.
    """

    links = build_mesh(site_url, active_key)

    html = """
<div class="seo-mesh">
    <h3>Recommended Vault Categories</h3>
    <ul>
"""

    for link in links:
        css = " class='active'" if link["active"] else ""

        html += f"""
        <li{css}>
            <a href="{link['url']}">{link['title']}</a>
        </li>
"""

    html += """
    </ul>
</div>
"""

    return html


# =========================================================
# CTA GENERATOR (ALWAYS CORRECT LANDING PAGES)
# =========================================================

def build_cta(site_url: str, category_key: str, label: str = None) -> str:
    """
    Generates consistent CTA buttons that ALWAYS point
    to correct landing pages.
    """

    if category_key not in CATEGORY_MAP:
        return ""

    data = CATEGORY_MAP[category_key]
    url = slug_url(site_url, data["slug"])

    text = label or f"Shop {data['title']} Deals Online Here ➔"

    return f"""
<div class="seo-cta">
    <a href="{url}" class="cta-button">
        {text}
    </a>
</div>
"""


# =========================================================
# PAGE ENRICHMENT PIPELINE
# =========================================================

def enrich_page(site_url: str, category_key: str, base_content: str):
    """
    This is the KEY FIX:
    Every page now becomes structured:

    - content
    - mesh navigation
    - correct CTA
    """

    return {
        "content": base_content,
        "internal_links": render_mesh_block(site_url, category_key),
        "cta": build_cta(site_url, category_key)
    }
