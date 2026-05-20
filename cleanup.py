import urllib.request, urllib.error, json

TOKEN = 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
OWNER = "brightlane"
REPO  = "Costumes-Halloween-Wizard"

def api(method, path, data=None):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        data=json.dumps(data).encode() if data else None,
        headers={"Authorization":f"token {TOKEN}","Accept":"application/vnd.github+json"},
        method=method
    )
    try:
        with urllib.request.urlopen(req) as r: return json.loads(r.read())
    except: return None

files = api("GET", f"/repos/{OWNER}/{REPO}/contents/")
html  = [f for f in files if f["name"].endswith(".html")]
print(f"Deleting {len(html)} files...")
for f in html:
    ok = api("DELETE", f"/repos/{OWNER}/{REPO}/contents/{f['name']}", {"message":f"remove {f['name']}","sha":f["sha"],"branch":"main"})
    print(f"  {'✔' if ok else '❌'}  {f['name']}")
print("Done! Now run the Action manually.")
