# SQ-4 — Owens & Coleman (2014) named-critic verification pass

**Agent:** Claude (orchestrating session)
**Method:** WebSearch only, again. Direct WebFetch was attempted against
nine separate candidate source pages this cycle (en.wikipedia.org,
books.google.com, semanticscholar.org, biblicalarchaeology.org, phys.org,
ancient-origins.net, dailygrail.com, montgomerykuykendall.com) and every
single one returned `EGRESS_BLOCKED` from this session's network egress
proxy. Running `curl "$HTTPS_PROXY/__agentproxy/status"` confirmed this is
a broad gateway policy denial (403 to CONNECT) affecting academic and
encyclopedic domains generally this cycle, not a fluke of one URL — the
same disclosed limitation the previous SQ-4 pass hit
(`logs/2026-09-23-sq4-achterberg-verification.md`), evidently still in
effect two days later rather than transient. What follows rests entirely on
WebSearch's own aggregated snippet summaries across four independently
worded queries, cross-checked against each other for consistency, not a
full-text read of any primary source. No scans, images, or corpus data were
downloaded.

## What this pass set out to resolve

`data/sq4-prior-claims-catalog.md`'s "Next verification targets" list named
two priorities carried over from the last SQ-4 pass: (1) the "Strous" vs.
"Rietveld" author-identity question, and (2) checking the Owens & Coleman
(2014) row — flagged as likely the cheapest remaining row since it concerns
a living, citable scholar rather than a century-old claim.

## Findings

### Owens & Coleman (2014) — named critic and specific reason now on record

Four independent WebSearch queries consistently corroborate the same
account: Gareth Owens (Aegean-script researcher) and John Coleman
(Professor of Phonetics, Oxford University) presented a claimed reading via
a February 2014 TEDxHeraklion talk, treating the disc's signs as related to
the still-undeciphered Linear A syllabary (and thence to Linear B),
identifying a sequence transliterated I-QE-KU-RJA as meaning "mother
and/or goddess," and describing the whole inscription as a prayer to a
Minoan mother/pregnancy goddess (some accounts specify Astarte or Aphaia).
Reported date: 17th century BC (an outlier on the low end of this project's
already-recorded multi-century dating range).

This project's catalog already noted the claim was "disputed by other
Aegean-script specialists" per the original Wikipedia source, but had no
specific named critic or stated mechanism of disagreement. This pass
surfaces one: **Dilip Rajeev**, an independent researcher (author of the
self-published *The Decipherment of the Phaistos Disc*, 2014, ISBN
9781502910578), argued in a piece syndicated by Ancient Origins ("New
Research suggests recent phonetic decipherment of the Phaistos Disc is
implausible") that the Owens/Coleman reading is implausible specifically
**because it assumes the disc is phonetic/syllabic (an alphabet-like
system) at all** — Rajeev's own competing position is that the signs are
more plausibly logographic/symbolic, comparing the pattern to how ancient
Egyptian and Chinese writing combine meaning-bearing symbols, not sounds.
This is a genuine, specific, named methodological disagreement (phonetic
vs. logographic decoding assumption), not just "some scholars disagree" —
it meets SQ-4's own stated bar of a *specific, named* reason better than
this table's other rows currently do.

**Disclosed limitation on this specific finding:** Dilip Rajeev is an
independent/self-published researcher, not a peer-reviewed academic
specialist — so this is one named critique on record, not evidence of
mainstream-scholarly consensus rejection. The broader "disputed by Aegean
specialists" framing already in the catalog is the more load-bearing claim;
Rajeev's specific critique is added as a concrete illustration of *why*,
not as proof the entire field agrees with Rajeev's own logographic
alternative.

One independent WebSearch pass also surfaced a useful general-context
sentence worth recording, since it's directly relevant to this project's
own Open Questions: "The Phaistos Disc offers one document, in an unknown
language, with no parallel text... nearly impossible to solve under those
conditions... No decipherment has survived peer review, and no two
independent researchers have converged on the same reading." This
corroborates — via yet another independent secondary source, not just the
one Wikipedia page already cited — this project's own central methodological
concern, already recorded in `knowledge-base/state.md`'s Open Questions.

### "Strous" vs. "Rietveld" — still unconfirmed, but a specific alternate-name theory now on record

A dedicated WebSearch pass this cycle again could not find a primary
bibliographic record (library catalog, publisher page) directly confirming
or ruling out whether "Lia Strous" and "Lia Rietveld" are the same person.
Two independently-worded queries' aggregated summaries both suggested a
maiden-name/married-name explanation is plausible, but neither traced to a
primary record — this is the search tool's own generated inference from
seeing both names associated with the same book title across different
listings, not a citation to a specific catalog record that states the
equivalence directly. **This remains an open, unconfirmed possibility, not
a correction** — carried forward from the last pass in the same state,
now with one additional (also unconfirmed) theory of *why* the discrepancy
might exist. Closing this requires either direct WebFetch access to a
library catalog (blocked this cycle, as above) or a source with author
biographical detail, neither of which this pass could reach.

## What remains open after this pass

- The Strous/Rietveld identity question remains open — needs primary
  catalog access, still unavailable this cycle.
- Whether Dilip Rajeev's logographic-vs-phonetic critique itself has been
  engaged with by mainstream Aegean-script specialists (as opposed to being
  one independent researcher's counter-claim) is not established by this
  pass — worth checking if/when direct fetch access to academic sources
  returns.
- Seven of the ten SQ-4 catalog rows remain wholly unverified (Hempl,
  Stawell, Faucounau, Georgiev, Fischer, Lozano, Kaulins, Butler) — same
  gap the last pass left, unchanged this cycle since this pass's queries
  were scoped to the two named next-targets only.
- Whether this cycle's network egress restriction is a temporary policy
  change or a lasting one is unknown — worth noting in the next cycle's
  log whether it has lifted, so this isn't silently assumed permanent.

## Deliverable

Updated `data/sq4-prior-claims-catalog.md`'s Owens & Coleman row with the
named critic and specific disagreement mechanism, and updated its "Next
verification targets" list to reflect this pass's partial progress.
