from urllib.parse import quote

AFF_BASE = "https://www.linkconnector.com/ta.php?lc=007949060109004909&atid=WebCostume"

CAT_URLS = {
    "womens": "https://www.halloweencostumes.com/womens-halloween-costumes.html",
    "mens": "https://www.halloweencostumes.com/mens-halloween-costumes.html",
}

def affiliate_url(cat_key=None, raw_url=None, search=None):

    if cat_key and cat_key in CAT_URLS:
        dest = CAT_URLS[cat_key]

    elif raw_url:
        dest = raw_url

    elif search:
        q = search.replace(" ", "+")
        dest = f"https://www.halloweencostumes.com/search?q={q}"

    else:
        dest = "https://www.halloweencostumes.com/"

    return f"{AFF_BASE}&url={quote(dest, safe='')}"
