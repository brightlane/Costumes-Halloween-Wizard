import os
from datetime import date
from urllib.parse import quote
from collections import defaultdict

# =========================================================
# CONFIG
# =========================================================

SITE_URL     = "https://brightlane.github.io/Costumes-Halloween-Wizard"
OUTPUT_DIR   = "dist"
TODAY        = str(date.today())
SITE_NAME    = "Halloween Costumes 2026"
OWNER        = "Benny Palmarino"
YEAR         = "2026"

AFFILIATE_ID   = "7949"
AFFILIATE_LC   = "007949060109004909"
AFFILIATE_ATID = "WebCostume"
AFFILIATE_BASE = "https://www.linkconnector.com/ta.php"
MERCHANT_BASE  = "https://www.halloweencostumes.com"

def aff(dest_path=""):
    dest    = f"{MERCHANT_BASE}{dest_path}"
    encoded = quote(dest, safe="")
    return f"{AFFILIATE_BASE}?lc={AFFILIATE_LC}&atid={AFFILIATE_ATID}&url={encoded}"


# =========================================================
# SHARED CSS
# =========================================================

SHARED_CSS = """
  :root { --orange:#ff6600; --dark:#111; --light:#f9f9f9; --card:#fff; --radius:8px; }
  * { box-sizing:border-box; }
  body { font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
         line-height:1.7; color:#333; max-width:1200px; margin:0 auto;
         padding:20px; background:var(--light); }
  header { background:var(--dark); color:#fff; padding:36px 30px; text-align:center;
           border-radius:var(--radius); margin-bottom:28px; }
  header h1 { color:var(--orange); margin:0 0 8px; font-size:2rem; }
  header p  { margin:0; color:#ccc; font-size:1rem; }
  .nav-zone { background:var(--card); border-radius:var(--radius);
              box-shadow:0 2px 6px rgba(0,0,0,.07); padding:16px 20px; margin-bottom:28px; }
  .nav-label { font-size:.8rem; font-weight:700; color:var(--orange);
               text-transform:uppercase; letter-spacing:.6px; margin-bottom:10px; }
  nav { display:flex; flex-wrap:wrap; gap:8px; }
  .nav-link { text-decoration:none; color:#444; padding:7px 12px; background:#eee;
              border-radius:4px; font-size:.88rem; transition:background .18s,color .18s; }
  .nav-link:hover,.nav-link.active { background:var(--orange); color:#fff; }
  main { background:var(--card); padding:40px 44px; border-radius:var(--radius);
         box-shadow:0 2px 6px rgba(0,0,0,.07); }
  main h2 { color:var(--orange); margin-top:2rem; }
  .cta-btn { display:inline-block; background:var(--orange); color:#fff;
             text-decoration:none; padding:16px 34px; font-weight:700;
             border-radius:5px; font-size:1.15rem; margin:22px 0;
             transition:background .18s,transform .12s; }
  .cta-btn:hover { background:#e05500; transform:translateY(-2px); }
  .feature-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
                  gap:18px; margin:28px 0; }
  .feature-card { background:#fff8f3; border:1px solid #ffe0cc; border-radius:6px;
                  padding:18px; text-align:center; }
  .feature-card .icon { font-size:2rem; margin-bottom:8px; }
  .feature-card h3 { margin:0 0 6px; font-size:1rem; color:var(--dark); }
  .feature-card p  { margin:0; font-size:.88rem; color:#666; }
  .related-links { margin-top:2rem; }
  .related-links ul { display:flex; flex-wrap:wrap; gap:8px; list-style:none;
                      padding:0; margin:10px 0; }
  .related-links li a { text-decoration:none; color:#444; padding:7px 12px;
                        background:#eee; border-radius:4px; font-size:.88rem;
                        transition:background .18s,color .18s; }
  .related-links li a:hover { background:var(--orange); color:#fff; }
  .faq { margin-top:2rem; }
  .faq details { border:1px solid #eee; border-radius:5px; margin-bottom:10px; padding:12px 16px; }
  .faq summary { font-weight:600; cursor:pointer; color:var(--dark); }
  .faq p { margin:8px 0 0; color:#555; font-size:.93rem; }
  footer { margin-top:30px; text-align:center; padding:20px; color:#999; font-size:.82rem; }
  @media(max-width:600px) { main{padding:24px 18px;} header h1{font-size:1.4rem;} }
"""


# =========================================================
# PRIMARY NAV PAGES
# =========================================================

