"""Hough-circle detection attempt to locate Side A's true center/radius for a future polar-grid
overlay, so a sign/word recount can walk the spiral without double-counting at crop seams.

Requires opencv-python-headless (installed this cycle; not previously a project dependency).
Result as of 2026-10-10: best Hough-circle match (1220, 1543, r=1175) traces the outer-ring/
middle-ring boundary reasonably well on the right and bottom of the disc but is visibly off-center
relative to the spiral's actual visual convergence point (upper-left of the detected center) --
not yet usable for an accurate polar angle grid. See
logs/2026-10-10-sq2-quadrant-crops-and-circle-detection-attempt.md for the full disclosed result.
"""
import cv2

SRC = 'data/derived/side-a-crops/disc_full.jpg'
OUT = 'data/derived/side-a-crops/circle_check.jpg'

img_gray = cv2.imread(SRC, cv2.IMREAD_GRAYSCALE)
blur = cv2.medianBlur(img_gray, 9)
circles = cv2.HoughCircles(
    blur, cv2.HOUGH_GRADIENT, dp=1.5, minDist=1000,
    param1=80, param2=60, minRadius=900, maxRadius=1400,
)
print(circles)

img = cv2.imread(SRC)
cx, cy, r = circles[0][0]
cv2.circle(img, (int(cx), int(cy)), int(r), (0, 255, 0), 6)
cv2.circle(img, (int(cx), int(cy)), 6, (0, 0, 255), -1)
cv2.imwrite(OUT, img)
print('saved', OUT)
