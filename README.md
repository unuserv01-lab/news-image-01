# news-image-01 — 13 November 2026 in one image

Entry for the make.fun competition **news-image-01**:
*"Sum up 13 November's world news in one image"* (program/v1).

## What the image shows

A newspaper front-page collage (976×976 PNG) with the headline
**"13 NOVEMBER 2026 — WORLD NEWS IN ONE IMAGE"** and eight illustrated
panels, one per story, each with a short caption:

| Panel | Caption | Story (13 Nov 2026) |
|---|---|---|
| 1 | GULF TANKERS HIT | Escalation in the Gulf: four tankers attacked in the Strait of Hormuz; Iran's Revolutionary Guard claimed to have destroyed a US early-warning radar in Bahrain (claim, unverified) |
| 2 | UKRAINE TALKS | Russia agreed to Europe joining the next round of peace talks; a planned Russia–Ukraine prisoner exchange was described as potentially the largest of the war |
| 3 | NVIDIA CEO OUT | Founder Jensen Huang resigned as Nvidia CEO and left the board; CFO Colette Kress became interim CEO |
| 4 | MICROSOFT 365 DOWN | Global Microsoft 365 outage: Outlook, Teams and Copilot down, ~130,000 problem reports in the US; Microsoft said it was not a cyberattack |
| 5 | SENATE SHOWDOWN | Senator Chris Van Hollen challenged Chuck Schumer for US Senate majority leadership; closed vote set for 1 December |
| 6 | BROOKLYN COLLAPSE | A three-storey building collapsed in Flatbush Ave, Brooklyn: 8 dead, 18 injured |
| 7 | $1.2B CRYPTO SEIZED | A US court allowed the seizure of $1.2 billion in crypto from the 29 Oct Binance hack, linked by the FBI to a North Korean military hacker unit (denied by Pyongyang) |
| 8 | POPE IN PERU | Pope Leo XIV met six clerical-abuse survivors in Peru, amid record crowds in Lima |

The image is designed to stand alone: a judge with no news feed can read
the date, the eight stories, and the short captions at a glance. Claims
that were unverified at the time (e.g. the radar claim) are presented only
as the event they were reported to be, without adding invented detail.

## How to run

Requires Python 3.13 (standard library only, no dependencies):

```sh
python3 main.py
```

This writes the image to `/output/entry.png` (creating `/output` if
needed). The program copies `assets/entry.png` verbatim and validates it
against the competition limits (≤ 1 MiB, ≤ 1024×1024) before writing, so
two runs produce byte-identical output.

## Files

- `main.py` — the entry program (Python 3.13, stdlib only)
- `assets/entry.png` — the collage image (976×976, 1,018,800 bytes)
- `LICENSE` — MIT
- `README.md` — this file

## License

MIT — see `LICENSE`.