PAGES = [
    {"slug":"index",             "filename":"index.html",                    "title":f"Halloween Costumes {YEAR}",              "h1":f"🎃 Halloween Costumes {YEAR} — World's #1 Store",                    "description":f"Halloween costumes {YEAR} — the world's best deals. Kids, adults, scary, funny, sexy, couples, group, wholesale, pet, accessories and decorations. Ships to 200+ countries.", "merchant":"/",                                  "emoji":"🏠","label":"Home",       "priority":"1.0"},
    {"slug":"womens-costumes-2026",       "filename":"womens-costumes-2026.html",        "title":f"Women's Halloween Costumes {YEAR}",       "h1":f"👩 Women's Halloween Costumes {YEAR}",                               "description":f"Shop the hottest women's Halloween costumes {YEAR}. Sexy, funny, scary, classic and group styles. Fast shipping.",                                           "merchant":"/womens-costumes.html",     "emoji":"👩","label":"Women's",    "priority":"0.9"},
    {"slug":"mens-costumes-online",       "filename":"mens-costumes-online.html",        "title":f"Men's Halloween Costumes {YEAR}",         "h1":f"👨 Men's Halloween Costumes {YEAR}",                                 "description":f"Best men's Halloween costumes {YEAR}. Superheroes, horror, funny, historical and more. Ships worldwide.",                                                   "merchant":"/mens-costumes.html",       "emoji":"👨","label":"Men's",      "priority":"0.9"},
    {"slug":"girls-costumes-and-dresses", "filename":"girls-costumes-and-dresses.html",  "title":f"Girls' Halloween Costumes {YEAR}",        "h1":f"👧 Girls' Halloween Costumes & Dresses {YEAR}",                      "description":f"Adorable girls' Halloween costumes {YEAR}. Princesses, witches, animals, superheroes and more.",                                                           "merchant":"/girl-costumes.html",      "emoji":"👧","label":"Girls'",     "priority":"0.85"},
    {"slug":"boys-superhero-ninja-costumes","filename":"boys-superhero-ninja-costumes.html","title":f"Boys' Halloween Costumes {YEAR}",       "h1":f"👦 Boys' Halloween Costumes — Superheroes & Ninjas {YEAR}",         "description":f"Top boys' Halloween costumes {YEAR}. Superheroes, ninjas, monsters, pirates and more for every age.",                                                      "merchant":"/boy-costumes.html",       "emoji":"👦","label":"Boys'",      "priority":"0.85"},
    {"slug":"kids-halloween-outfits",     "filename":"kids-halloween-outfits.html",      "title":f"Kids Halloween Costumes {YEAR}",          "h1":f"👶 Kids Halloween Costumes {YEAR}",                                  "description":f"Huge selection of kids Halloween costumes {YEAR}. All ages, all styles, all budgets. Fast shipping.",                                                      "merchant":"/kids-costumes.html",       "emoji":"👶","label":"Kids",       "priority":"0.85"},
    {"slug":"cool-teen-costumes",         "filename":"cool-teen-costumes.html",          "title":f"Teen Halloween Costumes {YEAR}",          "h1":f"🧑 Teen Halloween Costumes {YEAR} — Cool & Trendy",                  "description":f"Cool teen Halloween costumes {YEAR}. Trending pop culture, scary, funny, group costumes and more.",                                                        "merchant":"/teen-costumes.html",       "emoji":"🧑","label":"Teens",      "priority":"0.8"},
    {"slug":"cute-toddler-costumes",      "filename":"cute-toddler-costumes.html",       "title":f"Toddler Halloween Costumes {YEAR}",       "h1":f"🍼 Cute Toddler Halloween Costumes {YEAR}",                          "description":f"Adorable toddler Halloween costumes {YEAR}. Soft, safe, comfortable and so cute. Ships worldwide.",                                                       "merchant":"/toddler-costumes.html",    "emoji":"🍼","label":"Toddlers",   "priority":"0.8"},
    {"slug":"infant-baby-costumes",       "filename":"infant-baby-costumes.html",        "title":f"Baby Halloween Costumes {YEAR}",          "h1":f"👼 Baby & Infant Halloween Costumes {YEAR}",                         "description":f"Sweet baby Halloween costumes {YEAR}. Soft fabrics, easy snaps, adorable styles for infants 0–24 months.",                                                "merchant":"/baby-costumes.html",       "emoji":"👼","label":"Babies",     "priority":"0.8"},
    # Extra root-level pages in repo
    {"slug":"adult-costumes-apparel",     "filename":"adult-costumes-apparel.html",      "title":f"Adult Costume Apparel {YEAR}",            "h1":f"🧑 Adult Costume Apparel {YEAR}",                                    "description":f"Shop adult Halloween costume apparel {YEAR}. Huge selection, fast shipping.",                                                                              "merchant":"/adult-costumes.html",      "emoji":"🧑","label":"Adult",      "priority":"0.75"},
    {"slug":"funny-novelty-costumes",     "filename":"funny-novelty-costumes.html",      "title":f"Funny & Novelty Costumes {YEAR}",         "h1":f"😂 Funny & Novelty Halloween Costumes {YEAR}",                       "description":f"Hilarious funny Halloween costumes {YEAR}. Novelty, gag, and comedy costumes for every event.",                                                            "merchant":"/funny-costumes.html",      "emoji":"😂","label":"Funny",      "priority":"0.75"},
    {"slug":"scary-horror-costumes",      "filename":"scary-horror-costumes.html",       "title":f"Scary Horror Costumes {YEAR}",            "h1":f"💀 Scary Horror Halloween Costumes {YEAR}",                          "description":f"The scariest horror Halloween costumes {YEAR}. Monsters, killers, demons and more.",                                                                       "merchant":"/scary-costumes.html",      "emoji":"💀","label":"Scary",      "priority":"0.75"},
    {"slug":"sexy-adult-costumes",        "filename":"sexy-adult-costumes.html",         "title":f"Sexy Adult Halloween Costumes {YEAR}",    "h1":f"🔥 Sexy Adult Halloween Costumes {YEAR}",                            "description":f"Sexy adult Halloween costumes {YEAR}. Flirty, bold and beautiful styles for women and men.",                                                               "merchant":"/sexy-costumes.html",       "emoji":"🔥","label":"Sexy",       "priority":"0.75"},
    {"slug":"group-family-costumes",      "filename":"group-family-costumes.html",       "title":f"Group & Family Costumes {YEAR}",          "h1":f"👨‍👩‍👧‍👦 Group & Family Halloween Costumes {YEAR}",                             "description":f"Best group and family Halloween costumes {YEAR}. Matching sets for every group size.",                                                                      "merchant":"/group-costume-ideas.html",      "emoji":"👨‍👩‍👧","label":"Groups",    "priority":"0.75"},
    {"slug":"matching-couples-costumes",  "filename":"matching-couples-costumes.html",   "title":f"Couples Halloween Costumes {YEAR}",       "h1":f"💑 Matching Couples Halloween Costumes {YEAR}",                      "description":f"The best matching couples Halloween costumes {YEAR}. Duo sets for every style.",                                                                           "merchant":"/couple-costume-ideas.html",    "emoji":"💑","label":"Couples",    "priority":"0.75"},
    {"slug":"mystical-wizard-robes",      "filename":"mystical-wizard-robes.html",       "title":f"Wizard & Mystical Robes {YEAR}",          "h1":f"🧙 Wizard & Mystical Robes {YEAR}",                                  "description":f"Shop wizard robes, mystical costumes and fantasy Halloween outfits {YEAR}.",                                                                               "merchant":"/fantasy-costumes.html",               "emoji":"🧙","label":"Wizard",     "priority":"0.7"},
]


