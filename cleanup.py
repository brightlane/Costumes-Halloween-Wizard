import urllib.request
import urllib.error
import json
import base64

# =========================================================
# CONFIG — fill these in
# =========================================================

GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE"   # https://github.com/settings/tokens
REPO_OWNER   = "brightlane"
REPO_NAME    = "Costumes-Halloween-Wizard"
BRANCH       = "main"

# =========================================================
# GITHUB API HELPER
# =========================================================

def api(method, path, data=None):
    url = f"https://api.github.com{path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    }
    body = json.dumps(data).encode() if data else None
    req  = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code}: {e.read().decode()}")
        return None

# =========================================================
# MAIN — delete all .html files from repo root
# =========================================================

print(f"\n🗑  Deleting root HTML files from {REPO_OWNER}/{REPO_NAME}...\n")

# Get all files in root
contents = api("GET", f"/repos/{REPO_OWNER}/{REPO_NAME}/contents/?ref={BRANCH}")
if not contents:
    print("❌ Could not fetch repo contents. Check your token.")
    exit(1)

html_files = [f for f in contents if f["name"].endswith(".html")]
print(f"Found {len(html_files)} HTML files to delete.\n")

deleted = 0
failed  = 0

for f in html_files:
    name = f["name"]
    sha  = f["sha"]
    result = api("DELETE", f"/repos/{REPO_OWNER}/{REPO_NAME}/contents/{name}", {
        "message": f"Remove old static file: {name}",
        "sha":     sha,
        "branch":  BRANCH,
    })
    if result:
        print(f"  ✔  deleted: {name}")
        deleted += 1
    else:
        print(f"  ❌ failed:  {name}")
        failed += 1

print(f"\n✅ Done — {deleted} deleted, {failed} failed.")
print("Now go to GitHub Actions and run 'Daily Programmatic Index Sync' manually.")
