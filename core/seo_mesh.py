# core/seo_mesh.py

from core.routes import slug_url

# ---------------------------------------------------------
# SEO MESH GRAPH (RELATIONSHIPS BETWEEN PAGES)
# ---------------------------------------------------------

MESH = {
    "index": ["women", "men", "kids", "teen", "baby"],

    "women": ["men", "kids", "teen"],
    "men": ["women", "kids", "adult"],
    "kids": ["girls", "boys", "toddler", "baby"],
    "girls": ["kids", "women"],
    "boys": ["kids", "men"],
    "toddler": ["baby", "kids"],
    "baby": ["toddler", "kids"],
    "teen": ["women", "men", "kids"],
    "adult": ["men", "women"]
}

# ---------------------------------------------------------
# BUILD INTERNAL LINK BLOCK
# ---------------------------------------------------------

def build_mesh_links(slug: str, limit: int = 6) -> str:
    related = MESH.get(slug, ["index"])

    links = []

    for target in related[:limit]:
        links.append(f'<a href="{slug_url(target)}">{target.replace("-", " ").title()}</a>')

    return "<div class='seo-mesh'>" + " | ".join(links) + "</div>"

# ---------------------------------------------------------
# OPTIONAL: CONTEXT BOOST LINKS (footer reinforcement)
# ---------------------------------------------------------

def build_footer_mesh():
    return f"""
    <div class="footer-mesh">
        <a href="{slug_url('index')}">Home</a> |
        <a href="{slug_url('women')}">Women</a> |
        <a href="{slug_url('men')}">Men</a> |
        <a href="{slug_url('kids')}">Kids</a>
    </div>
    """
