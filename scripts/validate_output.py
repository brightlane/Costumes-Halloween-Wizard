import os
import sys

OUTPUT_DIR = "dist"

# =========================================================
# REQUIRED CORE FILES
# =========================================================

REQUIRED_FILES = [
    "index.html",
    "sitemap.xml",
    "robots.txt"
]

# =========================================================
# REQUIRED DIRECTORIES
# =========================================================

REQUIRED_DIRS = [
    OUTPUT_DIR,
    f"{OUTPUT_DIR}/blog"
]

# =========================================================
# VALIDATION HELPERS
# =========================================================

def check_dirs():
    print("📁 Checking output directories...")

    for d in REQUIRED_DIRS:
        if not os.path.isdir(d):
            print(f"❌ Missing directory: {d}")
            sys.exit(1)
        print(f"✔ OK: {d}")

def check_files():
    print("📄 Checking required files...")

    for f in REQUIRED_FILES:
        path = os.path.join(OUTPUT_DIR, f)

        if not os.path.exists(path):
            print(f"❌ Missing file: {path}")
            sys.exit(1)

        # extra safety: file not empty
        if os.path.getsize(path) == 0:
            print(f"❌ Empty file detected: {path}")
            sys.exit(1)

        print(f"✔ OK: {path}")

def check_blog_output():
    print("📝 Checking blog output...")

    blog_path = os.path.join(OUTPUT_DIR, "blog")

    if not os.path.isdir(blog_path):
        print("❌ Blog directory missing")
        sys.exit(1)

    files = os.listdir(blog_path)

    if len(files) < 2:
        print("❌ Blog output suspicious (too few files)")
        sys.exit(1)

    print(f"✔ Blog files generated: {len(files)}")

def check_html_quality():
    print("🔍 Basic HTML sanity check...")

    index_path = os.path.join(OUTPUT_DIR, "index.html")

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    required_markers = ["<html", "<head", "<body"]

    for marker in required_markers:
        if marker not in content.lower():
            print(f"❌ Missing HTML structure: {marker}")
            sys.exit(1)

    print("✔ HTML structure OK")

# =========================================================
# MAIN
# =========================================================

def run_validation():
    print("\n🚀 Running output validation...\n")

    check_dirs()
    check_files()
    check_blog_output()
    check_html_quality()

    print("\n✅ All output validation checks passed\n")

# =========================================================
# ENTRY
# =========================================================

if __name__ == "__main__":
    run_validation()
