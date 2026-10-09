"""
dirstats.py – simple CLI to report directory statistics.
Usage: python dirstats.py [path]
Defaults to current directory.
"""

import os
import argparse
import sys

def stats(path):
    total_files, total_size, largest = 0, 0, None
    for root, _, files in os.walk(path):
        for f in files:
            full = os.path.join(root, f)
            try:
                sz = os.path.getsize(full)
            except OSError:
                sz = 0
            total_files += 1
            total_size += sz
            if not largest or sz > largest[1]:
                largest = (full, sz)
    return total_files, total_size, largest

def main():
    parser = argparse.ArgumentParser(description="Directory statistics")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan")
    args = parser.parse_args()
    if not os.path.isdir(args.path):
        sys.exit(f"Error: {args.path!r} is not a directory.")
    files, size, largest = stats(args.path)
    print(f"Files scanned: {files}")
    print(f"Total size : {size:,} bytes")
    if largest:
        print(f"Largest file: {largest[0]} ({largest[1]:,} bytes)")

if __name__ == "__main__":
    main()