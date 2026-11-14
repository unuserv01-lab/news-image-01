# SPDX-License-Identifier: MIT
"""news-image-01 entry round 3: "The Table".

Writes one editorial image summing up the world news of Friday
13 November 2026 to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).

The image is "The Table": a single forced-perspective conference
table, diagonal across the frame, with the day's five stories sitting
on it or just off it -- Ukraine peace talks at the far end, four
tankers attacked in the Strait of Hormuz mid-table, the Microsoft 365
global outage as a cracked blue tablet at the centre, the DOJ's $1.2B
crypto seizure on a ticker tape along the near edge, and the Brooklyn
building collapse (8 dead) as a chalk outline on the floor. It is
drawn as flat vector art with Pillow (see README.md); the program
itself only ships the finished PNG.

The program copies assets/entry.png (a 1024x1024 PNG) verbatim to the
output path. It first checks the file is really a PNG, is within the
competition's size and dimension limits, and then re-reads what it
wrote and compares hashes, so a truncated or altered write is caught
instead of silently submitted. No network, no randomness, no clock:
two runs write byte-identical output.

Standard library only.
"""

import hashlib
import os
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576          # competition limit: at most 1 MiB
MAX_SIDE = 1024              # competition limit: at most 1024x1024


def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "assets", "entry.png")


def dest_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.png")


def validate_png(blob):
    """Check blob is a whole PNG and return its (width, height).

    Requires the magic, an IHDR chunk and a trailing IEND chunk, so a
    truncated PNG (a whole image is what the gate wants) is rejected
    here instead of at grading time. Works on the bytes already read,
    so even a 0-byte file fails cleanly with ValueError instead of a
    seek error.
    """
    if len(blob) < 45:  # magic (8) + IHDR chunk (25) + IEND chunk (12)
        raise ValueError("entry.png is %d bytes, too small to be a PNG"
                         % len(blob))
    if blob[:8] != PNG_MAGIC:
        raise ValueError("entry.png is not a PNG file")
    if blob[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    if blob[-8:-4] != b"IEND":
        raise ValueError("entry.png has no trailing IEND chunk")
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    return width, height


def sha256_hex(blob):
    return hashlib.sha256(blob).hexdigest()


def main():
    src = source_path()
    with open(src, "rb") as fh:
        blob = fh.read()
    source_hash = sha256_hex(blob)

    if len(blob) > MAX_BYTES:
        raise ValueError("entry.png is %d bytes, over the 1 MiB limit"
                         % len(blob))
    width, height = validate_png(blob)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError("entry.png is %dx%d, over the 1024x1024 limit"
                         % (width, height))

    dst = dest_path()
    parent = os.path.dirname(dst)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(dst, "wb") as fh:
        fh.write(blob)

    # Verify the write: re-read and compare hashes, so a partial
    # write can never pass as a valid entry.
    with open(dst, "rb") as fh:
        written = fh.read()
    if sha256_hex(written) != source_hash:
        raise ValueError("output %s does not match the source image" % dst)

    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (dst, width, height, len(blob), source_hash))
    return 0


if __name__ == "__main__":
    sys.exit(main())
