#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════
  HALLOWEENCOSTUMES 2026 — ULTIMATE SITE GENERATOR
  by Benny "Palmo Kid" Palmarino | LinkConnector ID 7949

  Run:  python3 build.py

  Generates 25+ pages covering EVERY category on
  halloweencostumes.com — plus categories they DON'T have.
  Goal: #1 Halloween affiliate site in the world.
═══════════════════════════════════════════════════════════
"""

import os
import json
from datetime import date
from urllib.parse import quote

# ─────────────────────────────────────────────────────────
# CONFIG (UPDATED WITH NEW AFFILIATE CREDENTIALS)
# ─────────────────────────────────────────────────────────
SITE_URL       = "https://brightlane.github.io/HalloweenCostumes"
AFF_BASE       = "https://www.linkconnector.com/ta.php?lc=007949060109004909&atid=WebCostume"
OWNER          = 'Benny "Palmo Kid" Palmarino'
LC_ID          = "7949"
TODAY          = date.today().isoformat()
OUTPUT_DIR     = "."
GOOGLE_VERIFY  = "eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"
SHIP_COUNTRIES = "200+"

# ─────────────────────────────────────────────────────────
# AFFILIATE LINK BUILDER
# ─────────────────────────────────────────────────────────
CAT_URLS = {
    "home":             "https://www.halloweencostumes.com/",
    "womens":           "https://www.halloweencostumes.com/womens-halloween-costumes.html",
    "mens":             "https://www.halloweencostumes.com/mens-halloween-costumes.html",
    "girls":            "https://www.halloweencostumes.com/girls-halloween-costumes.html",
    "boys":             "https://www.halloweencostumes.com/boys-halloween-costumes.html",
    "kids":             "https://www.halloweencostumes.com/kids-halloween-costumes.html",
    "teen":             "https://www.halloweencostumes.com/teen-halloween-costumes.html",
    "toddler":          "https://www.halloweencostumes.com/toddler-halloween-costumes.html",
    "baby":             "https://www.halloweencostumes.com/baby-halloween-costumes.html",
    "adult":            "https://www.halloweencostumes.com/adult-halloween-costumes.html",
    "scary":            "https://www.halloweencostumes.com/scary-halloween-costumes.html",
    "funny":            "https://www.halloweencostumes.com/funny-halloween-costumes.html",
    "sexy":             "https://www.halloweencostumes.com/sexy-halloween-costumes.html",
    "couples":          "https://www.halloweencostumes.com/couples-halloween-costumes.html",
    "group":            "https://www.halloweencostumes.com/group-halloween-costumes.html",
    "new2026":          "https://www.halloweencostumes.com/new-halloween-costumes.html",
    "plussize":         "https://www.halloweencostumes.com/plus-size-halloween-costumes.html",
    "wholesale":        "https://www.halloweencostumes.com/wholesale-halloween-costumes.html",
    "pet":              "https://www.halloweencostumes.com/pet-halloween-costumes.html",
    "accessories":      "https://www.halloweencostumes.com/halloween-costume-accessories.html",
    "wigs":             "https://www.halloweencostumes.com/halloween-wigs.html",
    "masks":            "https://www.halloweencostumes.com/halloween-masks.html",
    "decorations":      "https://www.halloweencostumes.com/halloween-decorations.html",
    "sale":             "https://www.halloweencostumes.com/sale-halloween-costumes.html",
    "lastminute":       "https://www.halloweencostumes.com/last-minute-halloween-costumes.html",
    "animatronics":     "https://www.halloweencostumes.com/halloween-animatronics.html",
    "props":            "https://www.halloweencostumes.com/halloween-props.html",
    "indoordecor":      "https://www.halloweencostumes.com/indoor-halloween-decorations.html",
    "outdoordecor":     "https://www.halloweencostumes.com/outdoor-halloween-decorations.html",
    "licensed":         "https://www.halloweencostumes.com/officially-licensed-halloween-costumes.html",
    "inflatable":       "https://www.halloweencostumes.com/inflatable-halloween-costumes.html",
    "collectibles":     "https://www.halloweencostumes.com/halloween-collectibles.html",
    "tween":            "https://www.halloweencostumes.com/tween-halloween-costumes.html",
    "medieval":         "https://www.halloweencostumes.com/renaissance-medieval-costumes.html",
    "videogame":        "https://www.halloweencostumes.com/video-game-costumes.html",
    "themes":           "https://www.halloweencostumes.com/halloween-costume-themes.html",
    "comiccon":         "https://www.halloweencostumes.com/superhero-costumes.html",
    "sizeguide":        "https://www.halloweencostumes.com/size-charts.html",
    "couples2":         "https://www.halloweencostumes.com/couples-halloween-costumes.html",
    "celebrations":     "https://www.halloweencostumes.com/",
    "addamsfamily":     "https://www.halloweencostumes.com/search?q=addams+family+costume",
    "beetlejuice":      "https://www.halloweencostumes.com/search?q=beetlejuice+costume",
    "horror":           "https://www.halloweencostumes.com/scary-halloween-costumes.html",
    "fnaf":             "https://www.halloweencostumes.com/search?q=five+nights+at+freddys+costume",
    "scooby":           "https://www.halloweencostumes.com/search?q=scooby+doo+costume",
    "harrypotter":      "https://www.halloweencostumes.com/search?q=harry+potter+costume",
    "decades":          "https://www.halloweencostumes.com/search?q=decade+costumes",
    "occupation":       "https://www.halloweencostumes.com/search?q=occupation+career+costumes",
    "fantasy":          "https://www.halloweencostumes.com/search?q=fantasy+fairy+angel+costume",
    "partysupplies":    "https://www.halloweencostumes.com/halloween-decorations.html",
    "diy":              "https://www.halloweencostumes.com/halloween-costume-accessories.html",
    "kpop":             "https://www.halloweencostumes.com/search?q=kpop+costume",
    "anime":            "https://www.halloweencostumes.com/search?q=anime+costume",
    "gamer":            "https://www.halloweencostumes.com/search?q=gamer+gaming+costume",
    "gifts":            "https://www.halloweencostumes.com/",
    "movies":           "https://www.halloweencostumes.com/search?q=movie+character+costume",
    "tvshows":          "https://www.halloweencostumes.com/search?q=tv+show+costume",
    "clothing":         "https://www.halloweencostumes.com/halloween-costume-accessories.html",
    "yearround":        "https://www.halloweencostumes.com/",
    "genshin":          "https://www.halloweencostumes.com/search?q=genshin+impact+costume",
    "leagueoflegends":  "https://www.halloweencostumes.com/search?q=league+of+legends+costume",
    "overwatch":        "https://www.halloweencostumes.com/search?q=overwatch+costume",
    "finalfantasy":     "https://www.halloweencostumes.com/search?q=final+fantasy+costume",
    "deadbydaylight":   "https://www.halloweencostumes.com/search?q=dead+by+daylight+costume",
    "jujutsukaisen":    "https://www.halloweencostumes.com/search?q=jujutsu+kaisen+costume",
    "hazbinhotel":      "https://www.halloweencostumes.com/search?q=hazbin+hotel+costume",
    "frieren":          "https://www.halloweencostumes.com/search?q=frieren+costume",
    "onepiececosplay":  "https://www.halloweencostumes.com/search?q=one+piece+costume",
    "cosplayshoes":     "https://www.halloweencostumes.com/search?q=costume+shoes+boots",
    "convention":       "https://www.halloweencostumes.com/search?q=convention+cosplay+costume",
    "lolita":           "https://www.halloweencostumes.com/search?q=lolita+costume",
    "swimwear":         "https://www.halloweencostumes.com/search?q=costume+swimsuit",
    "kawaii":           "https://www.halloweencostumes.com/search?q=kawaii+costume",
    "casualwear":       "https://www.halloweencostumes.com/search?q=anime+casual+wear+costume",
    "nier":             "https://www.halloweencostumes.com/search?q=nier+automata+costume",
    "cyberpunk":        "https://www.halloweencostumes.com/search?q=cyberpunk+costume",
    "zelda":            "https://www.halloweencostumes.com/search?q=legend+of+zelda+costume",
    "devilmaycry":      "https://www.halloweencostumes.com/search?q=devil+may+cry+costume",
    "weeklydeals":      "https://www.halloweencostumes.com/sale-halloween-costumes.html",
    "preorder":         "https://www.halloweencostumes.com/new-halloween-costumes.html",
    "morphsuits":       "https://www.halloweencostumes.com/search?q=morphsuit+full+body+costume",
    "piggyback":        "https://www.halloweencostumes.com/search?q=piggyback+costume",
    "digital":          "https://www.halloweencostumes.com/search?q=tech+animated+costume",
    "fullbody":         "https://www.halloweencostumes.com/search?q=full+body+costume+zentai",
    "halloweenfashion": "https://www.halloweencostumes.com/search?q=halloween+fashion+clothing",
    "halloweenpajamas": "https://www.halloweencostumes.com/search?q=halloween+pajamas+sleepwear",
    "matchingfamily":   "https://www.halloweencostumes.com/search?q=matching+family+halloween+costume",
    "halloweensweaters":"https://www.halloweencostumes.com/search?q=halloween+sweater+costume",
    "halloweendresses": "https://www.halloweencostumes.com/search?q=halloween+dress+costume",
    "makeup":           "https://www.halloweencostumes.com/halloween-makeup.html",
    "trickortreat":     "https://www.halloweencostumes.com/halloween-costume-accessories.html",
    "hauntedhouse":     "https://www.halloweencostumes.com/halloween-decorations.html",
    "pumpkin":          "https://www.halloweencostumes.com/halloween-decorations.html",
    "lighting":         "https://www.halloweencostumes.com/search?q=halloween+lighting+string+lights",
    "sizecharts":       "https://www.halloweencostumes.com/size-charts.html",
    "budget":           "https://www.halloweencostumes.com/sale-halloween-costumes.html",
    "clearance":        "https://www.halloweencostumes.com/sale-halloween-costumes.html",
    "princess":         "https://www.halloweencostumes.com/search?q=princess+costume",
    "mermaid":          "https://www.halloweencostumes.com/search?q=mermaid+costume",
    "steampunk":        "https://www.halloweencostumes.com/search?q=steampunk+costume",
    "masquerade":       "https://www.halloweencostumes.com/search?q=masquerade+costume",
    "food":             "https://www.halloweencostumes.com/search?q=food+costume+funny",
    "cheerleader":      "https://www.halloweencostumes.com/search?q=cheerleader+costume",
    "cowgirl":          "https://www.halloweencostumes.com/search?q=cowgirl+western+costume",
    "bestsellers":      "https://www.halloweencostumes.com/",
    "animals":          "https://www.halloweencostumes.com/search?q=animal+costume",
    "dragon":           "https://www.halloweencostumes.com/search?q=dragon+costume",
    "glowinthedark":    "https://www.halloweencostumes.com/search?q=glow+in+the+dark+costume",
    "skeletons":        "https://www.halloweencostumes.com/search?q=skeleton+decoration",
    "spiderwebs":       "https://www.halloweencostumes.com/search?q=spider+web+halloween+decoration",
    "tombstones":       "https://www.halloweencostumes.com/search?q=tombstone+graveyard+halloween",
    "candy":            "https://www.halloweencostumes.com/search?q=halloween+candy+treat",
    "trunkortreat":     "https://www.halloweencostumes.com/search?q=trunk+or+treat+halloween",
    "gnomes":           "https://www.halloweencostumes.com/search?q=halloween+gnome",
    "nightmarebc":      "https://www.halloweencostumes.com/search?q=nightmare+before+christmas+costume",
    "hocuspocus":       "https://www.halloweencostumes.com/search?q=hocus+pocus+costume",
    "murdermystery":    "https://www.halloweencostumes.com/search?q=murder+mystery+halloween",
    "sustainable":      "https://www.halloweencostumes.com/search?q=sustainable+eco+halloween+costume",
    "plusSizeCosplay":  "https://www.halloweencostumes.com/search?q=plus+size+cosplay+costume",
    "renfaire":         "https://www.halloweencostumes.com/search?q=renaissance+faire+costume",
    "gothic":           "https://www.halloweencostumes.com/search?q=gothic+dark+aesthetic+costume",
    "carnival":         "https://www.halloweencostumes.com/search?q=carnival+mardi+gras+costume",
    "larp":             "https://www.halloweencostumes.com/search?q=larp+roleplay+costume",
    "cosplaywigs":      "https://www.halloweencostumes.com/halloween-wigs.html",
    "witchaesthetic":   "https://www.halloweencostumes.com/search?q=witch+aesthetic+costume",
    "adaptive":         "https://www.halloweencostumes.com/search?q=wheelchair+adaptive+halloween+costume",
    "celebrity":        "https://www.halloweencostumes.com/search?q=celebrity+costume+2026",
    "friendscostume":   "https://www.halloweencostumes.com/search?q=best+friends+group+costume",
    "officecostume":    "https://www.halloweencostumes.com/search?q=office+appropriate+halloween+costume",
    "racer":            "https://www.halloweencostumes.com/search?q=race+car+driver+costume",
    "creepydoll":       "https://www.halloweencostumes.com/search?q=doll+puppet+creepy+costume",
    "occult":           "https://www.halloweencostumes.com/search?q=occult+supernatural+costume",
    "musicartist":      "https://www.halloweencostumes.com/search?q=music+artist+costume+2026",
    "horrornight":      "https://www.halloweencostumes.com/search?q=horror+night+costume",
    "wizard":           "https://www.halloweencostumes.com/search?q=wizard+costume"
}

def aff(cat_key=None, search=None):
    if cat_key and cat_key in CAT_URLS:
        dest = CAT_URLS[cat_key]
    elif search:
        dest = f"https://www.halloweencostumes.com/search?q={search.replace(' ','+')}"
    else:
        return AFF_BASE
    return f"{AFF_BASE}&url={quote(dest, safe='')}"

# ─────────────────────────────────────────────────────────
# PAGES DEFINITION (UPDATED WITH DISTINCT SEO FILENAMES)
# ─────────────────────────────────────────────────────────
PAGES = {
    "index": {
        "file":"index.html","cat_key":"home","icon":"🎃",
        "group":"main","nav_group":"shop",
        "en_title":"Halloween Costumes 2026 | #1 Store Worldwide",
        "en_desc":"Halloween costumes 2026 — the world's best deals. Kids, adults, scary, funny, sexy, couples, group, wholesale, pet, accessories and decorations. Ships to 200+ countries.",
        "en_h1":"Halloween Costumes 2026",
        "en_h1sub":"The World's #1 Halloween Store",
        "en_body":"Welcome to the world's #1 Halloween costume destination for 2026. We feature the largest selection of Halloween costumes on the internet — thousands of styles for kids, adults, teens, toddlers, babies, couples, groups, and pets. From cheap Halloween costumes under $10 to premium exclusive designs, our selection beats every other Halloween store online. Updated daily with new arrivals, sales, and exclusive deals. Ships to 200+ countries worldwide.",
        "schema_type":"WebSite",
        "keywords":"halloween costumes 2026, best halloween costumes, halloween costume store",
    },
    "womens": {
        "file":"womens-costumes-2026.html","cat_key":"womens","icon":"👩",
        "group":"gender","nav_group":"gender",
        "en_title":"Women's Halloween Costumes 2026 | Best Deals",
        "en_desc":"Women's Halloween costumes 2026 — hundreds of styles for women. Classic, scary, funny, sexy and plus size. Ships to 200+ countries.",
        "en_h1":"Women's Halloween Costumes 2026",
        "en_h1sub":"Hundreds of Styles for Women",
        "en_body":"Find the perfect women's Halloween costume 2026 from hundreds of styles. Our women's costume collection covers every theme — classic horror, pop culture icons, funny food costumes, sexy Halloween looks, renaissance and historical costumes, and more. Available in standard and plus sizes, with new styles added daily. Whether you want to be a witch, vampire, superhero, or pop culture queen — we have the best women's Halloween costumes at unbeatable prices.",
        "schema_type":"CollectionPage",
        "keywords":"womens halloween costumes, women halloween costumes 2026, ladies halloween costumes",
    },
    "mens": {
        "file":"mens-costumes-online.html","cat_key":"mens","icon":"👨",
        "group":"gender","nav_group":"gender",
        "en_title":"Men's Halloween Costumes 2026 | Best Deals",
        "en_desc":"Men's Halloween costumes 2026 — hundreds of styles for men. Scary, funny, classic and pop culture. Ships to 200+ countries.",
        "en_h1":"Men's Halloween Costumes 2026",
        "en_h1sub":"Scary, Funny & Classic Styles for Men",
        "en_body":"Shop the best men's Halloween costumes 2026. Our men's costume collection includes classic monsters, superheroes, movie villains, funny characters, historical figures, and pop culture icons. Available in all sizes including big and tall. Whether you want a terrifying scary costume or a hilarious outfit that wins the costume contest — our men's Halloween costumes have you covered. New styles added daily with unbeatable prices.",
        "schema_type":"CollectionPage",
        "keywords":"mens halloween costumes, men halloween costumes 2026, male halloween costumes",
    },
    "girls": {
        "file":"girls-costumes-and-dresses.html","cat_key":"girls","icon":"👧",
        "group":"gender","nav_group":"gender",
        "en_title":"Girls' Halloween Costumes 2026 | Princess, Witch, Animal & More",
        "en_desc":"Girls' Halloween costumes 2026 — princess dress-up sets, witch costumes, animal onesies, superhero capes and more. Sizes 2T to 14. From $15. Ships to 200+ countries.",
        "en_h1":"Girls' Halloween Costumes 2026",
        "en_h1sub":"Princess Sets, Witches, Animals & Superheroes — From $15",
        "en_body":"Find the perfect girls' Halloween costume for 2026 — our girls' costume collection is the largest online, covering every category girls love. Disney princess costumes featuring Elsa, Anna, Cinderella, Belle, Aurora, Ariel, Rapunzel, Moana, and Tiana. Light-up LED princess gowns that glow and twinkle all night. Princess dress-up multi-packs with 5-8 different character gowns and accessories in one box — perfect for girls who want to be a different princess every day. Witch costumes in every style from cute to scary. Animal onesie costumes in bee, unicorn, cat, dinosaur, and dozens more adorable creatures. Superhero costumes featuring Wonder Woman, Supergirl, and Black Widow. Mermaid costumes, fairy costumes, and dance recital-style costume sets. Each costume ships complete with accessories — tiaras, wands, earrings, gloves, and character-specific props. Available in sizes 2T through 14 (and adult sizes too). Girls' costumes from just $15. Perfect for Halloween, birthday parties, dress-up play, and school events. Ships to 200+ countries.",
        "schema_type":"CollectionPage",
        "keywords":"girls halloween costumes 2026, halloween costumes for girls, princess costume girls, elsa costume, disney princess halloween costume, girls costume set, light up princess dress, multi pack princess dress",
    },
    "boys": {
        "file":"boys-superhero-ninja-costumes.html","cat_key":"boys","icon":"👦",
        "group":"gender","nav_group":"gender",
        "en_title":"Boys' Halloween Costumes 2026 | Best Deals for Boys",
        "en_desc":"Boys' Halloween costumes 2026 — superheroes, monsters, ninjas, pirates and more. All sizes from toddler to teen. Ships to 200+ countries.",
        "en_h1":"Boys' Halloween Costumes 2026",
        "en_h1sub":"Superheroes, Monsters, Ninjas & Pirates",
        "en_body":"Shop the coolest boys' Halloween costumes 2026 — superheroes, scary monsters, ninjas, pirates, dinosaurs, Star Wars characters, video game icons and more. Our boys' costume collection covers all ages and sizes from infant to teen. Whether your boy wants to be a terrifying zombie or his favorite movie hero — we have the best boys' Halloween costumes at prices every parent loves.",
        "schema_type":"CollectionPage",
        "keywords":"boys halloween costumes, halloween costumes for boys 2026, boy costumes",
    },
    "kids": {
        "file":"kids-halloween-outfits.html","cat_key":"kids","icon":"👶",
        "group":"age","nav_group":"age",
        "en_title":"Kids Halloween Costumes 2026 | Best Deals for Children",
        "en_desc":"Kids Halloween costumes 2026 — superheroes, witches, animals, princesses and more. Sizes for all ages. Ships to 200+ countries.",
        "en_h1":"Kids Halloween Costumes 2026",
        "en_h1sub":"Superheroes, Witches, Animals & More",
        "en_body":"Find the best kids Halloween costumes 2026 for boys and girls of all ages. Our kids costume selection includes superheroes, witches, animals, princesses, scary monsters, funny characters and classic Halloween costumes. We carry kids sizes from toddler and infant all the way to teen, with prices starting from just $10. Perfect for trick-or-treating, school Halloween parties, and family events. All kids costumes ship worldwide with fast delivery.",
        "schema_type":"CollectionPage",
        "keywords":"kids halloween costumes, children halloween costumes 2026, halloween costumes for kids",
    },
    "teen": {
        "file":"cool-teen-costumes.html","cat_key":"teen","icon":"🧑",
        "group":"age","nav_group":"age",
        "en_title":"Teen Halloween Costumes 2026 | Cool Costumes for Teenagers",
        "en_desc":"Teen Halloween costumes 2026 — cool, scary and funny costumes for teenagers. Pop culture, horror and trendy styles. Ships to 200+ countries.",
        "en_h1":"Teen Halloween Costumes 2026",
        "en_h1sub":"Cool, Scary & Trendy Costumes for Teens",
        "en_body":"Find the coolest teen Halloween costumes 2026 — styles that teenagers actually want to wear. Our teen costume collection includes the latest pop culture characters, trendy horror looks, funny meme-worthy outfits, and classic Halloween styles updated for 2026. Teen sizes available for both girls and boys. Stand out at the Halloween party with a teen costume that's cool enough to impress your friends.",
        "schema_type":"CollectionPage",
        "keywords":"teen halloween costumes, teenager halloween costumes 2026, halloween costumes for teens",
    },
    "toddler": {
        "file":"cute-toddler-costumes.html","cat_key":"toddler","icon":"🍼",
        "group":"age","nav_group":"age",
        "en_title":"Toddler Halloween Costumes 2026 | Adorable Kids Costumes",
        "en_desc":"Toddler Halloween costumes 2026 — adorable and comfortable costumes for toddlers ages 1-4. Animals, superheroes, princesses and more.",
        "en_h1":"Toddler Halloween Costumes 2026",
        "en_h1sub":"Adorable Costumes for Little Ones Ages 1-4",
        "en_body":"Dress your toddler in the cutest Halloween costume 2026 — adorable animal costumes, tiny superhero suits, little witch outfits, and classic Halloween characters scaled down for the littlest trick-or-treaters. Our toddler costumes are designed to be comfortable, easy to put on, and sized perfectly for ages 1-4. Safe materials, vibrant colors, and styles so cute you'll want to photograph every moment. Toddler Halloween costumes from just $10.",
        "schema_type":"CollectionPage",
        "keywords":"toddler halloween costumes, halloween costumes for toddlers 2026, toddler costumes",
    },
    "baby": {
        "file":"infant-baby-costumes.html","cat_key":"baby","icon":"👼",
        "group":"age","nav_group":"age",
        "en_title":"Baby Halloween Costumes 2026 | Cutest Infant Costumes",
        "en_desc":"Baby Halloween costumes 2026 — the cutest infant and newborn Halloween costumes. Comfortable, safe and adorable. Ships to 200+ countries.",
        "en_h1":"Baby Halloween Costumes 2026",
        "en_h1sub":"The Cutest Infant & Newborn Halloween Costumes",
        "en_body":"Make your baby's first Halloween unforgettable with our adorable baby Halloween costumes 2026. From tiny pumpkin suits to mini superhero capes, cute animal onesies and classic Halloween characters — our baby costume collection is designed for maximum cuteness and comfort. Safe, soft materials suitable for newborns and infants up to 24 months. These baby Halloween costumes are perfect for trick-or-treating, family photos and Halloween parties.",
        "schema_type":"CollectionPage",
        "keywords":"baby halloween costumes, infant halloween costumes 2026, newborn halloween costumes",
    },
    "adult": {
        "file":"adult-costumes-apparel.html","cat_key":"adult","icon":"🎭",
        "group":"type","nav_group":"type",
        "en_title":"Adult Halloween Costumes 2026 | Best Deals for Men & Women",
        "en_desc":"Adult Halloween costumes 2026 — classic horror, pop culture, funny, scary and couples costumes. All sizes. Ships to 200+ countries.",
        "en_h1":"Adult Halloween Costumes 2026",
        "en_h1sub":"Classic Horror, Pop Culture & Original Designs",
        "en_body":"Discover the best adult Halloween costumes 2026 for men and women. Our adult costume collection includes classic horror characters, pop culture icons, funny costumes, scary monsters, couples costumes, and original designs. Available in all sizes from XS to plus size, with styles ranging from traditional Halloween to movie-inspired looks. Perfect for Halloween parties, haunted houses, and costume contests. All adult Halloween costumes ship worldwide.",
        "schema_type":"CollectionPage",
        "keywords":"adult halloween costumes, halloween costumes for adults 2026, adult costumes",
    },
    "scary": {
        "file":"scary-horror-costumes.html","cat_key":"scary","icon":"💀",
        "group":"type","nav_group":"type",
        "en_title":"Scary Halloween Costumes 2026 | Horror & Monster Costumes",
        "en_desc":"Scary Halloween costumes 2026 — terrifying monsters, zombies, vampires, clowns and haunted house looks. Ships to 200+ countries.",
        "en_h1":"Scary Halloween Costumes 2026",
        "en_h1sub":"Monsters, Zombies & Haunted House Looks",
        "en_body":"Shop the scariest Halloween costumes 2026 — guaranteed to terrify. Our scary costume collection includes classic horror monsters, zombies, vampires, werewolves, scary clowns, mummies, skeletons, demons and haunted house characters. Perfect for Halloween parties, haunted attractions, and anyone who wants to make a truly frightening impression. Scary Halloween costumes available in all sizes for kids, adults and plus size. Ships worldwide.",
        "schema_type":"CollectionPage",
        "keywords":"scary halloween costumes, horror halloween costumes 2026, terrifying costumes",
    },
    "funny": {
        "file":"funny-novelty-costumes.html","cat_key":"funny","icon":"😂",
        "group":"type","nav_group":"type",
        "en_title":"Funny Halloween Costumes 2026 | Hilarious Costume Ideas",
        "en_desc":"Funny Halloween costumes 2026 — hilarious outfits for adults, kids and groups. Win every costume contest. Ships to 200+ countries.",
        "en_h1":"Funny Halloween Costumes 2026",
        "en_h1sub":"Hilarious Outfits That Win Every Contest",
        "en_body":"Find the funniest Halloween costumes 2026 that are guaranteed to make everyone laugh. Our funny costume collection includes hilarious food costumes, pop culture parodies, punny outfits, inflatable costumes, and novelty character looks. Perfect for Halloween parties, office costume contests, and anyone who prefers laughs over scares. Funny Halloween costumes available for adults, kids, couples, and groups. Ships worldwide.",
        "schema_type":"CollectionPage",
        "keywords":"funny halloween costumes, hilarious halloween costumes 2026, humorous costumes",
    },
    "sexy": {
        "file":"sexy-adult-costumes.html","cat_key":"sexy","icon":"💋",
        "group":"type","nav_group":"type",
        "en_title":"Sexy Halloween Costumes 2026 | Best Adult Costume Deals",
        "en_desc":"Sexy Halloween costumes 2026 — stylish and alluring adult costume styles for women and men. All sizes. Ships to 200+ countries.",
        "en_h1":"Sexy Halloween Costumes 2026",
        "en_h1sub":"Stylish & Alluring Adult Halloween Styles",
        "en_body":"Find the best sexy Halloween costumes 2026 — stylish, alluring and perfectly crafted adult costume looks for Halloween parties. Our sexy costume collection includes sultry takes on classic Halloween characters, glamorous villain costumes, and chic party-ready looks for women and men. Available in all sizes with quality materials that look stunning. These sexy Halloween costumes are designed for adults who want to turn heads at every Halloween event.",
        "schema_type":"CollectionPage",
        "keywords":"sexy halloween costumes, sexy costumes 2026, adult sexy halloween costumes",
    },
    "couples": {
        "file":"matching-couples-costumes.html","cat_key":"couples","icon":"💑",
        "group":"type","nav_group":"type",
        "en_title":"Couples Halloween Costumes 2026 | Matching Costume Sets",
        "en_desc":"Couples Halloween costumes 2026 — matching costume sets for two. Classic duos, funny pairs, scary couples and pop culture sets. Ships to 200+ countries.",
        "en_h1":"Couples Halloween Costumes 2026",
        "en_h1sub":"Matching Sets for the Perfect Duo",
        "en_body":"Make Halloween twice as fun with our couples Halloween costumes 2026. We have the best matching costume sets for two — from classic duos like Bonnie & Clyde to funny food pairs, scary horror couples, pop culture icons, and Disney character sets. Our couples costumes are designed to complement each other perfectly, with coordinated styles for him and her. Perfect for Halloween parties, date nights, and every couples costume contest.",
        "schema_type":"CollectionPage",
        "keywords":"couples halloween costumes, matching halloween costumes 2026, couples costumes",
    },
    "group": {
        "file":"group-family-costumes.html","cat_key":"group","icon":"👨‍👩‍👧‍👦",
        "group":"type","nav_group":"type",
        "en_title":"Group Halloween Costumes 2026 | Family & Matching Sets",
        "en_desc":"Group Halloween costumes 2026 — matching sets for families, friends, couples and office parties. Ships to 200+ countries.",
        "en_h1":"Group Halloween Costumes 2026",
        "en_h1sub":"Matching Sets for Families, Friends & Offices",
        "en_body":"Coordinate your Halloween look with our group and family Halloween costumes 2026. We have matching costume sets for couples, families, friend groups, and office parties. Browse themed group sets from TV shows, movies, fairy tales, and classic Halloween themes. Whether you need costumes for 2 people or 20, we have complete group sets that fit seamlessly.",
        "schema_type":"CollectionPage",
        "keywords":"group halloween costumes, family costumes 2026, matching friend costumes",
    },
    "wizard": {
        "file":"mystical-wizard-robes.html","cat_key":"wizard","icon":"🧙‍♂️",
        "group":"extended","nav_group":"shop",
        "en_title":"Magical Halloween Wizard Costumes | Spellbinding Outfits",
        "en_desc":"Discover the ultimate collection of Halloween wizard costumes. From mystical robes and starry hats to enchanted accessories for kids and adults.",
        "en_h1":"Mystical Wizard Costumes",
        "en_h1sub":"Unleash the Magic This Halloween Night",
        "en_body":"Step into a realm where enchantment meets spookiness. Whether you are searching for a classic star-patterned sorcerer robe, a dark gothic battle mage outfit, or a cute magical apprentice costume for the little ones, our premium curated selection brings legendary folklore to life.",
        "schema_type":"CollectionPage",
        "keywords":"wizard costumes, halloween wizard robe, sorcerer costume 2026, kids wizard outfit",
    }
}

# Add structural entries dynamically with distinct filenames (e.g., 'jujutsukaisen' -> 'best-jujutsukaisen-costumes.html')
for key, mapping in CAT_URLS.items():
    if key not in PAGES and key != "home":
        readable = key.replace("cosplay"," Cosplay ").replace("decor"," Decor").capitalize()
        
        # Build completely distinct filename layout
        distinct_filename = f"best-{key.lower()}-costumes.html"
        
        PAGES[key] = {
            "file": distinct_filename, "cat_key": key, "icon": "🎭",
            "group": "extended", "nav_group": "shop",
            "en_title": f"{readable} Halloween Costumes & Gear 2026",
            "en_desc": f"Shop premium {readable} lines for Halloween 2026. Highest quality materials with global target delivery windows.",
            "en_h1": f"{readable} Collection 2026",
            "en_h1sub": "Beat the Competition with Exclusive Deals",
            "en_body": f"Explore our ultimate hub for premium {readable} apparel and design accessories. Tailored for absolute accuracy, maximum durability, and authentic detailing across all operational metrics."
        }
