# SQ-4 — Prior claimed decipherments catalog

Central deliverable per `config/sidequests.md` SQ-4: a structured, citable
record of the many decades of publicly claimed readings of the Phaistos
Disc, and the specific, named reason each is not accepted by scholarly
consensus, so this project does not silently retread already-covered ground
and a reader can check "has this specific idea already been tried" before
anyone proposes it again.

**Status:** partial / in progress. Ten entries below were first drafted as
a byproduct of the SQ-1 pass (see
`logs/2026-09-23-sq1-authenticity-provenance-audit.md`), sourced from
Wikipedia's dedicated "Phaistos Disc decipherment claims" page via WebFetch.
One entry (Achterberg, Best, Enzler & Rietveld, 2004) has since been
independently checked against bibliographic listings (bookseller, WorldCat,
Google Books, Semantic Scholar) — see
`logs/2026-09-23-sq4-achterberg-verification.md` — and corrected below. The
other nine entries are **not yet independently verified** against a primary
publication or a bibliographic record beyond the single Wikipedia page that
first surfaced them; treat their "claimed reading type" column as a
starting draft, not a finding.

None of this table's entries are "not accepted for reason X" details yet —
that named-reason-per-claim layer (the actual SQ-4 scope requirement) still
needs to be filled in per entry, ideally alongside each entry's
verification pass so the reason is checked against the same source as the
claim itself.

| Proposer | Year | Claimed script/language | Claimed reading type | Verification status |
|---|---|---|---|---|
| George Hempl | 1911 | Ionic Greek, syllabic | Religious/ritual hymn | Unverified — Wikipedia-only |
| F.M. Stawell | 1911 | Homeric Greek, syllabic | Religious invocation | Unverified — Wikipedia-only |
| Jean Faucounau | 1975 | Proto-Ionic Greek, syllabic | Funerary hymn | Unverified — Wikipedia-only |
| Vladimir Georgiev | 1976 | Hittite, syllabic | Unspecified | Unverified — Wikipedia-only |
| Steven R. Fischer | 1988 | A Greek dialect, syllabic | Linguistic text (unspecified genre) | Unverified — Wikipedia-only |
| Winfried Achterberg, Jan Best, Kees Enzler, Lia Rietveld | 2004 | Luwian/Anatolian hieroglyphic | **Diplomatic letter** — a letter transcribed in the local Phaistos script, purportedly from Great King Tarhundaradus of Arzawa (western Anatolia) to King Nestor of Pylos (Mycenaean Greece), re: Cretan dependencies. Published as *The Phaistos Disc: A Luwian Letter to Nestor* (Publications of the Henri Frankfort Foundation vol. 13, Dutch Archaeological and Historical Society, Amsterdam; ISBN 9789072067111; OCLC 64193136); later editions Harrassowitz 2011 and a 3rd revised/extended edition 2021. Proposed date: 14th century BC, from the group's dating of associated Linear A tablet PH 1. | **Corrected this cycle** — see `logs/2026-09-23-sq4-achterberg-verification.md`. Resolves the earlier "prayer/hymn vs. land-ownership-document" discrepancy: neither framing was accurate: the claim is a diplomatic letter. Author list corrected from the bootstrap-era "Achterberg, Best, Enzler & Strous" — "Strous" could not be confirmed as a real, distinct fourth/fifth author across 4 independent bibliographic listings; it may be a name-variant mixup with Rietveld, but this is an open, unconfirmed possibility, not a verified fact. Sourced via WebSearch snippet aggregation only this pass (direct WebFetch to the bibliographic sources was blocked by network egress this cycle) — still not a read of the primary 153-page publication itself. |
| Gareth Owens & John Coleman | 2014 | Minoan / Linear-tradition | Prayer to a goddess | Unverified beyond the original Wikipedia page — but independently corroborated as *disputed by other Aegean-script specialists* (same source), i.e. even the original secondary source discloses this is not accepted as a solution |
| Lozano | 2014 | — | Calendar reading | Unverified — Wikipedia-only, first name/full citation not yet found |
| Andis Kaulins | — | — | Proof of a geometric theorem, in Greek | Unverified — Wikipedia-only |
| Alan Butler | — | — | Astronomical calendar / calculating device | Unverified — Wikipedia-only |

## General scholarly assessment (carried over from SQ-1 pass)

Per the same Wikipedia decipherment-claims page (not yet independently
re-verified this cycle): "a large part of the claims are clearly
pseudoscientific," and linguists are doubtful the inscription is long
enough — 241/242 (disputed) sign-impressions across 61 short word-groups —
to be unambiguously interpretable at all. This is directly relevant to this
project's own central Open Question in `knowledge-base/state.md`: what
would count as defensible evidence for any reading at all, given the
object's size and uniqueness.

## Next verification targets

In priority order for a future pass, cheapest/most-consequential first:
1. Confirm or rule out the "Strous"/Rietveld identity question above via a
   library catalog record read directly (not search-snippet aggregation).
2. Owens & Coleman (2014) — a living, citable, mainstream Aegean-script
   scholar; likely the easiest of the unverified rows to check against a
   real journal article rather than an encyclopedia summary.
3. The remaining Wikipedia-only rows (Hempl, Stawell, Faucounau, Georgiev,
   Fischer, Lozano, Kaulins, Butler) — verify existence, date, and claim
   framing against a second source each, and add the specific
   named-reason-for-rejection this table still lacks for every row.
