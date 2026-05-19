from urllib.parse import quote

# =========================================================
# MASTER AFFILIATE CONFIG
# =========================================================

AFFILIATE_BASE = (
    "https://www.linkconnector.com/ta.php"
    "?lc=007949060109004909"
    "&atid=WebCostume"
)

# =========================================================
# CATEGORY DESTINATION MAP
# =========================================================

CATEGORY_URLS = {

    # =====================================================
    # CORE
    # =====================================================

    "home":
    "https://www.halloweencostumes.com/",

    "womens":
    "https://www.halloweencostumes.com/womens-halloween-costumes.html",

    "mens":
    "https://www.halloweencostumes.com/mens-halloween-costumes.html",

    "kids":
    "https://www.halloweencostumes.com/kids-halloween-costumes.html",

    "toddler":
    "https://www.halloweencostumes.com/toddler-halloween-costumes.html",

    "baby":
    "https://www.halloweencostumes.com/baby-halloween-costumes.html",

    "teen":
    "https://www.halloweencostumes.com/teen-halloween-costumes.html",

    "adult":
    "https://www.halloweencostumes.com/adult-halloween-costumes.html",

    # =====================================================
    # STYLES
    # =====================================================

    "scary":
    "https://www.halloweencostumes.com/scary-halloween-costumes.html",

    "funny":
    "https://www.halloweencostumes.com/funny-halloween-costumes.html",

    "couples":
    "https://www.halloweencostumes.com/couples-halloween-costumes.html",

    "group":
    "https://www.halloweencostumes.com/group-halloween-costumes.html",

    "plussize":
    "https://www.halloweencostumes.com/plus-size-halloween-costumes.html",

    # =====================================================
    # ACCESSORIES
    # =====================================================

    "wigs":
    "https://www.halloweencostumes.com/halloween-wigs.html",

    "masks":
    "https://www.halloweencostumes.com/halloween-masks.html",

    "accessories":
    "https://www.halloweencostumes.com/halloween-costume-accessories.html",

    "makeup":
    "https://www.halloweencostumes.com/halloween-makeup.html",

    # =====================================================
    # DECOR
    # =====================================================

    "decorations":
    "https://www.halloweencostumes.com/halloween-decorations.html",

    "animatronics":
    "https://www.halloweencostumes.com/halloween-animatronics.html",

    "props":
    "https://www.halloweencostumes.com/halloween-props.html",

    "hauntedhouse":
    "https://www.halloweencostumes.com/halloween-decorations.html",

    # =====================================================
    # FANDOMS
    # =====================================================

    "anime":
    "https://www.halloweencostumes.com/search?q=anime+costume",

    "wizard":
    "https://www.halloweencostumes.com/search?q=wizard+costume",

    "videogame":
    "https://www.halloweencostumes.com/video-game-costumes.html",

    "comiccon":
    "https://www.halloweencostumes.com/superhero-costumes.html",

    "fantasy":
    "https://www.halloweencostumes.com/search?q=fantasy+costume",

    "dragon":
    "https://www.halloweencostumes.com/search?q=dragon+costume",

    "princess":
    "https://www.halloweencostumes.com/search?q=princess+costume",

    "mermaid":
    "https://www.halloweencostumes.com/search?q=mermaid+costume",

    "steampunk":
    "https://www.halloweencostumes.com/search?q=steampunk+costume",

    "gothic":
    "https://www.halloweencostumes.com/search?q=gothic+costume",

    "witchaesthetic":
    "https://www.halloweencostumes.com/search?q=witch+costume",

    "gamer":
    "https://www.halloweencostumes.com/search?q=gaming+costume",

    # =====================================================
    # PETS
    # =====================================================

    "pet":
    "https://www.halloweencostumes.com/pet-halloween-costumes.html",

    # =====================================================
    # SPECIAL
    # =====================================================

    "lastminute":
    "https://www.halloweencostumes.com/last-minute-halloween-costumes.html",

    "budget":
    "https://www.halloweencostumes.com/sale-halloween-costumes.html",

    "new2026":
    "https://www.halloweencostumes.com/new-halloween-costumes.html",

    "matchingfamily":
    "https://www.halloweencostumes.com/search?q=family+halloween+costume",

    "officecostume":
    "https://www.halloweencostumes.com/search?q=office+halloween+costume",

    "cosplaywigs":
    "https://www.halloweencostumes.com/halloween-wigs.html",

    "cosplayshoes":
    "https://www.halloweencostumes.com/search?q=cosplay+boots",

    # =====================================================
    # FALLBACK
    # =====================================================

    "default":
    "https://www.halloweencostumes.com/"
}

# =========================================================
# SAFE AFFILIATE BUILDER
# =========================================================

def affiliate_url(
    cat_key=None,
    search=None,
    direct_url=None
):
    """
    Generates a fully tracked LinkConnector affiliate URL.

    PRIORITY:
    1. direct_url
    2. category map
    3. search query
    4. default homepage
    """

    # =====================================================
    # DIRECT URL
    # =====================================================

    if direct_url:

        destination = direct_url

    # =====================================================
    # CATEGORY URL
    # =====================================================

    elif cat_key and cat_key in CATEGORY_URLS:

        destination = CATEGORY_URLS[cat_key]

    # =====================================================
    # SEARCH QUERY
    # =====================================================

    elif search:

        q = search.strip().replace(" ", "+")

        destination = (
            "https://www.halloweencostumes.com/search?q="
            f"{q}"
        )

    # =====================================================
    # DEFAULT
    # =====================================================

    else:

        destination = CATEGORY_URLS["default"]

    # =====================================================
    # FINAL TRACKED URL
    # =====================================================

    encoded_destination = quote(
        destination,
        safe=""
    )

    tracked_url = (
        f"{AFFILIATE_BASE}"
        f"&url={encoded_destination}"
    )

    return tracked_url

# =========================================================
# HTML CTA GENERATOR
# =========================================================

def affiliate_button(
    text="Shop Now",
    cat_key=None,
    search=None,
    direct_url=None,
    css_class="btn"
):

    url = affiliate_url(
        cat_key=cat_key,
        search=search,
        direct_url=direct_url
    )

    return f'''
<a
href="{url}"
class="{css_class}"
target="_blank"
rel="nofollow sponsored noopener">

{text}

</a>
'''

# =========================================================
# TESTING
# =========================================================

if __name__ == "__main__":

    print(
        affiliate_url(cat_key="wizard")
    )

    print(
        affiliate_url(search="anime costume")
    )
