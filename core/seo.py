import re

# =========================================================
# SUPPORTED LANGUAGES
# =========================================================

LANGUAGES = {

    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ja": "Japanese",
    "ko": "Korean"
}

# =========================================================
# SAFE SLUGIFY
# =========================================================

def slugify(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s-]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        "-",
        text
    )

    text = re.sub(
        r"-+",
        "-",
        text
    )

    return text.strip("-")

# =========================================================
# CLEAN META TEXT
# =========================================================

def clean_meta(text):

    text = text.strip()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text

# =========================================================
# CANONICAL URL BUILDER
# =========================================================

def canonical_url(
    site_url,
    lang,
    slug
):

    site_url = site_url.rstrip("/")

    if slug == "index":

        return f"{site_url}/{lang}/"

    return f"{site_url}/{lang}/{slug}/"

# =========================================================
# HREFLANG BUILDER
# =========================================================

def hreflang_tags(
    site_url,
    slug,
    languages=None
):

    if languages is None:

        languages = LANGUAGES.keys()

    tags = []

    for lang in languages:

        tags.append({

            "lang":
            lang,

            "url":
            canonical_url(
                site_url,
                lang,
                slug
            )
        })

    return tags

# =========================================================
# META TITLE BUILDER
# =========================================================

def build_title(
    primary_keyword,
    suffix="Halloween Costumes 2026"
):

    title = f"{primary_keyword} | {suffix}"

    return clean_meta(title)

# =========================================================
# META DESCRIPTION BUILDER
# =========================================================

def build_description(
    keyword,
    extra=""
):

    base = (
        f"Shop {keyword} for Halloween 2026. "
        f"Best deals, trending outfits, cosplay, scary costumes, "
        f"funny looks, accessories, and worldwide shipping."
    )

    if extra:

        base += f" {extra}"

    return clean_meta(base)

# =========================================================
# KEYWORD EXPANSION ENGINE
# =========================================================

def keyword_variants(keyword):

    variants = [

        keyword,

        f"best {keyword}",

        f"cheap {keyword}",

        f"{keyword} online",

        f"{keyword} 2026",

        f"buy {keyword}",

        f"{keyword} near me",

        f"{keyword} ideas",

        f"{keyword} trends",

        f"{keyword} sale"
    ]

    return variants

# =========================================================
# INTERNAL LINK GRAPH
# =========================================================

def related_pages(
    pages,
    current_slug,
    limit=10
):

    related = []

    for page in pages:

        if page["slug"] == current_slug:

            continue

        related.append(page)

    return related[:limit]

# =========================================================
# OPEN GRAPH TAGS
# =========================================================

def open_graph(
    title,
    description,
    url,
    image=None
):

    tags = {

        "og:title":
        title,

        "og:description":
        description,

        "og:url":
        url,

        "og:type":
        "website"
    }

    if image:

        tags["og:image"] = image

    return tags

# =========================================================
# TWITTER CARD TAGS
# =========================================================

def twitter_tags(
    title,
    description,
    image=None
):

    tags = {

        "twitter:card":
        "summary_large_image",

        "twitter:title":
        title,

        "twitter:description":
        description
    }

    if image:

        tags["twitter:image"] = image

    return tags

# =========================================================
# HTML META RENDERER
# =========================================================

def render_meta_tags(meta):

    lines = []

    for key, value in meta.items():

        lines.append(
            f'<meta name="{key}" content="{value}">'
        )

    return "\n".join(lines)

# =========================================================
# OPEN GRAPH RENDERER
# =========================================================

def render_og_tags(tags):

    lines = []

    for key, value in tags.items():

        lines.append(
            f'<meta property="{key}" content="{value}">'
        )

    return "\n".join(lines)

# =========================================================
# HREFLANG HTML RENDERER
# =========================================================

def render_hreflangs(tags):

    html = []

    for tag in tags:

        html.append(

            f'<link rel="alternate" hreflang="{tag["lang"]}" href="{tag["url"]}">'
        )

    return "\n".join(html)

# =========================================================
# ROBOTS META
# =========================================================

def robots_index():

    return (
        '<meta name="robots" '
        'content="index,follow,max-image-preview:large">'
    )

# =========================================================
# BREADCRUMB BUILDER
# =========================================================

def breadcrumbs(
    site_url,
    lang,
    slug,
    title
):

    items = [

        {
            "name":
            "Home",

            "url":
            f"{site_url}/{lang}/"
        }
    ]

    if slug != "index":

        items.append({

            "name":
            title,

            "url":
            canonical_url(
                site_url,
                lang,
                slug
            )
        })

    return items

# =========================================================
# XML ESCAPE
# =========================================================

def xml_escape(text):

    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")

    return text

# =========================================================
# SITEMAP ENTRY
# =========================================================

def sitemap_entry(
    url,
    lastmod,
    priority="0.8",
    changefreq="weekly"
):

    return f"""
<url>
    <loc>{xml_escape(url)}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
</url>
""".strip()

# =========================================================
# PAGINATION
# =========================================================

def paginate(
    items,
    page_size
):

    pages = []

    for i in range(0, len(items), page_size):

        pages.append(
            items[i:i + page_size]
        )

    return pages

# =========================================================
# CONTENT CLUSTER HELPER
# =========================================================

def cluster_keywords(
    keywords,
    cluster_size=5
):

    return paginate(
        keywords,
        cluster_size
    )

# =========================================================
# DEBUG TEST
# =========================================================

if __name__ == "__main__":

    print(

        canonical_url(
            "https://example.com",
            "en",
            "wizard-costumes"
        )
    )

    print(

        hreflang_tags(
            "https://example.com",
            "wizard-costumes"
        )
    )
