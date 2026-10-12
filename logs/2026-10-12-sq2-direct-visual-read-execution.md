# Execution — direct visual read of the polar-unwrap image: methodology confirmed, a real crop issue found

Precommitment: `logs/2026-10-12-sq2-direct-visual-read-selfreview.md` (frozen before this ran).

## Method

Sliced the already-checksummed, already-generated `data/derived/side-a-crops/polar-unwrap.png`
(3600×1250) into 6 full-height, non-overlapping 600px-wide segments (pure width-slicing, no
radius-band crop applied — every pixel of every ring's own boundary is preserved in each
segment). Viewed all 6 segments directly, left to right, tracking each ring's boundary curve
by eye rather than assuming a fixed horizontal line.

## Result 1 — the direct-read approach resolves the specific blocker from last cycle

**Confirmed across all 6 segments, full width of the image**: each ring's own boundary curve
remains continuously visible and traceable by eye throughout, including where it visibly drifts
up or down in radius (e.g., clearly visible in segment 2 and segment 4, where the boundary
between the second and third rings dips and rises noticeably across the segment width). Because
no fixed band was ever imposed — the full image is read as a continuous whole, not
pre-cropped into a ring-shaped strip — the specific failure mode from last cycle (a fixed band
losing track of a drifting boundary and risking spillover into an adjacent ring by segment 5 of
8) does not occur here. This is a real, usable methodological finding: **the polar-unwrap image
is directly legible as a whole, without needing adaptive band-tracking at all, provided it is
read continuously rather than through fixed sub-crops.**

**Visual confirmation of structure**: 4 ring boundaries are visible across the full width,
consistent with this project's own already-documented expectation of 4 rings on this side (SQ-2
scope text: "all four ring boundaries").

## Result 2 — a real, concrete technical issue found: Ring 1 (outermost) is truncated

**In every one of the 6 segments, without exception**, the very top of the image cuts off
mid-sign — the outermost ring's own signs are visibly truncated at the image's top edge (y=0),
not showing their full height the way every other ring's signs do. This is consistent across
the entire width, not a one-off artifact in a single segment. **This indicates the polar-unwrap
generation's own outer-radius bound is set too tight**, cropping into the outermost ring rather
than fully containing it.

## Outcome

This cycle does not complete a full sign/divider count — consistent with the precommitment's
own stated acceptable outcome (a partial, honestly-bounded result). It accomplishes two
narrower, concrete things instead: confirms a real methodological fix (direct continuous
reading, not fixed-band cropping, is sufficient to track the drifting boundaries), and finds a
specific, actionable technical defect in the existing polar-unwrap asset (Ring 1 truncated at
the outer edge) that should be fixed before any full count is attempted — otherwise any count
of Ring 1 specifically would be working from incomplete sign images.

## Decision

**Next step, not attempted this cycle**: regenerate the polar-unwrap with a larger outer-radius
bound in `generate_polar_unwrap.py` so Ring 1's signs are fully contained, then attempt the
actual divider/sign count using the direct-continuous-read method validated here. This is a
smaller, more concrete next step than "build adaptive band boundaries" — the adaptive-boundary
problem turns out not to need solving for *reading* the image (direct reading already handles
it), only the crop's own outer bound needs adjusting.
