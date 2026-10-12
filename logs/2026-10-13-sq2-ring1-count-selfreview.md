# SQ-2 — precommitment: a first count attempt, Ring 1 only

## What's already known / not done yet

**Known:** both named blockers for a full recount are now resolved (ring-boundary drift,
resolved by continuous direct reading; Ring 1 truncation, resolved by padding the source and
widening the radius, directly verified). The established visual criterion for a true cell/word
divider is a full-height, bold vertical stroke spanning from the outer boundary curve to the
inner one, matching the weight of the ring-boundary curves themselves, distinguishable from
thinner internal sign-shape strokes (validated against a near-miss candidate in an earlier
cycle). No actual count has been attempted yet at any ring.

**Not done yet:** no divider/cell count exists for any ring of this disc side.

## Design and why it's non-circular

Scope this cycle's attempt to **Ring 1 only** (the outermost ring, the one whose own
truncation was just fixed) rather than attempting all four rings at once — a smaller, more
verifiable unit of work, consistent with this project's own discipline of not rushing a full
count in one pass. Slice the now-corrected polar-unwrap image (3600×1600) into 8 overlapping-
free, full-width-covering segments of 450px each, cropped to the top 420px (Ring 1 plus a
little of the Ring 1/Ring 2 boundary for context, not a tight band that could itself drift into
error). Read each segment directly and count dividers using the already-validated bold-full-
height-stroke criterion, left to right, keeping a running tally and flagging any genuinely
ambiguous case by position rather than guessing through it.

## Honesty precommitment

Report the exact tally, including any segment where a divider's status (true divider vs. a
sign's own stroke, or a divider sitting exactly on a segment boundary) was ambiguous — note
these explicitly rather than silently resolving them one way. This is a first count, not
necessarily the final authoritative one — cross-checking against a second method or a published
source remains a valid future step regardless of what this count finds.
