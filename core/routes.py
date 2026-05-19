from urllib.parse import quote


# =========================================================
# BASE URL HELPERS
# =========================================================

def normalize_slug(slug: str) -> str:
    """
    Ensures consistent slug formatting across ALL pages.
    Prevents broken internal links + duplicate URLs.
    """
    if not slug:
        return "index"

    slug = slug.strip().lower()
    slug = slug.replace(" ", "-")
    return slug


def slug_url(site_url: str, slug: str) -> str:
    """
    Builds canonical internal URL for a page.

    Example:
    https://site.com/mens-costumes
    """
    slug = normalize_slug(slug)

    if slug == "index":
        return site_url.rstrip("/") + "/"

    return f"{site_url.rstrip('/')}/{quote(slug)}/"


# =========================================================
# AFFILIATE SAFETY LAYER (PRESERVES LINKS)
# =========================================================

def preserve_affiliate_link(url: str) -> str:
    """
    IMPORTANT:
    This function is intentionally passive.

    It does NOT modify affiliate links so you never lose attribution.

    You can later extend this with:
    - tracking params
    - cloaking
    - redirect system

    But for now: ZERO mutation = safest SEO behavior.
    """
    return url


# =========================================================
# INTERNAL LINK BUILDER (SEO MESH READY)
# =========================================================

def internal_link(site_url: str, slug: str, anchor_text: str = None) -> dict:
    """
    Returns structured internal link object used by SEO mesh system.

    This is the foundation for:
    - "related pages"
    - "category clusters"
    - "topic silos"
    """

    url = slug_url(site_url, slug)

    return {
        "url": url,
        "slug": normalize_slug(slug),
        "anchor": anchor_text or slug.replace("-", " ").title()
    }
