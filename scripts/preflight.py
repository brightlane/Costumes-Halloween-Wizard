import importlib
import os
import sys

# =========================================================
# REQUIRED PYTHON MODULES
# =========================================================
REQUIRED_MODULES = [
    "os",
    "datetime",
    "urllib",
    "collections",
]

# =========================================================
# REQUIRED PROJECT FILES
# =========================================================
REQUIRED_FILES = [
    "build.py",
    "requirements.txt",
    "scripts/validate_output.py",
    "affiliate.json",
]

# =========================================================
# REQUIRED DIRECTORIES
# =========================================================
REQUIRED_DIRS = [
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
            print(f"  ✔ module OK: {module}")
        except ImportError:
            print(f"  ❌ missing module: {module}")
            sys.exit(1)

def check_files():
    print("📁 Checking required files...")
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            print(f"  ❌ missing file: {file}")
            sys.exit(1)
        if os.path.getsize(file) == 0:
            print(f"  ❌ empty file: {file}")
            sys.exit(1)
        print(f"  ✔ file OK: {file}")

def check_dirs():
    print("📂 Checking required directories...")
    for directory in REQUIRED_DIRS:
        if not os.path.isdir(directory):
            print(f"  ❌ missing directory: {directory}")
            sys.exit(1)
        print(f"  ✔ dir OK: {directory}")

def check_affiliate():
    print("🔗 Checking affiliate config...")
    import json
    try:
        with open("affiliate.json", "r") as f:
            data = json.load(f)
        required_keys = ["affiliate_id", "lc", "atid"]
        for key in required_keys:
            if key not in data:
                print(f"  ❌ affiliate.json missing key: {key}")
                sys.exit(1)
            print(f"  ✔ affiliate key OK: {key} = {data[key]}")
    except Exception as e:
        print(f"  ❌ affiliate.json error: {e}")
        sys.exit(1)

# =========================================================
# MAIN
# =========================================================

def run_preflight():
    print("\n🚀 Running preflight safety checks...\n")
    check_dirs()
    check_files()
    check_modules()
    check_affiliate()
    print("\n✅ Preflight passed — build is safe to run\n")

if __name__ == "__main__":
    run_preflight()
