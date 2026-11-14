# news-image-01 entry round 2 — "13 November 2026 in One Image"

A poster (1024×1024 PNG, 79,305 bytes) summing up the world news of
Friday 13 November 2026 in 8 panels, 2 columns × 4 rows, under a navy
header "13 NOVEMBER 2026 / WORLD NEWS IN ONE IMAGE".

## How the image was made

Round 1 was a single AI-rendered image. For round 2 the poster was
redrawn as **flat vector art with a Pillow script**
(`~/workspace/makefun/news-image-v2-work/draw.py`, build artifact, not
part of this entry): every scene is drawn from shapes and every word is
real text in DejaVu Sans Bold, so no caption can come out garbled and
every factual fix below is exactly as intended. The program
(`main.py`, stdlib only, no network) copies `assets/entry.png`
byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
verifying PNG magic bytes, dimensions ≤ 1024×1024 and size ≤ 1 MiB.

## The 8 panels

1. **GULF TANKERS HIT / 4 TANKERS ATTACKED** — two tankers burning in
   the Strait of Hormuz at dusk, black smoke, orange glow on the sea.
2. **UKRAINE TALKS / EUROPE JOINS NEXT ROUND** — two delegations seated
   opposite each other at a long table with documents, Ukrainian flag on
   one side, Russian flag on the other, talking. No handshake.
3. **NVIDIA CEO OUT / HUANG RESIGNS** — a large green computer chip on
   a desk beside an empty CEO office chair.
4. **MICROSOFT 365 DOWN / GLOBAL OUTAGE** — laptop and phone screens
   with red error crosses under a dark storm cloud with lightning, a
   disconnected plug and socket, servers with red lights.
5. **SENATE SHOWDOWN / VAN HOLLEN v SCHUMER** — two senators arguing
   face to face in front of the US Capitol dome.
6. **BROOKLYN COLLAPSE / 8 DEAD** — a collapsed brick apartment
   building with a jagged broken edge, rubble, rescue workers in orange
   vests and yellow helmets.
7. **$1.2B CRYPTO SEIZED / DOJ SEIZES HACK FUNDS** — a large golden
   Bitcoin coin with handcuffs in front of a courthouse.
8. **POPE IN PERU / MEETS ABUSE VICTIMS** — the Pope in white waving
   to a crowd in a colourful Peruvian street, Peruvian flags.

## What changed from round 1

- **Ukraine:** round 1 showed a handshake, implying a deal was done.
  Round 2 shows the delegations seated across the table in discussion,
  hands on the table apart — talks ongoing, no deal (per the brief:
  Russia agreed Europe joins the *next* round).
- **Brooklyn:** round 1 showed only rubble. Round 2 puts **"8 DEAD"**
  in the gold subline, so the death toll reads at a glance.
- **Microsoft:** round 1 was only a cloud icon. Round 2 shows error
  screens, a storm cloud with lightning, a disconnected plug and red
  server lights — a global outage, not just a cloud.
- **Key figures in captions:** "4 TANKERS", "8 DEAD" and "$1.2B" (plus
  the other sublines) are now printed in gold under each headline.
- **Size:** round 1 was 1,018,800 bytes, almost at the 1 MiB limit.
  Round 2 is 79,305 bytes — flat vector art compresses far better,
  leaving huge headroom.
- **Legibility:** verified at 300 px across — all headlines and
  sublines stay readable.

## Sources

All 8 stories follow `~/workspace/makefun/news-13-nov-2026-brief.md`
(13 Nov 2026 news brief). No story added, removed, or invented.
