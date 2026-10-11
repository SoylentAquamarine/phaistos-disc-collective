# SQ-2 — a polar-unwrap tool, a real step toward the recount, and an honest limit found while using it

**Trigger:** last cycle's own named next step, now that the spiral center is resolved: "the actual
sign/word count is next — genuinely tractable now, not blocked on tooling."

## What's already known / not done yet

Already known: the spiral center (1260, 1300 in `disc_full.jpg`'s pixel space), verified against all four
ring boundaries by direct visual check. Not done: any actual count — and the prior cycles' own concern
about double-counting at crop seams when working on the circular image was never actually resolved, just
set aside once the center was found.

## Design and why it's non-circular

Built a genuinely different tool rather than returning to the same crop-and-eyeball approach that
previously risked seam errors: `cv2.warpPolar`, centered on the already-found spiral center, transforms
the circular image into a rectangular strip — angle along one axis, radius along the other. This removes
the wraparound/seam problem by construction (there is one continuous strip, not eight separate crops to
reconcile) and makes radial dividers appear as vertical lines, directly readable left to right instead of
needing to be tracked around a circle.

## Honesty precommitment

Report what the tool actually makes possible and what it doesn't, including a real limitation discovered
while trying to use it for an actual count, rather than presenting the tool as if it alone solves the
counting problem.

## Result

The polar unwrap works, and dramatically better than either prior center-finding attempt: viewed as a
continuous strip, the ring structure is immediately legible, and a clear, confirmed visual criterion for a
true cell/word divider emerged directly from inspecting it — a **full-height, bold vertical stroke
spanning from the outer boundary curve to the inner one**, visually matching the weight of the ring-
boundary curves themselves, clearly distinguishable from the thinner internal strokes that are part of an
individual sign's own shape (confirmed by directly comparing several candidate "divider-looking" marks
against this criterion — one early candidate, in the first segment examined, turned out on closer
inspection to likely be part of a sign's own shape, not a true divider, disclosed here as a real
near-miss rather than silently corrected away).

**A genuine, disclosed limitation found while trying to actually count**: the ring boundaries are
hand-carved and not perfectly circular even around the correctly-found center — the boundary's radius
visibly drifts up and down across the circumference. A single fixed vertical (radius) band, applied
uniformly to crop "the outer ring," does not cleanly isolate just that ring at every angle; by segment 5 of
8, the fixed band had drifted enough that it was no longer clear whether the content shown belonged to the
outer ring or spilled into an adjacent one. **This is why a full count is not completed this cycle** — doing
it reliably needs either locally-adaptive band boundaries that track the actual boundary curve per angular
segment, or much more careful manual tracing than a uniform crop allows, and rushing past this risk is
exactly the failure mode this sidequest has avoided for three prior cycles running.

Saved: `data/derived/side-a-crops/polar-unwrap.png` (full resolution, 3600×1250) and
`polar-unwrap-overview.png` (downsampled for quick reference), both reproducible from the pinned original
via `data/scripts/generate_polar_unwrap.py` — no new independent source, just a transform of the
already-checksummed image.

## Decision

This is real, usable, reusable infrastructure — a genuinely better representation for this task than the
circular image — but not itself a completed recount. The concrete next step is now precise: build
per-segment adaptive band boundaries (tracking the actual ring-boundary curve's y-position across the
strip, not assuming a fixed one) before attempting the count itself, or accept a slower, segment-by-segment
manual trace that re-establishes the local boundary by eye at each step.
