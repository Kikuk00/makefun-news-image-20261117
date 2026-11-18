"""Copy the entry image to the output directory.

Standard library only. Reads entry.png from beside this script and writes
it to $MAKEFUN_OUTPUT_DIR/entry.png, byte for byte.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        print(f"entry image not found: {src}", file=sys.stderr)
        return 1
    dst = Path(out_dir) / "entry.png"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        print("copied file size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