# =========================================================
# BEST-* CATEGORY PAGES  (100+ cluster pages)
# =========================================================

BEST_PAGES = [
    {"slug":"best-accessories-costumes",    "title":f"Best Halloween Accessories {YEAR}",          "merchant":"/accessories.html"},
    {"slug":"best-adaptive-costumes",       "title":f"Best Adaptive Halloween Costumes {YEAR}",    "merchant":"/kids-costumes.html"},
    {"slug":"best-addamsfamily-costumes",   "title":f"Best Addams Family Costumes {YEAR}",         "merchant":"/scary-costumes.html"},
    {"slug":"best-animals-costumes",        "title":f"Best Animal Halloween Costumes {YEAR}",      "merchant":"/animal-costumes.html"},
    {"slug":"best-animatronics-costumes",   "title":f"Best Animatronic Halloween Props {YEAR}",    "merchant":"/halloween-decorations.html"},
    {"slug":"best-anime-costumes",          "title":f"Best Anime Halloween Costumes {YEAR}",       "merchant":"/anime-costumes.html"},
    {"slug":"best-beetlejuice-costumes",    "title":f"Best Beetlejuice Costumes {YEAR}",           "merchant":"/scary-costumes.html"},
    {"slug":"best-bestsellers-costumes",    "title":f"Best Selling Halloween Costumes {YEAR}",     "merchant":"/best-sellers.html"},
    {"slug":"best-budget-costumes",         "title":f"Best Budget Halloween Costumes {YEAR}",      "merchant":"/costumes-on-sale.html"},
    {"slug":"best-candy-costumes",          "title":f"Best Candy Halloween Costumes {YEAR}",       "merchant":"/food-costumes.html"},
    {"slug":"best-carnival-costumes",       "title":f"Best Carnival Costumes {YEAR}",              "merchant":"/funny-costumes.html"},
    {"slug":"best-casualwear-costumes",     "title":f"Best Halloween Casual Wear {YEAR}",          "merchant":"/adult-costumes.html"},
    {"slug":"best-celebrations-costumes",   "title":f"Best Celebration Costumes {YEAR}",           "merchant":"/"},
    {"slug":"best-celebrity-costumes",      "title":f"Best Celebrity Halloween Costumes {YEAR}",   "merchant":"/adult-costumes.html"},
    {"slug":"best-cheerleader-costumes",    "title":f"Best Cheerleader Costumes {YEAR}",           "merchant":"/cheerleader-costumes.html"},
    {"slug":"best-clearance-costumes",      "title":f"Best Clearance Halloween Costumes {YEAR}",   "merchant":"/costumes-on-sale.html"},
    {"slug":"best-clothing-costumes",       "title":f"Best Halloween Clothing {YEAR}",             "merchant":"/adult-costumes.html"},
    {"slug":"best-collectibles-costumes",   "title":f"Best Halloween Collectibles {YEAR}",         "merchant":"/accessories.html"},
    {"slug":"best-comiccon-costumes",       "title":f"Best Comic Con Costumes {YEAR}",             "merchant":"/adult-costumes.html"},
    {"slug":"best-convention-costumes",     "title":f"Best Convention Costumes {YEAR}",            "merchant":"/adult-costumes.html"},
    {"slug":"best-cosplayshoes-costumes",   "title":f"Best Cosplay Shoes {YEAR}",                  "merchant":"/accessories.html"},
    {"slug":"best-cosplaywigs-costumes",    "title":f"Best Cosplay Wigs {YEAR}",                   "merchant":"/wigs.html"},
    {"slug":"best-couples2-costumes",       "title":f"Best Couples Costumes {YEAR}",               "merchant":"/couple-costume-ideas.html"},
    {"slug":"best-cowgirl-costumes",        "title":f"Best Cowgirl Costumes {YEAR}",               "merchant":"/cowgirl-costumes.html"},
    {"slug":"best-creepydoll-costumes",     "title":f"Best Creepy Doll Costumes {YEAR}",           "merchant":"/scary-costumes.html"},
    {"slug":"best-cyberpunk-costumes",      "title":f"Best Cyberpunk Costumes {YEAR}",             "merchant":"/adult-costumes.html"},
    {"slug":"best-deadbydaylight-costumes", "title":f"Best Dead by Daylight Costumes {YEAR}",      "merchant":"/scary-costumes.html"},
    {"slug":"best-decades-costumes",        "title":f"Best Decades Halloween Costumes {YEAR}",     "merchant":"/decades-costumes.html"},
    {"slug":"best-decorations-costumes",    "title":f"Best Halloween Decorations {YEAR}",          "merchant":"/halloween-decorations.html"},
    {"slug":"best-devilmaycry-costumes",    "title":f"Best Devil May Cry Costumes {YEAR}",         "merchant":"/video-game-costumes.html"},
    {"slug":"best-digital-costumes",        "title":f"Best Digital Halloween Costumes {YEAR}",     "merchant":"/"},
    {"slug":"best-diy-costumes",            "title":f"Best DIY Halloween Costumes {YEAR}",         "merchant":"/adult-costumes.html"},
    {"slug":"best-dragon-costumes",         "title":f"Best Dragon Costumes {YEAR}",                "merchant":"/dragon-costumes.html"},
    {"slug":"best-fantasy-costumes",        "title":f"Best Fantasy Costumes {YEAR}",               "merchant":"/fantasy-costumes.html"},
    {"slug":"best-finalfantasy-costumes",   "title":f"Best Final Fantasy Costumes {YEAR}",         "merchant":"/video-game-costumes.html"},
    {"slug":"best-fnaf-costumes",           "title":f"Best FNAF Costumes {YEAR}",                  "merchant":"/video-game-costumes.html"},
    {"slug":"best-food-costumes",           "title":f"Best Food Halloween Costumes {YEAR}",        "merchant":"/food-costumes.html"},
    {"slug":"best-friendscostume-costumes", "title":f"Best Friends Group Costumes {YEAR}",         "merchant":"/group-costume-ideas.html"},
    {"slug":"best-frieren-costumes",        "title":f"Best Frieren Costumes {YEAR}",               "merchant":"/anime-costumes.html"},
    {"slug":"best-fullbody-costumes",       "title":f"Best Full Body Costumes {YEAR}",             "merchant":"/full-body-costumes.html"},
    {"slug":"best-gamer-costumes",          "title":f"Best Gamer Halloween Costumes {YEAR}",       "merchant":"/video-game-costumes.html"},
    {"slug":"best-genshin-costumes",        "title":f"Best Genshin Impact Costumes {YEAR}",        "merchant":"/anime-costumes.html"},
    {"slug":"best-gifts-costumes",          "title":f"Best Halloween Gifts {YEAR}",                "merchant":"/accessories.html"},
    {"slug":"best-glowinthedark-costumes",  "title":f"Best Glow in the Dark Costumes {YEAR}",     "merchant":"/glow-in-the-dark-costumes.html"},
    {"slug":"best-gnomes-costumes",         "title":f"Best Gnome Costumes {YEAR}",                 "merchant":"/funny-costumes.html"},
    {"slug":"best-gothic-costumes",         "title":f"Best Gothic Costumes {YEAR}",                "merchant":"/gothic-costumes.html"},
    {"slug":"best-halloweendresses-costumes","title":f"Best Halloween Dresses {YEAR}",             "merchant":"/womens-costumes.html"},
    {"slug":"best-halloweenfashion-costumes","title":f"Best Halloween Fashion {YEAR}",             "merchant":"/adult-costumes.html"},
    {"slug":"best-halloweenpajamas-costumes","title":f"Best Halloween Pajamas {YEAR}",             "merchant":"/adult-costumes.html"},
    {"slug":"best-halloweensweaters-costumes","title":f"Best Halloween Sweaters {YEAR}",           "merchant":"/adult-costumes.html"},
    {"slug":"best-harrypotter-costumes",    "title":f"Best Harry Potter Costumes {YEAR}",          "merchant":"/harry-potter-costumes.html"},
    {"slug":"best-hauntedhouse-costumes",   "title":f"Best Haunted House Costumes {YEAR}",         "merchant":"/scary-costumes.html"},
    {"slug":"best-hazbinhotel-costumes",    "title":f"Best Hazbin Hotel Costumes {YEAR}",          "merchant":"/anime-costumes.html"},
    {"slug":"best-hocuspocus-costumes",     "title":f"Best Hocus Pocus Costumes {YEAR}",           "merchant":"/scary-costumes.html"},
    {"slug":"best-horror-costumes",         "title":f"Best Horror Halloween Costumes {YEAR}",      "merchant":"/scary-costumes.html"},
    {"slug":"best-horrornight-costumes",    "title":f"Best Horror Night Costumes {YEAR}",          "merchant":"/scary-costumes.html"},
    {"slug":"best-indoordecor-costumes",    "title":f"Best Indoor Halloween Decorations {YEAR}",   "merchant":"/halloween-decorations.html"},
    {"slug":"best-inflatable-costumes",     "title":f"Best Inflatable Costumes {YEAR}",            "merchant":"/inflatable-costumes.html"},
    {"slug":"best-jujutsukaisen-costumes",  "title":f"Best Jujutsu Kaisen Costumes {YEAR}",        "merchant":"/anime-costumes.html"},
    {"slug":"best-kawaii-costumes",         "title":f"Best Kawaii Costumes {YEAR}",                "merchant":"/anime-costumes.html"},
    {"slug":"best-kpop-costumes",           "title":f"Best K-Pop Costumes {YEAR}",                 "merchant":"/adult-costumes.html"},
    {"slug":"best-larp-costumes",           "title":f"Best LARP Costumes {YEAR}",                  "merchant":"/fantasy-costumes.html"},
    {"slug":"best-lastminute-costumes",     "title":f"Best Last Minute Halloween Costumes {YEAR}", "merchant":"/adult-costumes.html"},
    {"slug":"best-leagueoflegends-costumes","title":f"Best League of Legends Costumes {YEAR}",     "merchant":"/video-game-costumes.html"},
    {"slug":"best-licensed-costumes",       "title":f"Best Licensed Halloween Costumes {YEAR}",    "merchant":"/licensed-costumes.html"},
    {"slug":"best-lighting-costumes",       "title":f"Best Halloween Lighting {YEAR}",             "merchant":"/halloween-decorations.html"},
    {"slug":"best-lolita-costumes",         "title":f"Best Lolita Costumes {YEAR}",                "merchant":"/adult-costumes.html"},
    {"slug":"best-makeup-costumes",         "title":f"Best Halloween Makeup {YEAR}",               "merchant":"/accessories.html"},
    {"slug":"best-masks-costumes",          "title":f"Best Halloween Masks {YEAR}",                "merchant":"/accessories.html"},
    {"slug":"best-masquerade-costumes",     "title":f"Best Masquerade Costumes {YEAR}",            "merchant":"/masquerade-costumes.html"},
    {"slug":"best-matchingfamily-costumes", "title":f"Best Matching Family Costumes {YEAR}",       "merchant":"/group-costume-ideas.html"},
    {"slug":"best-medieval-costumes",       "title":f"Best Medieval Costumes {YEAR}",              "merchant":"/medieval-costumes.html"},
    {"slug":"best-mermaid-costumes",        "title":f"Best Mermaid Costumes {YEAR}",               "merchant":"/mermaid-costumes.html"},
    {"slug":"best-morphsuits-costumes",     "title":f"Best Morphsuits {YEAR}",                     "merchant":"/morphsuits.html"},
    {"slug":"best-movies-costumes",         "title":f"Best Movie Halloween Costumes {YEAR}",       "merchant":"/movie-costumes.html"},
    {"slug":"best-murdermystery-costumes",  "title":f"Best Murder Mystery Costumes {YEAR}",        "merchant":"/adult-costumes.html"},
    {"slug":"best-musicartist-costumes",    "title":f"Best Music Artist Costumes {YEAR}",          "merchant":"/adult-costumes.html"},
    {"slug":"best-new2026-costumes",        "title":f"Best New Halloween Costumes {YEAR}",         "merchant":"/new-costumes.html"},
    {"slug":"best-nier-costumes",           "title":f"Best Nier Automata Costumes {YEAR}",         "merchant":"/video-game-costumes.html"},
    {"slug":"best-nightmarebc-costumes",    "title":f"Best Nightmare Before Christmas Costumes {YEAR}","merchant":"/nightmare-before-christmas-costumes.html"},
    {"slug":"best-occult-costumes",         "title":f"Best Occult Costumes {YEAR}",                "merchant":"/gothic-costumes.html"},
    {"slug":"best-occupation-costumes",     "title":f"Best Occupation Costumes {YEAR}",            "merchant":"/occupation-costumes.html"},
    {"slug":"best-officecostume-costumes",  "title":f"Best Office Halloween Costumes {YEAR}",      "merchant":"/adult-costumes.html"},
    {"slug":"best-onepiececosplay-costumes","title":f"Best One Piece Cosplay Costumes {YEAR}",     "merchant":"/anime-costumes.html"},
    {"slug":"best-outdoordecor-costumes",   "title":f"Best Outdoor Halloween Decorations {YEAR}",  "merchant":"/halloween-decorations.html"},
    {"slug":"best-overwatch-costumes",      "title":f"Best Overwatch Costumes {YEAR}",             "merchant":"/video-game-costumes.html"},
    {"slug":"best-partysupplies-costumes",  "title":f"Best Halloween Party Supplies {YEAR}",       "merchant":"/halloween-decorations.html"},
    {"slug":"best-pet-costumes",            "title":f"Best Pet Halloween Costumes {YEAR}",         "merchant":"/pet-costumes.html"},
    {"slug":"best-piggyback-costumes",      "title":f"Best Piggyback Costumes {YEAR}",             "merchant":"/piggyback-costumes.html"},
    {"slug":"best-plussize-costumes",       "title":f"Best Plus Size Halloween Costumes {YEAR}",   "merchant":"/plus-size-costumes.html"},
    {"slug":"best-plussizecosplay-costumes","title":f"Best Plus Size Cosplay Costumes {YEAR}",     "merchant":"/plus-size-costumes.html"},
    {"slug":"best-preorder-costumes",       "title":f"Best Pre-Order Halloween Costumes {YEAR}",   "merchant":"/new-costumes.html"},
    {"slug":"best-princess-costumes",       "title":f"Best Princess Halloween Costumes {YEAR}",    "merchant":"/princess-costumes.html"},
    {"slug":"best-props-costumes",          "title":f"Best Halloween Props {YEAR}",                "merchant":"/halloween-decorations.html"},
    {"slug":"best-pumpkin-costumes",        "title":f"Best Pumpkin Costumes {YEAR}",               "merchant":"/pumpkin-costumes.html"},
    {"slug":"best-racer-costumes",          "title":f"Best Racer Costumes {YEAR}",                 "merchant":"/adult-costumes.html"},
    {"slug":"best-renfaire-costumes",       "title":f"Best Renaissance Faire Costumes {YEAR}",     "merchant":"/medieval-costumes.html"},
    {"slug":"best-sale-costumes",           "title":f"Best Halloween Costume Sales {YEAR}",        "merchant":"/costumes-on-sale.html"},
    {"slug":"best-scooby-costumes",         "title":f"Best Scooby-Doo Costumes {YEAR}",            "merchant":"/scooby-doo-costumes.html"},
    {"slug":"best-sizecharts-costumes",     "title":f"Halloween Costume Size Charts {YEAR}",       "merchant":"/size-charts.html"},
    {"slug":"best-sizeguide-costumes",      "title":f"Halloween Costume Size Guide {YEAR}",        "merchant":"/size-charts.html"},
    {"slug":"best-skeletons-costumes",      "title":f"Best Skeleton Costumes {YEAR}",              "merchant":"/skeleton-costumes.html"},
    {"slug":"best-spiderwebs-costumes",     "title":f"Best Spider Web Decorations {YEAR}",         "merchant":"/halloween-decorations.html"},
    {"slug":"best-steampunk-costumes",      "title":f"Best Steampunk Costumes {YEAR}",             "merchant":"/steampunk-costumes.html"},
    {"slug":"best-sustainable-costumes",    "title":f"Best Sustainable Halloween Costumes {YEAR}", "merchant":"/adult-costumes.html"},
    {"slug":"best-swimwear-costumes",       "title":f"Best Halloween Swimwear {YEAR}",             "merchant":"/adult-costumes.html"},
    {"slug":"best-themes-costumes",         "title":f"Best Themed Halloween Costumes {YEAR}",      "merchant":"/adult-costumes.html"},
    {"slug":"best-tombstones-costumes",     "title":f"Best Halloween Tombstones {YEAR}",           "merchant":"/halloween-decorations.html"},
    {"slug":"best-trickortreat-costumes",   "title":f"Best Trick or Treat Costumes {YEAR}",        "merchant":"/kids-costumes.html"},
    {"slug":"best-trunkortreat-costumes",   "title":f"Best Trunk or Treat Costumes {YEAR}",        "merchant":"/kids-costumes.html"},
    {"slug":"best-tvshows-costumes",        "title":f"Best TV Show Halloween Costumes {YEAR}",     "merchant":"/tv-show-costumes.html"},
    {"slug":"best-tween-costumes",          "title":f"Best Tween Halloween Costumes {YEAR}",       "merchant":"/tween-costumes.html"},
    {"slug":"best-videogame-costumes",      "title":f"Best Video Game Costumes {YEAR}",            "merchant":"/video-game-costumes.html"},
    {"slug":"best-weeklydeals-costumes",    "title":f"Best Halloween Weekly Deals {YEAR}",         "merchant":"/costumes-on-sale.html"},
    {"slug":"best-wholesale-costumes",      "title":f"Best Wholesale Halloween Costumes {YEAR}",   "merchant":"/wholesale-costumes.html"},
    {"slug":"best-wigs-costumes",           "title":f"Best Halloween Wigs {YEAR}",                 "merchant":"/wigs.html"},
    {"slug":"best-witchaesthetic-costumes", "title":f"Best Witch Aesthetic Costumes {YEAR}",       "merchant":"/witch-costumes.html"},
    {"slug":"best-yearround-costumes",      "title":f"Best Year Round Costumes {YEAR}",            "merchant":"/"},
    {"slug":"best-zelda-costumes",          "title":f"Best Zelda Costumes {YEAR}",                 "merchant":"/video-game-costumes.html"},
]

