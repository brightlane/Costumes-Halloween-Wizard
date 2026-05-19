from collections import defaultdict

# =========================================================
# PAGE CLASSIFICATION (SEO INTENT GRAPH)
# =========================================================

HUB_PAGES = {
    "index",
    "womens-costumes-2026",
    "mens-costumes-online",
    "kids-halloween-outfits",
    "infant-baby-costumes"
}

# =========================================================
# GRAPH BUILDER
# =========================================================

class SEOMeshEngine:
    def __init__(self, routes):
        self.routes = routes
        self.graph = defaultdict(list)
        self.slug_map = {r["slug"]: r for r in routes}

    # -----------------------------------------------------
    # NODE TYPE DETECTION
    # -----------------------------------------------------

    def node_type(self, slug):
        if slug in HUB_PAGES:
            return "hub"
        return "cluster"

    # -----------------------------------------------------
    # BUILD GRAPH CONNECTIONS
    # -----------------------------------------------------

    def build_graph(self):
        slugs = [r["slug"] for r in self.routes]

        for slug in slugs:
            for target in slugs:
                if slug == target:
                    continue

                self.graph[slug].append({
                    "slug": target,
                    "type": self.edge_type(slug, target),
                    "weight": self.weight(slug, target)
                })

        return self.graph

    # -----------------------------------------------------
    # EDGE TYPE LOGIC
    # -----------------------------------------------------

    def edge_type(self, source, target):
        if source in HUB_PAGES:
            return "hub_link"
        if target in HUB_PAGES:
            return "upward_link"
        return "peer_link"

    # -----------------------------------------------------
    # WEIGHTING SYSTEM (REAL SEO CONTROL)
    # -----------------------------------------------------

    def weight(self, source, target):
        source_type = self.node_type(source)
        target_type = self.node_type(target)

        # HUB → EVERYTHING (strong)
        if source_type == "hub":
            return 1.0

        # CLUSTER → HUB (important upward signal)
        if target_type == "hub":
            return 0.8

        # CLUSTER → CLUSTER (weaker to avoid dilution)
        return 0.3

    # -----------------------------------------------------
    # GET OPTIMIZED LINKS FOR A PAGE
    # -----------------------------------------------------

    def get_links(self, slug, limit=6):
        links = self.graph.get(slug, [])

        sorted_links = sorted(
            links,
            key=lambda x: x["weight"],
            reverse=True
        )

        return sorted_links[:limit]

    # -----------------------------------------------------
    # CONTEXT-AWARE SEO MESH OUTPUT
    # -----------------------------------------------------

    def build_mesh_for_page(self, slug):
        links = self.get_links(slug)

        return [
            {
                "label": self.slug_map[l["slug"]]["title"],
                "url": f"{l['slug']}.html",
                "weight": l["weight"]
            }
            for l in links
        ]
