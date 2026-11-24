"""make.fun entry: Sum up 24 November's world news in one image.

Writes the prepared front-page image to /output/entry.png.
No network access. Deterministic: every run writes the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.png"))


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
