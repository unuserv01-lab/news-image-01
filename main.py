# SPDX-License-Identifier: MIT
"""news-image-01 entry: "13 November 2026 in one image".

Writes a single editorial collage summarising the world news of
13 November 2026 to /output/entry.png.

The image is held in the repo as assets/entry.png (a 976x976 PNG,
1,018,800 bytes) and is copied verbatim to the output path, so the
program is fully deterministic: two runs produce byte-identical output.

Standard library only. No network, no randomness, no timestamps.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1 * 1024 * 1024          # competition limit: <= 1 MiB
MAX_DIMENSION = 1024                # competition limit: <= 1024x1024
OUTPUT_PATH = "/output/entry.png"

SOURCE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "assets", "entry.png")


def read_png_dimensions(path):
    """Return (width, height) from a PNG file's IHDR chunk."""
    with open(path, "rb") as fh:
        header = fh.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file: %s" % path)
    if header[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk: %s" % path)
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def main():
    with open(SOURCE_PATH, "rb") as fh:
        data = fh.read()

    if len(data) > MAX_BYTES:
        raise ValueError("image is %d bytes, over the 1 MiB limit"
                         % len(data))

    width, height = read_png_dimensions(SOURCE_PATH)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError("image is %dx%d, over the 1024x1024 limit"
                         % (width, height))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)

    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (OUTPUT_PATH, width, height, len(data), sha256_hex(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
