# news-image-01 — round 3: "The Table"

One image summing up the world news of Friday 13 November 2026.

## The idea

One frame, one table. A forced-perspective conference table runs
diagonally from the bottom-left foreground to the top-right
background, and the day's five stories sit on it or just off it:

| Where | Story |
|---|---|
| Far end | Ukraine peace talks — two delegations, UA + EU flags |
| Mid-table | 4 tankers attacked in the Strait of Hormuz (model + seal) |
| Centre | Microsoft 365 global outage — cracked blue tablet, long shadow |
| Near edge | DOJ seizure of $1.2B in crypto — ticker tape, big orange type |
| Floor | Brooklyn building collapse, 8 dead — chalk outline + marker 8 |

The masthead dates it: "FRIDAY, 13 NOVEMBER 2026".

## Why one frame, not a grid

Round 2 was an 8-panel grid. The grid shrank every story to
postage-stamp size and read as generic infographic filler. One table
forces a single composition: the eye travels the table from the
delegations at the far end to the chalk outline at the near end, and
each story is an object, not a cell.

## How the image was made

Flat vector art drawn programmatically with Pillow
(`../news-image-v3-work/draw_v3.py`, not part of this entry):
charcoal, safety orange, off-white, one blue, one yellow accent;
hard shadows, no gradients. Every word is real text rendered by the
script, so no caption can come out garbled. Two facts were checked
against the 13 Nov news brief before drawing: the Brooklyn deaths
were a building collapse, not a shooting; the tankers were attacked
in the Strait of Hormuz.

## The program

`main.py` (Python 3.13, standard library only) copies
`assets/entry.png` (1024x1024, 70,592 bytes) verbatim to
`$MAKEFUN_OUTPUT_DIR/entry.png`. It validates the PNG first (magic,
IHDR dimensions, trailing IEND chunk, size limits) and re-reads what
it wrote to compare hashes, so two runs are byte-identical.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
