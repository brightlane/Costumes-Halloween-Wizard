from core.routes import slug_url


def build_mesh(site_url, pages):
    """
    Builds a structured SEO internal linking system.

    This creates:
    - hub pages (categories)
    - sibling links
    - related content clusters
    """

    mesh = {}

    # Normalize pages into base structure
    for page in pages:
        slug = page["slug"]

        mesh[slug] = {
            "slug": slug,
            "url": slug_url(site_url, slug),
            "title": page["title"],
            "category": detect_category(slug),
            "related": [],
            "siblings": [],
            "hub": None
        }

    # STEP 1: GROUP BY CATEGORY (SILO SYSTEM)
    categories = {}

    for slug, data in mesh.items():
        cat = data["category"]

        if cat not in categories:
            categories[cat] = []

        categories[cat].append(slug)

    # STEP 2: BUILD SIBLING LINKS (same category)
    for cat, slugs in categories.items():

        for slug in slugs:
            mesh[slug]["siblings"] = [
                mesh[s]["url"]
                for s in slugs
                if s != slug
            ]

    # STEP 3: BUILD RELATED LINKS (cross-category lightweight mesh)
    all_slugs = list(mesh.keys())

    for slug in all_slugs:

        related = []

        for other in all_slugs:

            if other == slug:
                continue

            # lightweight relevance logic
            if is_related(mesh[slug], mesh[other]):
                related.append(mesh[other]["url"])

        mesh[slug]["related"] = related[:5]  # limit for SEO safety

    # STEP 4: ASSIGN HUB PAGES
    for cat, slugs in categories.items():

        hub_slug = slugs[0]

        for slug in slugs:
            mesh[slug]["hub"] = mesh[hub_slug]["url"]

    return mesh


# =========================================================
# CATEGORY DETECTION (IMPORTANT FOR LANDING PAGES)
# =========================================================

def detect_category(slug):

    slug = slug.lower()

    if "women" in slug:
        return "women"
    if "men" in slug:
        return "men"
    if "kids" in slug:
        return "kids"
    if "girls" in slug:
        return "kids"
    if "boys" in slug:
        return "kids"
    if "baby" in slug:
        return "baby"

    return "general"


# =========================================================
# RELATIONSHIP ENGINE (SEO LINKING LOGIC)
# =========================================================

def is_related(page_a, page_b):

    # same category = strongly related
    if page_a["category"] == page_b["category"]:
        return True

    # lightweight cross-category relationships
    keywords_a = set(page_a["slug"].split("-"))
    keywords_b = set(page_b["slug"].split("-"))

    overlap = keywords_a.intersection(keywords_b)

    return len(overlap) >= 1