# Fill in filename and description for best pages automatically
for p in BEST_PAGES:
    p.setdefault("filename",    f"{p['slug']}.html")
    p.setdefault("description", f"{p['title']} — shop the full collection at the world's #1 Halloween store. Fast shipping to 200+ countries.")
    p.setdefault("h1",          p["title"])
    p.setdefault("priority",    "0.7")
    p.setdefault("emoji",       "🎃")
    p.setdefault("label",       p["title"])

ALL_PAGES = PAGES + BEST_PAGES


# =========================================================
# SEO MESH ENGINE  (from core/seo_mesh.py — inlined)
# =========================================================

HUB_SLUGS = {
    "index",
    "womens-costumes-2026",
    "mens-costumes-online",
    "kids-halloween-outfits",
    "infant-baby-costumes",
}

class SEOMeshEngine:
    def __init__(self, routes):
        self.routes   = routes
        self.graph    = defaultdict(list)
        self.slug_map = {r["slug"]: r for r in routes}

    def node_type(self, slug):
        return "hub" if slug in HUB_SLUGS else "cluster"

    def edge_type(self, source, target):
        if source in HUB_SLUGS:  return "hub_link"
        if target in HUB_SLUGS:  return "upward_link"
        return "peer_link"

    def weight(self, source, target):
        if self.node_type(source) == "hub":   return 1.0
        if self.node_type(target) == "hub":   return 0.8
        return 0.3

    def build_graph(self):
        slugs = [r["slug"] for r in self.routes]
        for slug in slugs:
            for target in slugs:
                if slug == target:
                    continue
                self.graph[slug].append({
                    "slug":   target,
                    "type":   self.edge_type(slug, target),
                    "weight": self.weight(slug, target),
                })
        return self.graph

    def get_links(self, slug, limit=6):
        links = self.graph.get(slug, [])
        return sorted(links, key=lambda x: x["weight"], reverse=True)[:limit]

    def build_mesh_for_page(self, slug):
        return [
            {
                "label": self.slug_map[l["slug"]]["title"],
                "url":   f"{l['slug']}.html",
                "weight": l["weight"],
            }
            for l in self.get_links(slug)
        ]


