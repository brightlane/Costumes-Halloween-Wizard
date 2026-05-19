import json

# =========================================================
# GENERIC JSON-LD SERIALIZER
# =========================================================

def to_json_ld(data):

    return json.dumps(
        data,
        ensure_ascii=False,
        separators=(",", ":")
    )

# =========================================================
# ORGANIZATION SCHEMA
# =========================================================

def organization_schema(
    site_name,
    site_url,
    logo_url=None
):

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "Organization",

        "name":
        site_name,

        "url":
        site_url
    }

    if logo_url:

        schema["logo"] = logo_url

    return to_json_ld(schema)

# =========================================================
# WEBSITE SCHEMA
# =========================================================

def website_schema(
    site_name,
    site_url
):

    return to_json_ld({

        "@context":
        "https://schema.org",

        "@type":
        "WebSite",

        "name":
        site_name,

        "url":
        site_url
    })

# =========================================================
# COLLECTION PAGE SCHEMA
# =========================================================

def collection_schema(
    title,
    description,
    url
):

    return to_json_ld({

        "@context":
        "https://schema.org",

        "@type":
        "CollectionPage",

        "name":
        title,

        "description":
        description,

        "url":
        url
    })

# =========================================================
# ARTICLE SCHEMA
# =========================================================

def article_schema(
    title,
    description,
    url,
    image=None,
    author="Benny Palmarino",
    publisher="Halloween Costumes 2026"
):

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "Article",

        "headline":
        title,

        "description":
        description,

        "author": {

            "@type":
            "Person",

            "name":
            author
        },

        "publisher": {

            "@type":
            "Organization",

            "name":
            publisher
        },

        "mainEntityOfPage":
        url
    }

    if image:

        schema["image"] = image

    return to_json_ld(schema)

# =========================================================
# FAQ SCHEMA
# =========================================================

def faq_schema(questions):

    entities = []

    for q in questions:

        entities.append({

            "@type":
            "Question",

            "name":
            q["q"],

            "acceptedAnswer": {

                "@type":
                "Answer",

                "text":
                q["a"]
            }
        })

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "FAQPage",

        "mainEntity":
        entities
    }

    return to_json_ld(schema)

# =========================================================
# BREADCRUMB SCHEMA
# =========================================================

def breadcrumb_schema(items):

    item_list = []

    for idx, item in enumerate(items, start=1):

        item_list.append({

            "@type":
            "ListItem",

            "position":
            idx,

            "name":
            item["name"],

            "item":
            item["url"]
        })

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "BreadcrumbList",

        "itemListElement":
        item_list
    }

    return to_json_ld(schema)

# =========================================================
# ITEMLIST SCHEMA
# =========================================================

def itemlist_schema(
    title,
    urls
):

    items = []

    for idx, url in enumerate(urls, start=1):

        items.append({

            "@type":
            "ListItem",

            "position":
            idx,

            "url":
            url
        })

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "ItemList",

        "name":
        title,

        "itemListElement":
        items
    }

    return to_json_ld(schema)

# =========================================================
# IMAGE OBJECT SCHEMA
# =========================================================

def image_schema(
    image_url,
    caption=""
):

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "ImageObject",

        "contentUrl":
        image_url
    }

    if caption:

        schema["caption"] = caption

    return to_json_ld(schema)

# =========================================================
# SEARCH ACTION SCHEMA
# =========================================================

def search_action_schema(
    site_url
):

    return to_json_ld({

        "@context":
        "https://schema.org",

        "@type":
        "WebSite",

        "url":
        site_url,

        "potentialAction": {

            "@type":
            "SearchAction",

            "target":
            f"{site_url}/search?q={{search_term_string}}",

            "query-input":
            "required name=search_term_string"
        }
    })

# =========================================================
# LOCAL BUSINESS SCHEMA
# =========================================================

def local_business_schema(
    name,
    url,
    description=""
):

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "LocalBusiness",

        "name":
        name,

        "url":
        url
    }

    if description:

        schema["description"] = description

    return to_json_ld(schema)

# =========================================================
# PERSON SCHEMA
# =========================================================

def person_schema(
    name,
    url=None
):

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "Person",

        "name":
        name
    }

    if url:

        schema["url"] = url

    return to_json_ld(schema)

# =========================================================
# PRODUCT STYLE SCHEMA
# =========================================================

def product_schema(
    name,
    description,
    url,
    image=None,
    brand="Halloween Costumes"
):

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "Product",

        "name":
        name,

        "description":
        description,

        "brand": {

            "@type":
            "Brand",

            "name":
            brand
        },

        "url":
        url
    }

    if image:

        schema["image"] = image

    return to_json_ld(schema)

# =========================================================
# HOWTO SCHEMA
# =========================================================

def howto_schema(
    title,
    steps
):

    schema_steps = []

    for idx, step in enumerate(steps, start=1):

        schema_steps.append({

            "@type":
            "HowToStep",

            "position":
            idx,

            "text":
            step
        })

    schema = {

        "@context":
        "https://schema.org",

        "@type":
        "HowTo",

        "name":
        title,

        "step":
        schema_steps
    }

    return to_json_ld(schema)

# =========================================================
# DEBUG TEST
# =========================================================

if __name__ == "__main__":

    faq = faq_schema([

        {
            "q":
            "What are the best Halloween costumes?",

            "a":
            "Anime, horror, funny, and couples costumes are trending."
        }

    ])

    print(faq)
