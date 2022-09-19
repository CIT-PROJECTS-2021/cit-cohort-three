# Bulk file rename tool

import os
import sys
import argparse
import re

def main():
    parser = argparse.ArgumentParser(description="Bulk file rename tool")
    parser.add_argument("path", help="Path to directory")
    parser.add_argument("pattern", help="Pattern to match")
    parser.add_argument("replacement", help="Replacement string")
    args = parser.parse_args()
    path = args.path
    pattern = args.pattern
    replacement = args.replacement
    if not os.path.isdir(path):
        print("Path is not a directory")
        sys.exit(1)
    for file in os.listdir(path):
        if re.search(pattern, file):
            new_file = re.sub(pattern, replacement, file)
            os.rename(os.path.join(path, file), os.path.join(path, new_file))

if __name__ == "__main__":
    main()

# usage: app.py [-h] path pattern replacement
# eg: app.py . ".*\.txt" ".bak"