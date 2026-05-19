from urllib.parse import quote

# =========================================================
# AFFILIATE CONFIG (KEEP YOUR TRACKING INTACT)
# =========================================================

AFF_BASE = (
    "https://www.linkconnector.com/ta.php"
    "?lc=007949060109004909"
    "&atid=WebCostume"
)

DEFAULT_DOMAIN = "https://www.halloweencostumes.com/"

# =========================================================
# BUILD CLEAN DESTINATION URL
# =========================================================

def build_destination(category=None, search=None, url=None):

    if url:
        return url

    if category:
        return f"{DEFAULT_DOMAIN}{category}.html"

    if search:
        q = quote(search.strip().replace(" ", "+"))
        return f"{DEFAULT_DOMAIN}search?q={q}"

    return DEFAULT_DOMAIN

# =========================================================
# MAIN AFFILIATE WRAPPER
# =========================================================

def affiliate_link(category=None, search=None, url=None):

    destination = build_destination(
        category=category,
        search=search,
        url=url
    )

    return f"{AFF_BASE}&url={quote(destination, safe='')}"
