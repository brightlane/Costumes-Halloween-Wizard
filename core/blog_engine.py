from datetime import date
from core.affiliates import affiliate_link
from core.seo import (
    slugify,
    build_title,
    build_description
)

TODAY = str(date.today())

# =========================================================
# BLOG TOPIC DATABASE
# =========================================================

BLOG_TOPICS = [

    "Best Scary Halloween Costumes",
    "Best Funny Halloween Costumes",
    "Trending Anime Costumes",
    "Best Couples Halloween Costumes",
    "Easy Last Minute Costumes",
    "Best Kids Halloween Costumes",
    "Top Horror Movie Costumes",
    "Best Cosplay Ideas",
    "Best Group Costume Ideas",
    "Most Popular Costumes 2026",
    "Halloween Costume Trends",
    "Cheap Halloween Costumes",
    "DIY Costume Ideas",
    "Best Witch Costumes",
    "Best Vampire Costumes",
    "Top Zombie Costumes",
    "Best Wizard Robes",
    "Best Superhero Costumes",
    "Top Disney Costumes",
    "Best Pet Halloween Costumes"
]

# =========================================================
# MULTILINGUAL TITLES
# =========================================================

TRANSLATIONS = {

    "es": {
        "read_more":
        "Leer más",

        "shop_now":
        "Comprar ahora",

        "trending":
        "Tendencias"
    },

    "fr": {
        "read_more":
        "Lire plus",

        "shop_now":
        "Acheter",

        "trending":
        "Tendance"
    },

    "de": {
        "read_more":
        "Mehr lesen",

        "shop_now":
        "Jetzt kaufen",

        "trending":
        "Trends"
    }
}

# =========================================================
# ARTICLE GENERATOR
# =========================================================

def generate_article(
    topic,
    lang="en"
):

    slug = slugify(topic)

    title = build_title(topic)

    description = build_description(topic)

    article = {

        "slug":
        slug,

        "title":
        title,

        "description":
        description,

        "date":
        TODAY,

        "lang":
        lang,

        "body":
        build_article_body(
            topic,
            lang
        )
    }

    return article

# =========================================================
# ARTICLE BODY BUILDER
# =========================================================

def build_article_body(
    topic,
    lang="en"
):

    cta = affiliate_link(
        search=topic
    )

    intro = f"""
<p>
{topic} are exploding in popularity for Halloween 2026.
This year's trends include horror aesthetics, anime cosplay,
gaming characters, movie villains, funny memes,
and premium cinematic costume replicas.
</p>
"""

    trends = f"""
<h2>Trending {topic} Styles</h2>

<p>
Consumers are searching for realistic materials,
movie-accurate accessories,
LED enhancements,
inflatable builds,
and social-media-friendly costume designs.
</p>

<p>
Premium cosplay quality and comfort are becoming
major buying factors for Halloween shoppers.
</p>
"""

    buying = f"""
<h2>Where To Buy {topic}</h2>

<p>
Finding authentic quality matters.
Cheap materials often fail during conventions,
Halloween parties,
or trick-or-treat events.
</p>

<p>
We recommend trusted official retailers
with verified shipping,
sizing support,
and reliable customer service.
</p>

<p>
<a href="{cta}" class="cta-button" target="_blank" rel="nofollow sponsored noopener">
Shop {topic} Deals Here →
</a>
</p>
"""

    seo_block = f"""
<h2>Why {topic} Are Trending In 2026</h2>

<p>
Search interest for {topic} has increased dramatically
due to TikTok cosplay culture,
anime fandom growth,
streaming platform popularity,
and convention attendance spikes worldwide.
</p>

<p>
Social media creators,
YouTube influencers,
and Instagram cosplay communities
continue driving massive seasonal demand.
</p>
"""

    faq = f"""
<h2>Frequently Asked Questions</h2>

<h3>What are the best {topic}?</h3>

<p>
The best options combine comfort,
durability,
screen accuracy,
and high-quality accessories.
</p>

<h3>Are {topic} popular this year?</h3>

<p>
Yes.
Search trends show extremely strong growth
for this category in 2026.
</p>

<h3>Where can I buy {topic} online?</h3>

<p>
You can shop trusted costume retailers using
the links above for verified inventory
and seasonal discounts.
</p>
"""

    return (
        intro +
        trends +
        buying +
        seo_block +
        faq
    )

# =========================================================
# BULK ARTICLE GENERATOR
# =========================================================

def generate_all_articles():

    articles = []

    for topic in BLOG_TOPICS:

        article = generate_article(topic)

        articles.append(article)

    return articles

# =========================================================
# BLOG CATEGORY CLUSTERS
# =========================================================

BLOG_CLUSTERS = {

    "anime": [

        "Naruto Costumes",
        "One Piece Cosplay",
        "Jujutsu Kaisen Costumes",
        "Demon Slayer Outfits",
        "Attack on Titan Cosplay"
    ],

    "gaming": [

        "Fortnite Costumes",
        "Minecraft Costumes",
        "League of Legends Cosplay",
        "Zelda Costumes",
        "Cyberpunk Outfits"
    ],

    "horror": [

        "Zombie Costumes",
        "Ghostface Costumes",
        "Clown Costumes",
        "Vampire Outfits",
        "Haunted House Themes"
    ]
}

# =========================================================
# CLUSTER ARTICLE ENGINE
# =========================================================

def generate_cluster_articles():

    pages = []

    for cluster, topics in BLOG_CLUSTERS.items():

        for topic in topics:

            pages.append(
                generate_article(topic)
            )

    return pages

# =========================================================
# INTERNAL LINK BLOCK
# =========================================================

def related_articles_html(
    articles,
    limit=5
):

    html = [
        "<div class='related-posts'>",
        "<h2>Related Articles</h2>",
        "<ul>"
    ]

    for article in articles[:limit]:

        html.append(

            f"<li>"
            f"<a href='/blog/{article['slug']}/'>"
            f"{article['title']}"
            f"</a>"
            f"</li>"
        )

    html.append("</ul></div>")

    return "\n".join(html)

# =========================================================
# BLOG INDEX PAGE
# =========================================================

def build_blog_index(
    articles
):

    html = [
        "<h1>Halloween Costume Blog</h1>",
        "<div class='blog-grid'>"
    ]

    for article in articles:

        html.append(f"""
<article class="blog-card">

<h2>
<a href="/blog/{article['slug']}/">
{article['title']}
</a>
</h2>

<p>
{article['description']}
</p>

<a href="/blog/{article['slug']}/"
class="read-more">
Read More →
</a>

</article>
""")

    html.append("</div>")

    return "\n".join(html)

# =========================================================
# TRENDING KEYWORD GENERATOR
# =========================================================

def trending_keywords():

    keywords = []

    for topic in BLOG_TOPICS:

        keywords.extend([

            f"{topic} 2026",
            f"cheap {topic}",
            f"best {topic}",
            f"{topic} ideas",
            f"{topic} trends",
            f"{topic} online"
        ])

    return keywords

# =========================================================
# DEBUG TEST
# =========================================================

if __name__ == "__main__":

    articles = generate_all_articles()

    print(articles[0]["title"])

    print(articles[0]["body"][:1000])
