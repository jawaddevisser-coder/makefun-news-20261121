#!/usr/bin/env python3
"""Copy the pre-rendered entry image to the output directory.

Standard library only, no network, deterministic: the output bytes are
exactly the bytes of entry.png shipped in this repository.
"""
import os
import shutil
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
