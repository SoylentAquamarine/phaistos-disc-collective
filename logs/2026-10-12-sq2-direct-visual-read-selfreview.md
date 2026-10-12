# SQ-2 — precommitment: a direct visual read of the polar-unwrap image, no fixed-band crop

## What's already known / not done yet

**Known:** the polar-unwrap tool (`data/derived/side-a-crops/polar-unwrap.png`, 3600×1250)
exists and is already checksummed/pinned. The established visual criterion for a true cell/
word divider is a full-height, bold vertical stroke spanning from the outer boundary curve to
the inner one, visually matching the weight of the ring-boundary curves themselves — already
confirmed against several candidates in the prior cycle. **The specific limitation that stalled
the count**: a *fixed* vertical (radius) band, applied uniformly to crop "the outer ring" as a
sub-image for closer analysis, does not track the ring boundary's own real drift across the
circumference, so a fixed-crop approach risks spilling into an adjacent ring by segment 5 of 8.

**Not done yet:** nobody has tried directly viewing the full, already-generated polar-unwrap
image itself (not a fixed-band crop of it) and visually following each ring's own natural,
curving boundary by eye — the original limitation was specifically about automated/fixed-crop
isolation, not about whether the unwrap image itself is legible when read directly as a whole.

## Design and why it's non-circular

Split the existing, already-checksummed 3600-wide polar-unwrap image into several vertical
segments (by straightforward width-slicing, not a radius-band crop — the full height of each
slice is kept, so no ring-boundary information is ever cropped away) purely to fit within a
single image view at readable resolution. Read each segment directly, left to right, tracking
each ring's own boundary curve visually as it naturally drifts, rather than assuming a fixed
horizontal line divides the rings. Count dividers per ring using the already-established bold-
full-height-stroke criterion, exactly as previously validated. This sidesteps the specific
failure mode found last time (a fixed band losing track of a drifting boundary) by never
imposing a fixed band at all — the already-curving boundary lines are read directly off the
image, the same way a human would trace a line with a finger.

## Honesty precommitment

This is a first attempt at a direct full read, not guaranteed to produce a clean final count —
report exactly how far a reliable count gets, where ambiguity or uncertainty arises (signs
abutting a boundary, damaged/worn sections, or genuinely ambiguous divider-vs-sign-stroke
cases), and stop rather than guess through an unclear segment. A partial, honestly-bounded
result (e.g., one ring fully counted, others partially) is an acceptable, reportable outcome —
this does not need to resolve the entire disc's count in one pass.
