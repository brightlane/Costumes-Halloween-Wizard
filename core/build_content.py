def build_content(route, internal_links, affiliate_url):
    """
    Stable SEO content generator (no dependencies)
    """

    title = route["title"]
    desc = route["description"]

    # -----------------------------
    # INTERNAL LINKS (SEO MESH)
    # -----------------------------
    links_html = ""

    for link in internal_links:
        links_html += f"""
        <li>
            <a href="{link['url']}">
                {link['label']}
            </a>
        </li>
        """

    # -----------------------------
    # PAGE BODY
    # -----------------------------
    return f"""
    <section class="hero">
        <h1>{title}</h1>
        <p>{desc}</p>
    </section>

    <section class="seo-mesh">
        <h2>Recommended Vault Categories</h2>
        <ul>
            {links_html}
        </ul>
    </section>

    <section class="affiliate-cta">
        <a href="{affiliate_url}">
            Shop {title} Deals ➜
        </a>
    </section>

    <footer>
        <p>Updated for 2026 Halloween season</p>
    </footer>
    """
