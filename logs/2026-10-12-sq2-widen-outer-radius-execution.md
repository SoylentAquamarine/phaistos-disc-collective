# Execution — widened outer radius: Ring 1 fully captured, verified by direct view

Precommitment: `logs/2026-10-12-sq2-widen-outer-radius-selfreview.md` (frozen before this ran).

## What was done

**Attempt 1**: switched the polar-unwrap's source from `disc_full.jpg` to the larger, already-
on-file `side-a-original.jpg` (4818×3216), with the spiral center translated to that image's own
coordinate system — (2410, 1440), a deterministic translation of the already-verified (1260,
1300) center, not a re-finding. Computed minimum center-to-edge distance: 1440px (vs.
`disc_full.jpg`'s ~1260px). Set `MAX_RADIUS = 1420` and regenerated.

**Result of Attempt 1, directly checked**: a real but incomplete improvement. The disc's own
physical rim became visible in most segments, but a direct re-crop of segment 0 (the same
angular range checked last cycle) still showed Ring 1 signs truncated at the top edge — the
disc's hand-carved rim isn't a perfect circle, so the single binding edge-distance constraint
(1440px, in one specific direction) didn't guarantee full capture at every angle around the
circumference.

**Attempt 2, the actual fix**: padded `side-a-original.jpg` with a uniform 400px gray border on
all sides (`data/scripts/pad_source_image.py`, new reproducible script), removing the aspect-
ratio/edge constraint entirely regardless of angle. New center: (2810, 1840) in the padded
image's coordinates; minimum distance to any edge: 1840px. Set `MAX_RADIUS = 1600` (a real
safety margin below the 1840px limit) and regenerated.

**Directly verified**: re-cropped and viewed the same segment 0 angular range again. **Ring 1 is
now fully captured** — every sign shows its complete height, with the disc's own physical rim
clearly visible above the inscription, and (visible in the overview) even part of the display
mount/stand holding the disc is captured beyond that. This is a definitive, visually-confirmed
fix, not inferred from the parameter change alone.

## Artifacts updated

- `data/scripts/generate_polar_unwrap.py` — now sources from the padded image, documents both
  the ring-drift resolution (2026-10-12) and this radius fix in its own header.
- `data/scripts/pad_source_image.py` — new, small, reproducible script for the padding step.
- `data/derived/side-a-original-padded.jpg` — new derived asset, SHA256
  `6f3cb06eff3fbf91a8162cf9d42a1888d909a9c2360fb2759fa1d09263462e39`.
- `data/derived/side-a-crops/polar-unwrap.png` — regenerated, now 3600×1600 (was 3600×1250),
  SHA256 `ad53c0ce97a58e5c2d58752556e7beaff48eaf3474a86c72b28191712011e9c7`.
- `data/derived/side-a-crops/polar-unwrap-overview.png` — regenerated, SHA256
  `22ddefd84960c0a3821bf29b5d1dba427eb720fa53e807f1bfff673ab8c207e3`.

## Outcome

Both of SQ-2's own named blockers for a full count are now resolved: the ring-drift problem
(resolved last cycle, by reading continuously rather than through a fixed band) and the Ring 1
truncation (resolved this cycle, by widening the source image's own margin). **The actual
sign/divider count is now the only remaining step** — no further tooling or image-preparation
work is a prerequisite.

## Decision

Next step, not attempted this cycle: use the now-fully-prepared polar-unwrap image to attempt
the actual divider/sign count, segment by segment, using the direct-continuous-read method
validated last cycle. This is a larger, separate undertaking (the project's own established
"don't rush a count" discipline) — named explicitly as the next concrete step, not folded into
this cycle's image-preparation work.
