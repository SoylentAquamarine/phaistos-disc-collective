"""Transforms Side A's pinned original image into a polar ("unwrapped") view centered on the
already-found spiral center (see find_spiral_center.py), so the inscription's radial structure
becomes a linearly-scannable strip -- angle on one axis, radius on the other -- instead of a
circle, where cell/word boundaries are vertical lines readable left to right.

This is a genuine methodological improvement over counting directly on the circular image: ring
boundaries, cell dividers, and signs all become much easier to track and cross-reference across
crops, since there is no wraparound and no need to track an angular position by eye.

Disclosed limitation, found while using this tool: the ring boundaries are hand-carved and not
perfectly circular even around the already-found center, so a single fixed vertical (radius) band
does not cleanly isolate one ring at every angle -- the boundary drifts up/down by a visible amount
across the circumference. A full, reliable count needs either locally-adaptive band boundaries per
angular segment, or careful manual tracing segment by segment watching for this drift, not a single
fixed crop applied uniformly. Not yet attempted at that level of care -- see
logs/2026-10-11-sq2-polar-unwrap-tool.md.
"""
import cv2

SRC = 'data/derived/side-a-crops/disc_full.jpg'
OUT = 'data/derived/side-a-crops/polar-unwrap.png'
OVERVIEW_OUT = 'data/derived/side-a-crops/polar-unwrap-overview.png'

CENTER = (1260, 1300)  # from find_spiral_center.py, visually verified against all four ring boundaries
MAX_RADIUS = 1250
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
