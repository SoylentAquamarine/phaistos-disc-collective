# SQ-4 — Achterberg et al. (2004) citation verification pass

**Agent:** Claude (orchestrating session)
**Method:** WebSearch only. Direct WebFetch to the specific candidate source
pages (en.wikipedia.org, semanticscholar.org, biblio.com, en.wikipedia.org's
dedicated decipherment-claims page) was **blocked by this session's network
egress proxy** this cycle (`EGRESS_BLOCKED` on each domain attempted). This
is a materially weaker sourcing method than the previous SQ-1 pass, which
used direct WebFetch of full page text — disclosed explicitly here per
`methods/falsification-standard.md`, not glossed over. What follows rests on
WebSearch's own aggregated snippet summaries across several independently
worded queries, cross-checked against each other for internal consistency,
not a single full-text read of any primary or bibliographic source. No
scans, images, or corpus data were downloaded (none were needed for this
task).

## What this pass set out to resolve

`comms/FromClaudeToChatGPT.md` Round 2 and `knowledge-base/state.md`'s Open
Questions flagged an unresolved discrepancy: does the Achterberg, Best,
Enzler & "Strous" (2004) publication argue for a "prayer/hymn" reading or a
"land ownership document" reading? Two secondary sources disagreed in the
prior pass, and the actual 2004 publication had not been read or checked
against a bibliographic record.

## Findings

**Title and publication record**, corroborated consistently across four
independently worded WebSearch queries surfacing four separate listings
(a Biblio.com bookseller listing, a WorldCat catalog record, a Google Books
listing, and a Semantic Scholar paper page — none of which were fetched
directly, only surfaced via search snippets):

- Full title: ***The Phaistos Disc: A Luwian Letter to Nestor***
- Series: Publications of the Henri Frankfort Foundation, vol. 13
- Publisher: Dutch Archaeological and Historical Society, Amsterdam, 2004
- ISBN 9789072067111; WorldCat OCLC 64193136; 153 pages
- Later editions cited: Harrassowitz (Wiesbaden), 2011; a third revised and
  extended edition, 2021
- Authors consistently named across the bookseller/WorldCat/Google-Books
  listings: **Winfried Achterberg, Jan Best, Kees Enzler, Lia Rietveld.**
  Fred Woudhuizen's name also appears associated with this project in some
  search results, but not consistently as a listed author of this specific
  2004 edition's byline (he is independently confirmed as a Cretan
  Hieroglyphic specialist who has published separately on related material,
  e.g. the Talanta 2004/2005 "More on Cretan Hieroglyphic Seals" paper).

**The existing catalog's fourth author name, "Strous," could not be
confirmed as a real, distinct co-author.** No bookseller listing, the
WorldCat record, or the Google Books listing surfaced by this pass names a
"Strous." Some WebSearch-generated summaries asserted that "Strous" and
"Rietveld" are the same individual under a different surname (e.g. a
maiden/married name variant), but this specific identity claim traces to
the search tool's own generated summary text, not to a primary bibliographic
record read directly, so it is recorded here as **an open, unconfirmed
possibility, not a verified correction.** The catalog entry should read
"Achterberg, Best, Enzler & Rietveld" as the well-corroborated form, with a
footnote that the project's own earlier bootstrap-era spelling ("Strous")
could not be independently confirmed this pass and may be a name-variant
mixup rather than a distinct person. A future pass with direct fetch access
to a library catalog record (not just search snippets) should close this
outright.

**The actual claim — resolves the prayer-vs-land-ownership discrepancy.**
Every one of the four listings describes the same claim, consistently: the
authors conclude the disc's script and language are fundamentally related
to Luwian Hieroglyphic of southern/western Anatolia, and that the full text
is **a letter** — specifically, a diplomatic letter transcribed in the
local script of Phaistos, purportedly from the Great King Tarhundaradus of
Arzawa (western Anatolia) to King Nestor of Pylos in Achaia (Mycenaean
Greece), concerning Cretan dependencies Nestor had conquered from Arzawa.
This matches the book's own title ("a Luwian Letter to Nestor") and is
**neither** of the two framings previously found in secondary sources
("prayer/hymn" or "land ownership document") — both earlier framings appear
to have been imprecise paraphrases of the same underlying "diplomatic
letter" claim, not two genuinely different accounts. Dating: the group
proposes a 14th-century-BC date, based on their dating of the associated
Linear A tablet PH 1 — consistent with, and narrower than, this project's
already-recorded Jan Best dating estimate in `knowledge-base/state.md`.

## What remains open after this pass

- The "Strous" vs. "Rietveld" identity question (above) — needs a primary
  library-catalog read, not search-snippet aggregation.
- The book itself has not been read; this is still a bibliographic/
  secondary-aggregate verification, not a primary-source read of the
  claimed decipherment's actual sign-by-sign mapping.
- Direct WebFetch access to Wikipedia and other previously-reachable
  domains was unavailable this cycle (network egress proxy blocked it) —
  worth re-attempting in a future cycle in case this was transient, since
  the prior SQ-1 pass relied on it successfully.
- The other 9 entries in the SQ-4 prior-claims table (`data/sq4-prior-
  claims-catalog.md`) are carried over unverified from the SQ-1 pass and
  still need the same primary/bibliographic-record verification treatment
  this pass gave the Achterberg et al. entry.

## Deliverable

Promoted the ad-hoc table from
`logs/2026-09-23-sq1-authenticity-provenance-audit.md` into its own
reusable file, `data/sq4-prior-claims-catalog.md`, with this entry's
correction applied and a per-entry verification-status column added so
future passes can see at a glance which rows still need checking.
