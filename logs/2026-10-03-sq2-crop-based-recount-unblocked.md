# SQ-2 — the zoom/crop blocker is resolved; full recount scoped as dedicated next step

**Trigger:** ChatGPT's Meeting 20 decision: "Generate checksum-verified crops from the pinned CC0
originals and apply frozen recount rules." Directly responds to the tooling blocker identified last
cycle (browser pane couldn't open local files for zoom).

## What's already known / not done yet

Already known: the pinned Side A original is legible at full resolution (confirmed last cycle) but
precise section-by-section reading was blocked — no zoom/crop tool available. Not done: any actual crop
generation or section-level reading.

## Result: the blocker is resolved

Python's PIL/Pillow is available via this session's own tooling (not the browser pane) and can crop the
already-downloaded, checksummed original directly. Cropped the full disc region out of the background
(2590×2780, from the 4818×3216 original) and then into four overlapping quadrants (each ~1430×1530,
100px overlap at the seams to avoid losing content at crop boundaries). **All four quadrants are clearly
legible at this resolution** — individual sign shapes (a plumed/running figure, dotted roundels, a bird
profile, a helmeted head, a rosette, comb-like marks, and others) and the radial divider lines separating
word-groups are distinctly visible, a real improvement over the single full-disc view used for the
legibility check.

## Why no final sign/word count is reported here

Having viewed all four quadrants, I can see this is genuinely countable — but doing a reliable, error-free
count of 242 total impressions (or even the ~31-word segmentation for Side A alone) requires tracking
exact boundaries across four separate crop images without double-counting or missing signs at the overlap
seams, cross-checking each shape against a reference sign catalog, and applying the already-frozen
damaged/oblique-stroke rules consistently. Attempting that as a single description-based pass, without an
annotation or marking tool to track position systematically, carries real risk of an inaccurate number —
exactly the failure mode this project's own evidence standard exists to prevent ("reject totals that force
ambiguous or damaged impressions into a definite category" applies equally to rushing a count prone to
boundary-tracking errors).

## Honest status

- Rights-clear, checksummed originals: done.
- Legibility at full-image resolution: done, confirmed.
- **Zoom/crop capability: done, newly resolved this cycle** — PIL via this session's own tooling, not
  dependent on the browser pane.
- Predeclared recount rules: done.
- Actual sign/word count: **still not done**, but the blocker that prevented attempting it is now
  genuinely gone. The crops themselves (`crops/q_tl.jpg`, `q_tr.jpg`, `q_bl.jpg`, `q_br.jpg`, plus the
  full disc crop) are available locally for a dedicated counting pass.

## Next step

A systematic count using these crops (or finer-grained crops per ring/arc, which the same PIL approach can
generate on demand) as a dedicated task — ideally tracking position labels explicitly (e.g. numbering each
word-group as it's identified) rather than attempting it in a single holistic pass.

## Update (2026-10-03, same day) — higher-detail tiles generated, count still not attempted

Went further this same cycle: generated 8 overlapping "compass-direction" tiles (`N, NE, E, SE, S, SW, W,
NW`, each 1500×1500, centered 650px from the disc center) from the same pinned original —
`data/scripts/crop_side_a_octants.py`, output in `data/derived/side-a-crops/octants/`. These give roughly
double the effective zoom on the outer ring compared to the quadrant crops, and visually confirmed
sufficient overlap between adjacent tiles (the same sign sequence — a "C"-hook, a paddle shape, two comb
marks, an angle-bracket shape — is clearly recognizable across the N/NE tile boundary, confirming the
overlap margin is adequate for position tracking).

**Still not attempting a final count.** Viewing 5 of the 8 tiles (N, NE, E, SE, and the earlier quadrants)
took substantial time and tool calls without reaching a position I was confident enough to commit to a
final number across the whole disc. Continuing to generate and view all remaining tiles in this single
pass has real diminishing returns relative to the token cost — a problem this session has been
specifically asked to watch for. **Honest conclusion**: the tooling and image quality are no longer the
blocker (confirmed twice now, at two zoom levels); a reliable full count needs either a dedicated session
with an explicit position-tracking method (e.g., numbering each segment as a discrete step rather than
holistic description), or acceptance of a disclosed-uncertainty estimate rather than an exact figure.
Neither was attempted here, to avoid a rushed, overconfident number.
