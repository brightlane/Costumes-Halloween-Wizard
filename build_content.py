# core/build_content.py

from core.seo import build_title

def build_content(route, internal_links, affiliate_url):
    """
    SINGLE SOURCE OF TRUTH FOR PAGE BODY CONTENT
    """

    title = route["title"]
    desc = route["description"]

    links_html = "".join([
        f"<li><a href='{link['url']}'>{link['label']}</a></li>"
        for link in internal_links
    ])

    return f"""
    <section class="hero">
        <h1>{build_title(title)}</h1>
        <p>{desc}</p>
    </section>

    <section class="vault">
        <h2>Recommended Vault Categories</h2>
        <ul>
            {links_html}
        </ul>
    </section>

    <section class="cta">
        <a class="affiliate-button" href="{affiliate_url}">
            Shop {title} Deals ➜
        </a>
    </section>
    """
