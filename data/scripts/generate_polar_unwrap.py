"""Transforms Side A's pinned original image into a polar ("unwrapped") view centered on the
already-found spiral center (see find_spiral_center.py), so the inscription's radial structure
becomes a linearly-scannable strip -- angle on one axis, radius on the other -- instead of a
circle, where cell/word boundaries are vertical lines readable left to right.

This is a genuine methodological improvement over counting directly on the circular image: ring
boundaries, cell dividers, and signs all become much easier to track and cross-reference across
crops, since there is no wraparound and no need to track an angular position by eye.

Disclosed limitation, found while using this tool (2026-10-11): the ring boundaries are hand-carved
and not perfectly circular even around the already-found center, so a single fixed vertical (radius)
band does not cleanly isolate one ring at every angle -- the boundary drifts up/down by a visible
amount across the circumference. **Resolved (2026-10-12)**: reading the full unwrap image directly
(not through a fixed sub-crop) keeps every ring's drifting boundary traceable by eye -- adaptive
per-segment boundaries are not needed for reading, only for an automated/cropped extraction this
project never required. See logs/2026-10-12-sq2-direct-visual-read-{selfreview,execution}.md.

Disclosed limitation, found the same cycle: with disc_full.jpg as the source, the spiral center
(1260, 1300) sits only ~1260px from that crop's own left edge, capping MAX_RADIUS and truncating
Ring 1 (the outermost ring) at the top of every one of 6 segments checked. **Resolved (2026-10-12)**:
switched the source to the original, larger photograph (side-a-original.jpg, 4818x3216, still on
file, already checksummed by crop_side_a.py), which has far more margin around the same physical
center point -- recomputed in the original's own coordinate system, the center's minimum distance to
any edge is 1440px, versus disc_full.jpg's ~1260px. See
logs/2026-10-12-sq2-widen-outer-radius-{selfreview,execution}.md.
"""
import cv2

# Even side-a-original.jpg (4818x3216) wasn't enough margin in every direction: at MAX_RADIUS=1420
# (the tightest edge, "north"/top), some angular positions still truncated Ring 1 -- the disc's
# hand-carved rim isn't a perfect circle, so the binding constraint at one angle doesn't guarantee
# full capture at every angle. Fixed by padding the source with a uniform 400px gray border on all
# sides (ImageOps.expand) so every angular direction has generous headroom regardless of the disc's
# own real eccentricity -- see data/scripts/pad_source_image.py and
# logs/2026-10-12-sq2-widen-outer-radius-{selfreview,execution}.md.
SRC = 'data/derived/side-a-original-padded.jpg'
OUT = 'data/derived/side-a-crops/polar-unwrap.png'
OVERVIEW_OUT = 'data/derived/side-a-crops/polar-unwrap-overview.png'

# Center recomputed in side-a-original-padded.jpg's own coordinate system: the same already-
# verified physical point as (1260, 1300) in disc_full.jpg, translated by disc_full.jpg's own crop
# offset (1150, 140) from crop_side_a.py plus the 400px pad border -- a deterministic translation,
# not a re-finding of the center.
CENTER = (2810, 1840)
MAX_RADIUS = 1600  # min distance to any padded edge is 1840; 1600 leaves real safety margin
ANGULAR_RESOLUTION = 3600  # 0.1 degree per output row before rotation

img = cv2.imread(SRC)
polar = cv2.warpPolar(img, (MAX_RADIUS, ANGULAR_RESOLUTION), CENTER, MAX_RADIUS, cv2.WARP_POLAR_LINEAR)
# rotate so angle is the x-axis (reads like a strip) and radius is the y-axis (outer ring at top)
polar_t = cv2.rotate(polar, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite(OUT, polar_t)

from PIL import Image
overview = Image.open(OUT).resize((1800, 625), Image.LANCZOS)
overview.save(OVERVIEW_OUT)
print('wrote', OUT, 'and', OVERVIEW_OUT)
