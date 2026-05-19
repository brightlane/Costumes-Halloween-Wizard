# core/system_lock.py

from core.routes import ROUTES, slug_url

# =========================================================
# SYSTEM LOCK
# Prevents broken pages, broken links, and wrong slugs
# =========================================================

def assert_valid_slug(slug: str):
    """
    HARD FAIL if a slug doesn't exist in ROUTES.
    This prevents silent 404 generation.
    """
    if slug not in ROUTES:
        raise ValueError(f"[SYSTEM LOCK] Invalid slug detected: {slug}")


def safe_url(slug: str) -> str:
    """
    ALWAYS use this instead of manually building URLs.
    Prevents 404 routing drift.
    """
    return slug_url(slug)


def validate_page_set(pages: list):
    """
    Ensures build.py is not generating pages that don't exist in routing.
    """
    for p in pages:
        assert_valid_slug(p["slug"])


def build_safe_link(slug: str, label: str) -> str:
    """
    ONLY safe way to create internal links.
    Prevents broken SEO mesh links.
    """
    return f'<a href="{safe_url(slug)}">{label}</a>'


# =========================================================
# SEO SAFETY CHECK (RUN BEFORE BUILD)
# =========================================================

def prebuild_validation(pages: list):
    """
    Run this before generating ANY files.
    Stops broken deploys BEFORE GitHub Actions.
    """
    validate_page_set(pages)
