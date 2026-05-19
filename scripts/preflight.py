import importlib
import os
import sys

# =========================================================
# REQUIRED PYTHON MODULES
# =========================================================

REQUIRED_MODULES = [
    "jinja2",
    "os",
    "datetime",
]

# =========================================================
# REQUIRED PROJECT FILES
# =========================================================

REQUIRED_FILES = [
    "build.py",
    "requirements.txt",
    "core/renderer.py",
    "core/seo.py",
    "core/schema.py",
    "core/blog_engine.py",
]

# =========================================================
# REQUIRED DIRECTORIES
# =========================================================

REQUIRED_DIRS = [
    "core",
    "scripts",
]

# =========================================================
# CHECK FUNCTIONS
# =========================================================

def check_modules():
    print("🔍 Checking Python dependencies...")

    for module in REQUIRED_MODULES:
        try:
            importlib.import_module(module)
            print(f"✔ module OK: {module}")
        except ImportError:
            print(f"❌ missing module: {module}")
            sys.exit(1)

def check_files():
    print("📁 Checking required files...")

    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            print(f"❌ missing file: {file}")
            sys.exit(1)
        print(f"✔ file OK: {file}")

def check_dirs():
    print("📂 Checking required directories...")

    for directory in REQUIRED_DIRS:
        if not os.path.isdir(directory):
            print(f"❌ missing directory: {directory}")
            sys.exit(1)
        print(f"✔ dir OK: {directory}")

# =========================================================
# MAIN
# =========================================================

def run_preflight():
    print("\n🚀 Running preflight safety checks...\n")

    check_dirs()
    check_files()
    check_modules()

    print("\n✅ Preflight passed — build is safe to run\n")

# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    run_preflight()
