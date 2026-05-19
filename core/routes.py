# core/routes.py

from dataclasses import dataclass
from typing import Dict, List, Optional


# =========================================================
# ROUTE MODEL
# =========================================================

@dataclass(frozen=True)
class Route:
    slug: str
    title: str
    parent: Optional[str]
    level: int
    affiliate_target: str


# =========================================================
# CANONICAL ROUTE MAP (SOURCE OF TRUTH)
# IMPORTANT: These MUST match your generated HTML filenames
# =========================================================

ROUTES: Dict[str, Route] = {

    # =========================
    # MAIN HUB
    # =========================
    "index": Route(
        slug="index",
        title="Halloween Costumes 2026",
        parent=None,
        level=0,
        affiliate_target="/index.html"
    ),

    # =========================
    # ADULT HUB
    # =========================
    "adult": Route(
        slug="adult-costumes-apparel",
        title="Adult Halloween Costumes",
        parent="index",
        level=1,
        affiliate_target="/adult-costumes-apparel.html"
    ),

    "women": Route(
        slug="womens-costumes-2026",
        title="Women's Halloween Costumes 2026",
        parent="adult",
        level=2,
        affiliate_target="/womens-costumes-2026.html"
    ),

    "men": Route(
        slug="mens-costumes-online",
        title="Men's Halloween Costumes 2026",
        parent="adult",
        level=2,
        affiliate_target="/mens-costumes-online.html"
    ),

    # =========================
    # KIDS HUB (IMPORTANT FIX)
    # =========================
    "kids": Route(
        slug="kids-halloween-outfits",
        title="Kids Halloween Costumes 2026",
        parent="index",
        level=1,
        affiliate_target="/kids-halloween-outfits.html"
    ),

    "girls": Route(
        slug="girls-costumes-and-dresses",
        title="Girls Halloween Costumes 2026",
        parent="kids",
        level=2,
        affiliate_target="/girls-costumes-and-dresses.html"
    ),

    "boys": Route(
        slug="boys-superhero-ninja-costumes",
        title="Boys Halloween Costumes 2026",
        parent="kids",
        level=2,
        affiliate_target="/boys-superhero-ninja-costumes.html"
    ),

    "toddler": Route(
        slug="cute-toddler-costumes",
        title="Toddler Halloween Costumes 2026",
        parent="kids",
        level=2,
        affiliate_target="/cute-toddler-costumes.html"
    ),

    "baby": Route(
        slug="infant-baby-costumes",
        title="Baby Halloween Costumes 2026",
        parent="kids",
        level=2,
        affiliate_target="/infant-baby-costumes.html"
    ),

    "teen": Route(
        slug="cool-teen-costumes",
        title="Teen Halloween Costumes 2026",
        parent="kids",
        level=2,
        affiliate_target="/cool-teen-costumes.html"
    ),
}


# =========================================================
# CORE RESOLVERS
# =========================================================

def get_route(key: str) -> Route:
    """Get a route by key. Fails loudly if missing (prevents silent SEO bugs)."""
    if key not in ROUTES:
        raise ValueError(f"[ROUTES] Missing route definition: {key}")
    return ROUTES[key]


def get_url(key: str) -> str:
    """Return canonical URL for a route."""
    return get_route(key).affiliate_target


def get_parent(key: str) -> Optional[str]:
    """Return parent route key."""
    return get_route(key).parent


# =========================================================
# INTERNAL LINK HELPERS (THIS FIXES YOUR SEO MESH ISSUE)
# =========================================================

def get_children(parent_key: str) -> List[Route]:
    """Get all child routes of a parent."""
    return [
        r for r in ROUTES.values()
        if r.parent == parent_key
    ]


def get_siblings(key: str) -> List[Route]:
    """Get sibling pages (same parent)."""
    parent = get_parent(key)
    if not parent:
        return []
    return [
        r for r in ROUTES.values()
        if r.parent == parent and r.slug != key
    ]


def breadcrumb(key: str) -> List[Route]:
    """Build breadcrumb trail from root → current."""
    trail = []
    current = get_route(key)

    while current:
        trail.append(current)
        if current.parent is None:
            break
        current = get_route(current.parent)

    return list(reversed(trail))


# =========================================================
# SEO MESH CORE (CRITICAL FIX FOR YOUR SYSTEM)
# =========================================================

def build_internal_mesh(key: str) -> Dict[str, List[Route]]:
    """
    This is your SEO graph engine.

    Every page gets:
    - parent
    - children
    - siblings
    """
    return {
        "parent": [get_route(get_parent(key))] if get_parent(key) else [],
        "children": get_children(key),
        "siblings": get_siblings(key),
        "breadcrumb": breadcrumb(key)
    }
