from urllib.parse import urlencode

AFFILIATE_CONFIG = {
    "affiliate_id": "7949",
    "network": "LinkConnector",
    "tracking_url": "https://www.linkconnector.com/ta.php",
    "lc": "007949060109004909",
    "atid": "WebCostume",
    "niche": "Halloween Costumes",
    "owner": "Benny Palmarino"
}


def affiliate_link(search=None, slug=None, tag=None):
    """
    Stable LinkConnector affiliate router
    Ensures attribution is ALWAYS preserved
    """

    base = AFFILIATE_CONFIG["tracking_url"]

    params = {
        "lc": AFFILIATE_CONFIG["lc"],
        "atid": AFFILIATE_CONFIG["atid"],
    }

    # -----------------------------
    # SEO / tracking enrichment
    # -----------------------------
    if search:
        params["q"] = search

    if tag:
        params["tag"] = tag

    if slug:
        params["page"] = slug

    # ALWAYS return tracked link
    return f"{base}?{urlencode(params)}"