# =========================================================
# SCHEMA HELPERS
# =========================================================

def website_schema():
    return f"""{{
  "@context":"https://schema.org",
  "@type":"WebSite",
  "name":"{SITE_NAME}",
  "url":"{SITE_URL}/index.html",
  "potentialAction":{{"@type":"SearchAction","target":"{SITE_URL}/index.html?q={{search_term_string}}","query-input":"required name=search_term_string"}}
}}"""

def breadcrumb_schema(page):
    url   = f"{SITE_URL}/{page['filename']}"
    items = [f'{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/index.html"}}']
    if page["slug"] != "index":
        items.append(f'{{"@type":"ListItem","position":2,"name":"{page["title"]}","item":"{url}"}}')
    return f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(items)}]}}'

def faq_schema(faqs):
    entities = [
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faqs
    ]
    return f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{",".join(entities)}]}}'


# =========================================================
# NAV BUILDER  (primary pages only — keeps nav clean)
# =========================================================

def build_nav(current_slug):
    links = []
    for p in PAGES:
        active = " active" if p["slug"] == current_slug else ""
        links.append(f'<a href="{p["filename"]}" class="nav-link{active}">{p["emoji"]} {p["label"]}</a>')
    return "\n      ".join(links)


# =========================================================
# CONTENT BUILDER
# =========================================================

