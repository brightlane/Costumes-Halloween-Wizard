# core/affiliates.py

from urllib.parse import urlencode

# =========================================================
# GLOBAL AFFILIATE CONFIG
# =========================================================

AFFILIATE_ID = "your_affiliate_id_here"
BASE_OUTBOUND = "https://example.com/deals"  # replace with real merchant base

# =========================================================
# CORE AFFILIATE LINK BUILDER
# =========================================================

def affiliate_link(slug: str, campaign: str = "default", label: str = "Shop Now") -> str:
    """
    Generates tracked affiliate URLs consistently across entire site.
    """

    params = {
        "aff": AFFILIATE_ID,
        "src": campaign,
        "tag": slug
    }

    url = f"{BASE_OUTBOUND}?{urlencode(params)}"

    return f'<a href="{url}" rel="nofollow sponsored">{label}</a>'


# =========================================================
# CATEGORY MAPPING (IMPORTANT FOR SEO + CONVERSION)
# =========================================================

AFFILIATE_CAMPAIGNS = {
    "index": "home",
    "women": "women_costumes",
    "men": "men_costumes",
    "kids": "kids_costumes",
    "girls": "girls_costumes",
    "boys": "boys_costumes",
    "toddler": "toddler_costumes",
    "baby": "baby_costumes",
    "teen": "teen_costumes",
    "adult": "adult_costumes",
}


def category_affiliate(slug: str) -> str:
    """
    Returns category-specific affiliate link.
    """
    campaign = AFFILIATE_CAMPAIGNS.get(slug, "generic")

    return affiliate_link(
        slug=slug,
        campaign=campaign,
        label="Shop Deals ➜"
    )
