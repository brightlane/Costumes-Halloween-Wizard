# core/routes.py

SITE_BASE = "https://brightlane.github.io/Costumes-Halloween-Wizard"

# ---------------------------------------------------------
# CENTRAL ROUTE MAP (single source of truth)
# ---------------------------------------------------------

ROUTES = {
    "index": "index.html",

    "women": "womens-costumes-2026.html",
    "men": "mens-costumes-online.html",
    "kids": "kids-halloween-outfits.html",
    "girls": "girls-costumes-and-dresses.html",
    "boys": "boys-superhero-ninja-costumes.html",
    "toddler": "cute-toddler-costumes.html",
    "baby": "infant-baby-costumes.html",
    "teen": "cool-teen-costumes.html",
    "adult": "sexy-adult-costumes.html",
}

# ---------------------------------------------------------
# CORE URL BUILDER (THIS is what build.py imports)
# ---------------------------------------------------------

def slug_url(slug: str) -> str:
    """
    Returns full canonical URL for a given internal slug.
    Always safe fallback if slug missing.
    """
    file = ROUTES.get(slug, f"{slug}.html")
    return f"{SITE_BASE}/{file}"

# ---------------------------------------------------------
# SEO INTERNAL LINK HELPER
# ---------------------------------------------------------

def internal_link(slug: str, label: str) -> str:
    return f'<a href="{slug_url(slug)}">{label}</a>'

# ---------------------------------------------------------
# SAFETY CHECK (helps debug future CI failures)
# ---------------------------------------------------------

def validate_routes():
    missing = [k for k, v in ROUTES.items() if not v.endswith(".html")]
    if missing:
        raise ValueError(f"Invalid route definitions: {missing}")