def build_content(page, mesh_links):
    title   = page["title"]
    h1      = page["h1"]
    desc    = page["description"]
    cta_url = aff(page["merchant"])

    features = [
        ("🚀","Fast Shipping",   "Ships to 200+ countries. Get your costume in time."),
        ("💰","Best Prices",     "Cheap to premium — every budget covered."),
        ("🎭","Huge Selection",  "Thousands of styles updated daily."),
        ("⭐","Top Rated",       "Millions of happy customers worldwide."),
    ]
    feature_html = "".join(f"""
        <div class="feature-card">
          <div class="icon">{icon}</div>
          <h3>{heading}</h3>
          <p>{body}</p>
        </div>""" for icon, heading, body in features)

    faqs = [
        (f"Where can I buy {title.lower()}?", f"Shop {title.lower()} at HalloweenCostumes.com — the world's largest Halloween store."),
        ("Do you ship internationally?",       "Yes — orders ship to 200+ countries worldwide with fast delivery options."),
        ("Are there budget-friendly options?", "Absolutely. Hundreds of costumes are available under $20, $30, and $50."),
        ("When should I order?",               "Order by mid-October to guarantee Halloween delivery. Early orders get the best selection."),
    ]
    faq_html = "".join(f"""
        <details><summary>{q}</summary><p>{a}</p></details>"""
        for q, a in faqs)

    # SEO mesh related links
    related_html = ""
    if mesh_links:
        items = "".join(f'<li><a href="{l["url"]}">{l["label"]}</a></li>' for l in mesh_links)
        related_html = f"""
      <div class="related-links">
        <h2>Related Categories</h2>
        <ul>{items}</ul>
      </div>"""

    return f"""
      <h1>{h1}</h1>
      <p>{desc}</p>
      <center>
        <a href="{cta_url}" class="cta-btn" target="_blank" rel="nofollow noopener">
          Shop {title} Deals Online ➔
        </a>
      </center>
      <h2>Why Shop With Us?</h2>
      <div class="feature-grid">{feature_html}
      </div>
      <h2>About {title}</h2>
      <p>Whether you're looking for last-minute deals or planning months ahead, our curated
      collection of {title.lower()} has you covered. We partner with HalloweenCostumes.com —
      the internet's #1 Halloween store — to bring you the widest selection, fastest shipping,
      and best prices available anywhere online in {YEAR}. New arrivals added daily.</p>
      <center>
        <a href="{cta_url}" class="cta-btn" target="_blank" rel="nofollow noopener">
          Browse All {title} Now ➔
        </a>
      </center>
      {related_html}
      <div class="faq">
        <h2>Frequently Asked Questions</h2>
        {faq_html}
      </div>"""


