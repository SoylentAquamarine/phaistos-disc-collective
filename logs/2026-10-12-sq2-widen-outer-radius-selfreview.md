# SQ-2 — precommitment: widen the polar-unwrap's outer-radius bound to fix the Ring 1 truncation

## What's already known / not done yet

**Known:** last cycle's direct visual read found Ring 1 (outermost) visibly truncated at the
top edge of the polar-unwrap image (`MAX_RADIUS = 1250` in `generate_polar_unwrap.py`) across
the full width, named as the concrete next fix. Checking `disc_full.jpg`'s own dimensions
(2590×2780) against the already-found spiral center (1260, 1300) shows the center sits only
1260px from the crop's own left edge — almost exactly the current `MAX_RADIUS`, meaning the
*current crop itself*, not just the polar-unwrap parameter, is the real constraint: there is
essentially no headroom to raise `MAX_RADIUS` without the source crop running out of image on
the left side first. Directly viewing a 300×300 region near the center's left side (x=0-300,
y=1150-1450) confirms this: the disc's own inscription (a shell/fan sign) is still visible right
at the crop's left edge — the physical disc rim is **not** visible in `disc_full.jpg` at that
position, confirming the crop itself cuts into the disc.

**Not done yet:** nobody has re-cropped from the original, larger source photograph with more
margin.

## Design and why it's non-circular

`data/scripts/crop_side_a.py` records its own source: `data/derived/side-a-original.jpg`
(4818×3216, still present, already checksummed by that script's own prior run), cropped down to
`disc_full.jpg`'s current (1150, 140, 3740, 2920) box. The original has substantial unused
margin on every side (1150px left, 1078px right, 140px top, 296px bottom around the old crop
box). Recompute the spiral center's coordinates in the *original* image's own coordinate system
(a deterministic translation, not a re-finding of the center — the already-verified center stays
the same physical point, only its pixel coordinates in a different, larger crop change), use the
full original image as the new working crop (maximum available margin on every side, no reason
to re-introduce a tight boundary), and set `MAX_RADIUS` to just under the new minimum center-to-
edge distance. This directly targets the specific, now-diagnosed cause (insufficient crop
margin), not a guess.

## Stated prediction

The new minimum center-to-edge distance, computed from the original image's own dimensions, is
expected to be roughly 1400-1450px (vs. the current ~1250-1260px) — comfortably wider than the
current bound, likely enough to fully contain Ring 1 with some background margin to spare,
confirmable by directly viewing the regenerated unwrap afterward.

## Honesty precommitment

Report the actual new minimum radius computed, regenerate the unwrap, and directly view the
result to confirm (or disconfirm) that Ring 1 is now fully contained — don't assume success from
the parameter change alone without checking the actual output image.
