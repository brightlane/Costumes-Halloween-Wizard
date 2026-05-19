from core.routes import slug_url


def build_mesh(site_url, pages):
    """
    Creates a structured internal linking graph.
    Every page gets:
    - parent hub
    - related pages
    - category siblings
    """

    mesh = {}

    for page in pages:
        slug = page["slug"]

        mesh[slug] = {
            "url": slug_url(site_url, slug),
            "title": page["title"],
            "related": []
        }

    # build relationships (simple SEO clustering)
    for page in pages:
        slug = page["slug"]

        for other in pages:
            if other["slug"] != slug:

                # same category grouping logic
                if any(word in other["slug"] for word in slug.split("-")[0:1]):
                    mesh[slug]["related"].append(mesh[other["slug"]]["url"])

    return mesh
