# SQ-2 — the spiral's true center found, diagnosing why the Hough-circle attempt failed

**Trigger:** last cycle's own named next step: "refine the detected center, or try line/ellipse detection
on the drawn ring boundaries directly." This cycle does both — tries ellipse detection first, diagnoses
why it still wasn't the answer, then resolves it by direct visual verification.

## What's already known / not done yet

Already known: last cycle's Hough-circle fit (center ≈1220,1543) tracked the ring boundary well on the
right/bottom but drifted badly on the upper-left — not yet usable for a polar-angle grid. Not done: any
diagnosis of *why* it failed, or a working alternative.

## Design and why it's non-circular

First tried the more sophisticated alternative named last cycle: threshold the image to isolate the whole
disc's silhouette against its lighter background, find its contour, and fit an ellipse (`cv2.fitEllipse`)
rather than assuming a circle. This fit the disc's actual physical rim very well — but checking its
reported center against the image directly revealed it sits roughly 90px away from the small central
rosette where the spiral visually converges, not on it. **This is the real diagnosis**: the disc's outer
physical silhouette and its inscribed spiral are not concentric in this photograph (plausibly a real
property of the actual object, or a photography-angle effect — not investigated further, since it doesn't
matter for the practical goal). Any circle or ellipse fit to the *outer edge* will always be fit to the
wrong feature for this purpose.

Having identified the right target (the spiral's own convergence point, not the disc's outer rim), found
it directly: cropped tightly around the central rosette, marked a candidate center, and iterated by
re-cropping and checking alignment by eye — three rounds of adjustment — until the position sat visually
at the rosette's own point of convergence. Verified at a **different, larger scale** than the search
itself: drew four concentric rings at the actual approximate ring-boundary radii around the found center
and checked them against the full disc image, not just the small rosette crop used to find it.

## Honesty precommitment

Report the center as a visual estimate, not a computed sub-pixel value, and disclose that the verification
rings still show minor drift in places rather than claiming a perfect fit.

## Result

**Spiral center found: (1260, 1300)** in `data/derived/side-a-crops/disc_full.jpg`'s own pixel coordinates
(2590×2780 image). Verified against all four visible ring boundaries around the disc's full circumference,
not just the central rosette's own shape — see
`data/derived/side-a-crops/center-refined-verification.jpg`, SHA256
`f21f800ff09ab64ec23a9956cb7c5fe056f3b1d458f2b5a24887c4f87b3be46b`. This is a dramatic improvement over
last cycle's Hough-circle attempt: the rings now track the actual drawn boundaries around the full
circumference, including the upper-left region where the prior attempt failed. **Disclosed limitation**:
still a visual estimate (not sub-pixel precise), and the innermost ring shows slight drift in a few spots
— good enough to build a usable polar-angle grid, not claimed as more precise than that.

**A genuine secondary finding, not just a tooling fix**: the disc's outer physical edge and its inscribed
spiral are measurably not concentric in this photograph. Worth keeping in mind for any future measurement
that assumes radial symmetry from the disc's outer silhouette.

## Decision

This resolves the blocker named across the last three SQ-2 cycles. The next concrete step — building the
actual polar-angle grid and attempting the sign/word recount — is now genuinely tractable rather than
blocked on center-finding. Not attempted this cycle, to keep this update focused and auditable on its own
terms (the center-finding result itself is worth verifying independently before building more on top of
it).
