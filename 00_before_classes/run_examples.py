"""Run all example files from the 00_before_classes folder."""

import subprocess
from pathlib import Path


def main():
    for file_path in sorted(Path("examples").glob("example_*.py")):
        print()
        print("=" * 60)
        print(file_path)
        print("=" * 60)
        subprocess.run(["python", str(file_path)], check=True)


if __name__ == "__main__":
    main()
