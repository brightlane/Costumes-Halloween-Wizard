from urllib.parse import quote

# =========================================================
# AFFILIATE CONFIG
# =========================================================

AFF_BASE = (
    "https://www.linkconnector.com/ta.php"
    "?lc=007949060109004909"
    "&atid=WebCostume"
)

DEFAULT_DOMAIN = "https://www.halloweencostumes.com/"

# =========================================================
# SAFE DESTINATION BUILDER
# =========================================================

def build_destination(
    category=None,
    search=None,
    url=None
):

    """
    Returns a clean destination URL BEFORE affiliate wrapping.
    """

    if url:

        return url

    if category:

        return f"{DEFAULT_DOMAIN}{category}.html"

    if search:

        q = quote(search.strip().replace(" ", "+"))

        return f"{DEFAULT_DOMAIN}search?q={q}"

    return DEFAULT_DOMAIN

# =========================================================
# CORE AFFILIATE LINK WRAPPER
# =========================================================

def affiliate_link(
    category=None,
    search=None,
    url=None
):

    """
    Always returns a tracked LinkConnector URL.
    """

    destination = build_destination(
        category=category,
        search=search,
        url=url
    )

    return f"{AFF_BASE}&url={quote(destination, safe='')}"

# =========================================================
# BULK LINK GENERATOR
# =========================================================

def batch_affiliate_links(items):

    """
    Accepts list of dicts:
    {
        "category": "...",
        "search": "...",
        "url": "..."
    }
    """

    links = []

    for item in items:

        links.append(
            affiliate_link(
                category=item.get("category"),
                search=item.get("search"),
                url=item.get("url")
            )
        )

    return links

# =========================================================
# CTA BUILDER (SEO SAFE ANCHORS)
# =========================================================

def build_cta(
    text,
    category=None,
    search=None,
    url=None
):

    link = affiliate_link(
        category=category,
        search=search,
        url=url
    )

    return f'<a href="{link}" target="_blank" rel="nofollow sponsored noopener">{text}</a>'

# =========================================================
# TRACKING VALIDATOR
# =========================================================

def validate_affiliate(url):

    """
    Ensures link is still correctly routed.
    """

    if "linkconnector.com" not in url:

        raise ValueError("Invalid affiliate link detected!")

    if "lc=007949060109004909" not in url:

        raise ValueError("Missing LC tracking ID!")

    return True

# =========================================================
# SEO SAFE SEARCH LINK BUILDER
# =========================================================

def search_link(query):

    return affiliate_link(
        search=query
    )

# =========================================================
# CATEGORY LINK BUILDER
# =========================================================

def category_link(category):

    return affiliate_link(
        category=category
    )

# =========================================================
# DEBUG TEST
# =========================================================

if __name__ == "__main__":

    print(
        affiliate_link(
            search="wizard costume"
        )
    )

    print(
        build_cta(
            "Shop Now",
            search="anime costumes"
        )
    )
