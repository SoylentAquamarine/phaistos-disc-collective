"""Finds Side A's true spiral center, continuing from detect_disc_circle.py's disclosed failure
(its Hough-circle fit tracked the outer-ring/middle-ring boundary on the right/bottom but drifted
badly on the upper-left).

Diagnosis this cycle: that failure happened because the disc's outer PHYSICAL silhouette and the
INSCRIBED SPIRAL are not concentric in this photograph. Confirmed by fitting an ellipse to the whole
disc's outer edge (via thresholding + cv2.fitEllipse) -- that ellipse tracks the physical rim
beautifully, but its center (1210, 1471) lands roughly 90px away from the small central rosette
where the spiral visually converges, not on it.

The spiral's own center was instead found by visual inspection: crop tightly around the central
rosette, mark a candidate center, and iterate by eye until the drawn concentric ring boundaries line
up around the full circumference. Result: (1260, 1300) in the pinned original image's pixel
coordinates -- verified against all four visible ring boundaries, not just the rosette's own shape.
See logs/2026-10-10-sq2-spiral-center-found.md for the full method and the verification image
(data/derived/side-a-crops/center-refined-verification.jpg).

This is a visual estimate, not a sub-pixel-precise computed value -- good enough to build a usable
polar-angle grid for the next step (the actual sign/word recount), not claimed as more precise than
that.
"""

SPIRAL_CENTER_PX = (1260, 1300)  # (x, y) in data/derived/side-a-crops/disc_full.jpg's own pixel space