# =========================================================
# PAGE RENDERER
# =========================================================

def render_page(page, mesh_links):
    slug      = page["slug"]
    title     = page["title"]
    desc      = page["description"]
    canonical = f"{SITE_URL}/{page['filename']}"
    nav_html  = build_nav(slug)
    content   = build_content(page, mesh_links)

    faqs_schema = [
        (f"Where can I buy {title.lower()}?", f"Shop {title.lower()} at HalloweenCostumes.com."),
        ("Do you ship internationally?",       "Yes, ships to 200+ countries."),
    ]
    schemas = "\n  ".join([
        f'<script type="application/ld+json">{website_schema()}</script>',
        f'<script type="application/ld+json">{breadcrumb_schema(page)}</script>',
        f'<script type="application/ld+json">{faq_schema(faqs_schema)}</script>',
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | {SITE_NAME}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title"       content="{title} | {SITE_NAME}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url"         content="{canonical}">
  <meta property="og:type"        content="website">
  <meta name="twitter:card"        content="summary">
  <meta name="twitter:title"       content="{title} | {SITE_NAME}">
  <meta name="twitter:description" content="{desc}">
  {schemas}
  <style>{SHARED_CSS}</style>
</head>
<body>
  <header>
    <h1>🎃 {SITE_NAME}</h1>
    <p>The World's #1 Halloween Store</p>
  </header>
  <div class="nav-zone">
    <div class="nav-label">Browse All Categories</div>
    <nav>
      {nav_html}
    </nav>
  </div>
  <main>
    {content}
  </main>
  <footer>
    <p>&copy; {YEAR} {OWNER} | Affiliate Platform Portfolio | Powered by Vulture Engine</p>
    <p style="font-size:.75rem;color:#bbb;">This site contains affiliate links. We earn a commission when you purchase through our links, at no extra cost to you.</p>
  </footer>
</body>
</html>"""


# =========================================================
# BLOG ENGINE
# =========================================================

BLOG_ARTICLES = [
    {"slug":"best-halloween-costumes-2026",  "title":f"Best Halloween Costumes {YEAR}",          "description":f"Top Halloween costume trends for {YEAR} — the ultimate guide.",              "merchant":"/",                              "body":f"<p>Looking for the best Halloween costumes in {YEAR}? From viral pop-culture characters to classic horror icons, this year's selection is the biggest ever. Whether you want scary, funny, sexy or group costumes, our full guide covers every trend, budget, and age group.</p>"},
    {"slug":"cheap-costumes-under-20",       "title":"Cheap Halloween Costumes Under $20",        "description":"Budget Halloween costume ideas that look great without breaking the bank.",    "merchant":"/costumes-on-sale.html", "body":"<p>You don't need to spend a fortune to have an amazing Halloween costume. We've rounded up the best cheap Halloween costumes under $20 — all available online with fast shipping. From funny one-liners to classic characters, these budget picks deliver serious impact.</p>"},
    {"slug":"kids-halloween-guide",          "title":f"Kids Halloween Costume Guide {YEAR}",      "description":f"Safe, comfortable and adorable kids Halloween costumes for {YEAR}.",         "merchant":"/kids-costumes.html",  "body":f"<p>Picking the perfect Halloween costume for your child in {YEAR}? Our kids' guide covers safety tips, sizing advice, trending characters, and the best costumes for every age — from infants and toddlers all the way up to tweens.</p>"},
    {"slug":"scary-costume-ideas",           "title":f"Scary Halloween Costume Ideas {YEAR}",     "description":f"The scariest Halloween costumes for {YEAR} — horror, gore, and creepy classics.", "merchant":"/scary-costumes.html","body":f"<p>Ready to terrify? Our scary Halloween costume roundup for {YEAR} covers the most chilling options — from classic horror movie monsters to creepy clowns, zombies, demons, and beyond. These are the costumes that will haunt the night.</p>"},
    {"slug":"couples-costumes",              "title":f"Couples Halloween Costumes {YEAR}",        "description":f"The best matching couples Halloween costumes for {YEAR}.",                    "merchant":"/couple-costume-ideas.html","body":f"<p>Halloween is more fun with a partner! Our couples costume guide for {YEAR} features the best matching sets — from classic duos and pop-culture pairs to funny couples, horror double-acts, and themed group expansions.</p>"},
]

def build_blog():
    blog_dir = os.path.join(OUTPUT_DIR, "blog")
    os.makedirs(blog_dir, exist_ok=True)

    items = "\n".join(
        f'<li><a href="{a["slug"]}.html">{a["title"]}</a> — {a["description"]}</li>'
        for a in BLOG_ARTICLES
    )
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Halloween Costume Blog | {SITE_NAME}</title>
  <meta name="description" content="Halloween costume tips, guides and ideas for {YEAR}.">
  <link rel="canonical" href="{SITE_URL}/blog/index.html">
  <style>{SHARED_CSS}</style>
</head>
<body>
  <header><h1>🎃 {SITE_NAME}</h1><p>Halloween Costume Blog</p></header>
  <main>
    <h1>Halloween Costume Blog {YEAR}</h1>
    <p>Tips, guides, and costume ideas for {YEAR}.</p>
    <ul>{items}</ul>
    <p><a href="../index.html">← Back to Main Store</a></p>
  </main>
  <footer><p>&copy; {YEAR} {OWNER} | Powered by Vulture Engine</p></footer>
</body></html>"""

    with open(os.path.join(blog_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("  ✔  blog/index.html")

    for a in BLOG_ARTICLES:
        cta_url = aff(a.get("merchant", "/"))
        post_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{a['title']} | {SITE_NAME}</title>
  <meta name="description" content="{a['description']}">
  <link rel="canonical" href="{SITE_URL}/blog/{a['slug']}.html">
  <style>{SHARED_CSS}</style>
</head>
<body>
  <header><h1>🎃 {SITE_NAME}</h1><p>The World's #1 Halloween Store</p></header>
  <main>
    <h1>{a['title']}</h1>
    {a['body']}
    <center>
      <a href="{cta_url}" class="cta-btn" target="_blank" rel="nofollow noopener">
        Shop {a['title']} ➔
      </a>
    </center>
    <p style="margin-top:2rem;"><a href="index.html">← Back to Blog</a> &nbsp;|&nbsp; <a href="../index.html">🏠 Main Store</a></p>
  </main>
  <footer>
    <p>&copy; {YEAR} {OWNER} | Powered by Vulture Engine</p>
    <p style="font-size:.75rem;color:#bbb;">Affiliate links — we earn a commission at no extra cost to you.</p>
  </footer>
</body></html>"""
        with open(os.path.join(blog_dir, f"{a['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(post_html)
        print(f"  ✔  blog/{a['slug']}.html")


# =========================================================
# SITEMAP
# =========================================================

def build_sitemap():
    urls = ""
    for page in ALL_PAGES:
        url = f"{SITE_URL}/{page['filename']}"
        priority = page.get("priority", "0.7")
        urls += f"""
  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>"""
    # blog pages
    for a in BLOG_ARTICLES:
        urls += f"""
  <url>
    <loc>{SITE_URL}/blog/{a['slug']}.html</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /
Disallow: /dist/

Sitemap: {SITE_URL}/sitemap.xml
"""


# =========================================================
# MAIN PIPELINE
# =========================================================

def build_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("🚀 Starting Vulture Engine build...\n")

    # Build SEO mesh across ALL pages
    mesh = SEOMeshEngine(ALL_PAGES)
    mesh.build_graph()

    # Primary + extra pages
    print("📄 Building pages...")
    for page in ALL_PAGES:
        mesh_links = mesh.build_mesh_for_page(page["slug"])
        html = render_page(page, mesh_links)
        path = os.path.join(OUTPUT_DIR, page["filename"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✔  {page['filename']}")

    # Blog
    print("\n📝 Building blog...")
    build_blog()

    # SEO files
    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(build_sitemap())
    print("  ✔  sitemap.xml")

    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(build_robots())
    print("  ✔  robots.txt")

    total = len(ALL_PAGES)
    print(f"\n🏁 Build complete — {total} pages + {len(BLOG_ARTICLES)} blog posts")
    print(f"   Affiliate : lc={AFFILIATE_LC} atid={AFFILIATE_ATID}")
    print(f"   Sitemap   : {total + len(BLOG_ARTICLES)} URLs indexed")


if __name__ == "__main__":
    build_all()
