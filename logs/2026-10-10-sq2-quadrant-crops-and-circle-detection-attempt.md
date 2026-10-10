# SQ-2 — a real attempt at the recount: quadrant crops, a circle-detection tool, honest result

**Trigger:** actively searching for an unclaimed thread this cycle. SQ-2's own status trail has named "the
actual sign/word count" as the next concrete step across four consecutive updates (2026-09-29 legibility
check, 2026-09-29 tooling blocker, 2026-10-03 crop-based unblock) without anyone attempting it — each
cycle correctly declined to rush a low-confidence number, but the thread had gone three cycles without a
real attempt, not just a cautious deferral.

## What's already known / not done yet

Already known: the pinned, checksummed Side A original is legible at full resolution; octant crops exist
(`data/derived/side-a-crops/octants/`, generated 2026-10-03) but no recount has been attempted against
them. The predeclared damaged-sign/oblique-stroke/word-boundary rules from
`logs/2026-09-28-sq2-recount-rules-predeclaration.md` are frozen and ready to apply.

## Design and why it's non-circular

Rather than attempt a freehand count across the existing overlapping octant crops (real risk of
double-counting or missing cells at the seams between crops, with no way to audit afterward which cells
were double-counted), first tried to build a tool that removes that risk: locate the disc's true center
and radius so a polar-angle grid can be drawn directly on the full image, making any future count
auditable against fixed angular reference lines rather than against fuzzy crop boundaries.

## Honesty precommitment

Report exactly how far this got and where it stalled, rather than presenting a partial tool as if it were
a completed recount.

## What was built and what it found

1. **Four new quadrant crops** (`data/derived/side-a-crops/quadrants/quad_{NW,NE,SW,SE}.jpg`, 2x upscaled,
   deliberately overlapping by design so no cell sits exactly on a crop edge) — checksummed below.
2. **Installed `opencv-python-headless`** (not previously a dependency of this project) and wrote
   `data/scripts/detect_disc_circle.py`, running Hough circle detection against the pinned Side A original
   to locate its true center/radius automatically rather than eyeballing it.
3. **Result, disclosed plainly**: the strongest detected circle (center ≈(1220, 1543), radius ≈1175 px)
   traces the boundary between the outer sign-ring and the middle ring reasonably well along the right and
   bottom of the disc, but visibly undershoots on the upper-left — the true spiral convergence point (where
   the signs visibly spiral inward toward the small central rosette) sits up and to the left of the
   detected center. **Not yet accurate enough to drive a reliable polar angle grid.** Saved as
   `data/derived/side-a-crops/circle_check.jpg` for anyone picking this up next.

## Why the recount itself is still not attempted this cycle

Attempting a freehand walk-around count across the quadrant crops without a verified angular reference
would repeat exactly the failure mode this sidequest has avoided three cycles running: a number produced
under time pressure with no way to later verify whether a cell at a crop seam was counted zero or two
times. The responsible call, consistent with this project's own established discipline here, is to report
this tooling attempt honestly rather than force a count the methodology can't yet back up.

## Decision and concrete next step

This narrows the blocker precisely: a future cycle needs either (a) manual refinement of the detected
center (visually identify the spiral's convergence point in the existing `circle_check.jpg` overlay and
adjust cx/cy directly, which the current script makes trivial to do), or (b) a different automated
approach (e.g. detecting the drawn ring boundary lines directly via Hough line/ellipse detection rather
than the whole-disc outer edge). Either way, the actual recount becomes a much more mechanical, auditable
task once a correct center exists — this is now a well-scoped, concrete piece of work rather than an
open-ended "do a recount" item.

## Checksums (new files)

- `data/derived/side-a-crops/quadrants/quad_NW.jpg` — SHA256 `ada1e07019b5bc07eb624add4a1ff7c6be852e3033c86e3d3e8f92bfe5ae4f81`
- `data/derived/side-a-crops/quadrants/quad_NE.jpg` — SHA256 `49626263895e0cbb6cb9bedc1ba20b9080fa02588158bc2c11b22b4940ec3b15`
- `data/derived/side-a-crops/quadrants/quad_SW.jpg` — SHA256 `c4f25a4036753d10aea7dae1b29166c94392d203416e00e9236a66bfb1a374e6`
- `data/derived/side-a-crops/quadrants/quad_SE.jpg` — SHA256 `943fa9db774c416c2f2f4bf9141478bda4f1e72e2c49a97727a8f2044332fc0b`

All four generated deterministically from the already-pinned, already-checksummed
`data/derived/side-a-original.jpg` via `data/scripts/crop_side_a_quadrants.py` — reproducible, not a new
independent source.
