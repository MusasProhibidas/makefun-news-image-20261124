"""make.fun entry: Sum up 24 November's world news in one image.

Writes the prepared front-page image to /output/entry.png.
No network access. Deterministic: every run writes the same bytes.
After copying, the output is verified byte-for-byte against the
source (SHA-256) so a partial or corrupted write fails loudly.
"""
import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.png"))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    if _sha256(SRC) != _sha256(OUT):
        raise SystemExit("entry.png copy mismatch: output bytes differ from source")


if __name__ == "__main__":
    main()
