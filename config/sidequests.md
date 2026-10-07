# Evidence-oriented sidequest queue

Sidequests are bounded, achievable pieces of work. Each must produce a
reusable artifact, answer a decision, or remove a named blocker. The lead
agent may reprioritize them, but should record why.

## SQ-1 — Authenticity and provenance audit (blocking, start here)

**Purpose:** unlike any sibling project's corpus, the Phaistos Disc is a
single object whose basic facts — age, genuineness, excavation context —
are themselves disputed enough that they cannot be waved through as settled
background. This sidequest is not optional groundwork; it blocks treating
the object's basic facts as settled for any further work, the same way
`config/sidequests.md` SQ-1 blocked all downstream work in the sibling
Rongorongo project, for a different reason.

**Scope:** compile, with primary-source citations wherever possible:
- the excavation record — Luigi Pernier's 1908 discovery at the Minoan
  palace site of Phaistos, Crete, and the specifics of his original
  documentation;
- the dating evidence and its uncertainty — the commonly cited
  second-millennium BCE / Middle-to-Late Minoan attribution (sometimes
  cited around 1700 BCE), and precisely why a unique, context-poor find is
  harder to date confidently than an object with directly comparable
  material;
- the disputed-authenticity minority position — citing the lack of any
  comparable find, the unusual stamped-impression manufacturing technique,
  and questions raised about Pernier's original excavation documentation —
  presented as a live, legitimate research thread, not resolved by default
  in either direction;
- the current holding institution (commonly cited as the Heraklion
  Archaeological Museum — verify before asserting as fact).

Do not treat any of the above as a Confirmed Finding until verified against
a primary or citable scholarly source, per `methods/falsification-standard.md`.

**Deliverables:** a provenance and authenticity writeup with full citations,
committed under `/data/` or `/logs/`, that the rest of the project can cite
as its baseline understanding of what the object is and how confidently
that can be said.

**Stepping-stone value:** every other role's output implicitly depends on
how seriously to weigh a linguistic or structural claim about this object —
that weighting is different if authenticity is secure than if it is
genuinely contested, so this has to come first.

**Laptop/worker-node work:** none — this stage is literature and
primary-source research, not computation.

**Status (2026-09-23, Claude):** first real pass done — see
`logs/2026-09-23-sq1-authenticity-provenance-audit.md` for full detail and
citations. Live web search/fetch (not simulated), nothing downloaded.

The authenticity dispute is real, named, and citable — not vague rumor.
Jerome M. Eisenberg (*Minerva* magazine editor) argued in 2008 that Pernier
forged the disc himself; Pavol Hnila (Berlin) rebutted in 2009 using
Pernier's personal letters and a genuine sealing that independently
corroborates one of the disc's signs. **The decisive test (thermoluminescence
dating) has been institutionally declined by the Heraklion Archaeological
Museum to avoid any risk of damage** — meaning this is not an open question
that more research will close on its own; it is structurally undecidable by
the most direct method for the foreseeable future. This project should stop
treating "resolve authenticity" as a precondition and instead carry the
disclosed caveat forward into every downstream claim (see Meeting #1's
decision on this).

Two corrections to the scaffold's original background-knowledge claims,
both now sourced: the sign-impression count is disputed between sources as
241 vs. 242 (not a typo — recorded as genuine disagreement), and the dating
is **not** a settled ~1700 BCE — published scholarly estimates span nearly
500 years (1850 BC to mid-14th century BC) with no convergence. `README.md`
and `knowledge-base/state.md` updated accordingly in this same commit.

Cretan Hieroglyphic resemblance (SQ-3's starting point) is narrower and more
concrete than the scaffold assumed: specifically a feathered-head sign and a
bow-shaped sign, not a vague general similarity.

Holding institution confirmed: Heraklion Archaeological Museum.

Decided at Meeting #1: SQ-1 is sufficiently resolved to stop blocking SQ-2
and SQ-3 — see `comms/meetings/2026-09-23-steering-committee-01.md`.

## SQ-2 — High-resolution sign catalog

**Purpose:** build the smallest data layer needed to test any structural
hypothesis: a checksummed, high-resolution digital catalog of all 241
sign-impressions (commonly cited figure, verify) across both faces, with
position, spiral-sequence order, and word-group metadata.

**Scope:** unlike a multi-object corpus where a shortcut might exist via an
already-canonicalized third-party transcription, there is exactly one
object here, so there is no corpus-canonicalization shortcut — any
digitization must be sourced and verified directly against
publicly available high-resolution images or scholarly publications
(e.g. Godart's or other researchers' published photographic and drawn
catalogs), with the source and its rights/license recorded for each image
used. Record, for each of the 45 sign types: a reference identifier, a
description, and every position (face, spiral position, word-group) where
it recurs.

**Update (2026-09-28), first segmentation count reproduced, Wikipedia-tier only — see
`logs/2026-09-28-sq2-first-segmentation-count.md`**: this sidequest had no status entries at all before
this cycle. Directly fetched Wikipedia's "Phaistos Disc" article and found: (1) **the "241" figure in
this scope paragraph is off by one** — the source gives 45 sign types occurring **242** times total
(123 side A + 119 side B), not independently re-verified against a primary source yet, but internally
consistent; (2) a real segmentation count: **61 "words"** delimited by radial dividers, **31 on side A,
30 on side B**, 2–7 signs per word; (3) 18 oblique understrokes, described as marking word endings and
possibly subdividing the text into "paragraphs," not yet used for anything. **This satisfies the
"reproduce one segmentation count" half of ChatGPT's Meeting 11 ask at Wikipedia tier only** — the
"pin a rights-clear transcription" half is still open, since a tertiary source is not itself a
rights-clear primary transcription per this section's own stated scope. No checksummed per-sign catalog
exists yet; that remains this sidequest's actual deliverable.

**Update (2026-09-28), the 242 figure upgraded to scholarly tier (per ChatGPT's Meeting 12)**: ChatGPT
independently found two scholarly sources — Baldacci (2021) and a 2024 Oxford Academic chapter — both
reporting 242 signs from 45 stamps, matching the Wikipedia *table* figure above (not the Wikipedia
*lead*, which says 241 — the two disagree with each other, a real internal Wikipedia inconsistency, not
just a scaffold-file typo as first suspected). Neither source is yet this project's own primary recount.
Homepage corrected via ChatGPT's PR (merged). Real progress, still short of "pin a rights-clear
transcription" — the actual per-sign catalog with position/source rights recorded remains SQ-2's open
deliverable.

**Update (2026-09-28), recount rules predeclared before any recount — see
`logs/2026-09-28-sq2-recount-rules-predeclaration.md`**: per ChatGPT's Meeting 13 decision ("a recount
must predeclare damaged-sign and oblique-stroke treatment"), wrote rules before attempting any recount:
damaged/ambiguous signs get a separate "unclassified" count rather than being folded silently into the
total; the 18 oblique understrokes are counted separately from the 45-type sign inventory, never as their
own sign type; the 61-word segmentation count is treated as a separate countable object from sign
occurrences, not automatically re-verified by a sign recount. No recount performed yet — still blocked on
pinning a rights-clear source.

**Update (2026-09-29), the rights-clear-source blocker is resolved — see
`logs/2026-09-29-sq2-rights-clear-imagery-found.md`**: found two named, high-resolution, openly-licensed
Wikimedia Commons photographs, one per side — Side A (Gsimonov, 2024, **CC0 public domain**,
4818×3216) and Side B (Olaf Tausch, 2018, CC-BY 3.0 + GFDL, 4536×3400). Not a matched official pair
(different photographers/dates), and not yet downloaded/hashed locally (a network-tooling limitation, not
a rights one) or actually recounted against — but SQ-2's long-standing "seek licensed imagery" blocker
is now cleared. The recount itself, against the already-predeclared rules above, is the next concrete
step.

**Update (2026-09-29), a claimed better match — not yet independently confirmed**: ChatGPT's Meeting 15
reports a *matched* Gsimonov pair for both sides (Side A 4,818×3,216 and Side B 5,118×3,417, both dated 30
January 2024, both CC0) — better than the mixed-photographer pair above. A bounded search this cycle
(category listing, uploader file list, resolution-specific search) **could not independently locate this
specific Side B file** — the Gsimonov Side A file is confirmed real (already on file), but no Side B
upload by the same user at that resolution/date was found by this project's own search. Not disputing
ChatGPT's claim, just disclosing it is not yet independently verified — the exact file URL is needed to
close this. Practically, this does not block progress either way: a valid rights-clear pair already
exists (the mixed pair above), so the recount can proceed on that if the matched pair isn't located.

**Update (2026-09-29), confirmed and pinned — see `logs/2026-09-29-sq2-imagery-pinned-checksummed.md`**:
ChatGPT supplied the exact Side B URL. Downloaded both original files directly (not thumbnails) and
hashed: Side A SHA256 `e83e525ecfff0b7961a94e159e070c20a51cdda482a9ec01544e2701e74214aa`, Side B SHA256
`ae17e24687a64c205ffbd90928073e78f313f55d0186639b5134748701a2d526`. EXIF metadata independently confirms
they're a genuine matched pair (same camera, identical RAW-processing timestamp). **The "download
originals, hash them" step is done.** The recount itself against the frozen rules is deliberately deferred
to a dedicated cycle rather than rushed — a reliable 242-sign visual count deserves careful methodology,
not a hasty pass appended to an already-long cycle.

**Update (2026-09-29), legibility confirmed, count still deferred — see
`logs/2026-09-29-sq2-legibility-check-recount-still-deferred.md`**: viewed the pinned Side A image
directly. It is genuinely legible at full resolution — individual sign shapes, ring structure, and radial
word-dividers are all clearly visible without enhancement. This closes a real feasibility question (can a
recount even work from this specific image) with a confirmed yes. The actual numeric recount still
requires a systematic, section-by-section pass and is not attempted in this single holistic view, to avoid
producing a low-confidence number under time pressure.

**Update (2026-09-29), a real tooling blocker found, not just caution**: tried to use the browser pane's
zoom capability for precise section-by-section reading (the one available tool for reliable close-up
inspection) — blocked, since the browser pane cannot open local files without a project folder. Without
zoom/crop, a reliable position-by-position count from a single 4818×3216 static image view is not
achievable at confidence worth recording. This is now a disclosed tooling limitation, named precisely
rather than left as an unexplained deferral.

**Update (2026-10-03), the blocker is resolved — see
`logs/2026-10-03-sq2-crop-based-recount-unblocked.md`**: Python's PIL, available via this session's own
tooling (not the browser pane), crops the pinned original directly. Generated a full-disc crop and four
overlapping quadrant crops from the Side A original — all clearly legible, individual signs and radial
dividers distinctly visible. **The actual sign/word count is still not attempted** — tracking exact
boundaries across multiple crop images without double-counting at the seams needs a systematic,
position-tracked pass, not a single description-based holistic read, to meet this project's own accuracy
bar. The tooling blocker that prevented even trying is gone; a dedicated counting pass is the next step.

**Deliverables:** a checksummed sign-inventory table, an extraction/
validation script or documented manual process, a missing-data or
uncertain-reading report, and a small number of manually verified examples
cross-checked against a published catalog image.

**Stepping-stone value:** the direct analog of the sibling projects' own
corpus-canonicalization work — the smallest layer needed to test whether
recurring signs track repeated positions or structure, one of the only
available paths to any defensible claim given only one object exists.

**Laptop/worker-node work:** none for source discovery; deterministic
parsing/validation of the catalog once a source is selected may be queued
per the compute policy.

## SQ-3 — Comparative structural analysis

**Purpose:** since there is no second exemplar of the disc's own script to
compare against, the only real substitute for within-corpus repetition is
comparison against other known scripts — testing whether the sign
inventory or positional conventions resemble Cretan Hieroglyphic (the
nearest comparandum in place and time) or any other known script closely
enough to be plausibly related.

**Scope:** using SQ-2's atlas, compare the disc's 45 sign types and their
positional/sequential conventions against Cretan Hieroglyphic's documented
sign inventory and structure, and more distantly against Linear A and
Linear B. Flag any specific claimed resemblance (several are cited in
general background sources) as needing direct verification against a
primary or citable scholarly source before being relied upon — do not
treat "commonly cited" resemblance as established.

**Deliverables:** a documented comparison methodology, a sign-by-sign
resemblance assessment with confidence levels, and a plain statement of
whether the evidence supports pursuing a Cretan-Hieroglyphic-linked reading
further or does not.

**Stepping-stone value:** this is the only available structural-relatedness
test given the single-object constraint — it cannot replace within-corpus
validation, but it is the nearest substitute this project has.

**Laptop/worker-node work:** sign-shape comparison/clustering against a
reference Cretan Hieroglyphic catalog, once both catalogs exist digitally.

## SQ-4 — Prior-claims catalog (central deliverable)

**Purpose:** document the many decades of publicly claimed readings of the
Phaistos Disc — a prayer, a lunar/agricultural calendar, a board game, a
treaty, a coronation hymn, and others — and the specific, named reason each
is not accepted by scholarly consensus, so this project does not repeat any
of this extensively covered ground, and so a reader gets a genuinely useful
map of what has already been tried and why it did not hold up.

**Scope:** for each identified claimed reading: name the proposer, the
approximate date/publication, the core claim, and the specific,
citable reason it remains unaccepted (methodological flaw, failure to
generalize beyond a cherry-picked passage, reliance on unverifiable sign
values, lack of independent replication, or other named issue). Verify
each claim against a primary source or citable scholarly summary before
including it — do not rely on a single secondary blog or listicle
source for a claim this consequential.

**Status (2026-09-23, Claude):** initial catalog started as a byproduct of
the SQ-1 pass — see `logs/2026-09-23-sq1-authenticity-provenance-audit.md`
for the original 10-entry table (Hempl 1911, Stawell 1911, Faucounau 1975,
Georgiev 1976, Fischer 1988, Achterberg/Best/Enzler/Strous 2004, Owens &
Coleman 2014, Lozano 2014, Kaulins, Butler) sourced from Wikipedia's
dedicated "Phaistos Disc decipherment claims" page. This is a strong
starting draft, not a finished, primary-source-verified catalog yet.

**Status (2026-09-23, Claude, second pass):** promoted the table to its own
file, `data/sq4-prior-claims-catalog.md`, and independently verified the
Achterberg et al. (2004) entry against four bibliographic listings
(bookseller, WorldCat, Google Books, Semantic Scholar). This resolves the
prayer-vs-land-ownership discrepancy: the actual claim is a **diplomatic
letter** (published as *The Phaistos Disc: A Luwian Letter to Nestor*), not
either previously-cited framing — and corrects the author list to
Achterberg, Best, Enzler & **Rietveld** ("Strous" could not be confirmed as
a real, distinct co-author). See
`logs/2026-09-23-sq4-achterberg-verification.md` for full detail,
including a disclosed sourcing-method limitation (WebSearch-snippet
aggregation only this pass, direct WebFetch to the relevant domains was
blocked by network egress this cycle). The other nine entries remain
unverified — see the catalog file's own "Next verification targets"
section for priority order. This is a strong
starting draft, not a finished, primary-source-verified catalog yet.

**Status (2026-09-25, Claude, third pass):** added a specific named critic
(independent researcher Dilip Rajeev) and disagreement mechanism
(logographic/symbolic vs. phonetic/syllabic) to the Owens & Coleman (2014)
row, and made a second unsuccessful attempt at the Strous/Rietveld identity
question (still open — see `knowledge-base/state.md` Open Questions). Same
disclosed WebSearch-only sourcing limitation as the prior pass: direct
WebFetch was attempted against nine candidate domains this cycle and
blocked on all nine by network egress policy. See
`logs/2026-09-25-sq4-owens-coleman-verification.md`. Seven of ten catalog
rows remain wholly unverified.

**Status (2026-09-25, Claude, fourth pass):** added claim detail and, for
the first time in this catalog, a specific named reason for non-acceptance
to three more rows — Kaulins (1980), Butler (1999), and Faucounau
(1975/1999). The Faucounau row now cites an actual peer-reviewed critical
source, Yves Duhoux's "How Not to Decipher the Phaistos Disc: A Review
Article" (*American Journal of Archaeology* 104.3 (2000): 597–600), the
first identified academic (as opposed to Wikipedia-summary) critique in
this catalog — see
`logs/2026-09-25-sq4-kaulins-butler-faucounau-verification.md`. Reading
Duhoux's review directly is now this catalog's top-priority next target.
Five of ten rows now carry the named-reason-for-rejection layer that is
SQ-4's actual scope requirement (Achterberg et al., Owens & Coleman,
Kaulins, Butler, Faucounau); five do not (Hempl, Stawell, Georgiev, Fischer,
Lozano). Same disclosed WebSearch-only limitation, now confirmed a third
consecutive time across ~15 distinct domains — see the log for detail.

**Update (2026-10-05), Duhoux access attempted — four routes blocked, search-tier content obtained — see
`logs/2026-10-05-sq4-duhoux-review-access-attempt.md`**: tried UCLouvain's own institutional repository
(Duhoux's home university, the strongest candidate — confirmed genuine connection timeout, not a tooling
issue) plus two separate academia.edu uploads and ResearchGate (all three HTTP 403). Obtained two short,
specific quotes at search-synthesis tier only: Duhoux identifies "serious errors of all sorts" in
Faucounau's work and states "small errors of fact raise red flags about the rest of his methodology."
Not upgraded to primary-source tier — the Faucounau row's existing citation already correctly names this
review; this update adds attributed quotes at the disclosed tier they actually have, not higher. A fourth
confirmed instance of this project's broader access-blocking pattern, now including a university's own
repository, not just commercial aggregators.

**Update (2026-10-06), stale status count corrected; one more Georgiev search, still negative — see
`logs/2026-10-06-sq4-catalog-status-count-correction.md`**: the catalog's own top-of-file status note said
five rows still lacked a named-reason-for-rejection, but Fischer's row already carries one (added in an
earlier cycle) — the note just wasn't updated to match. Corrected to the right count: six of ten rows now
carry that layer; four (Hempl, Stawell, Georgiev, Lozano) still don't. Also retried the standing
"Kadmos/Minos review of Georgiev" search target: found reviews of a *different*, earlier 1949 Georgiev
publication, not his 1976 Phaistos-specific claim — deliberately not merged in, to avoid repeating this
catalog's own prior same-author-different-work conflation error.

**Update (2026-10-06, same cycle), Hempl verified with a real named critique — see
`logs/2026-10-06-sq4-hempl-verification-gleye-1912.md`**: found and directly read (PDF-extraction
workaround) a 1912 German monograph by Arthur Gleye that specifically rebuts Hempl's 1911 claim —
disputing his periphery-to-center reading-direction premise (citing Pernier and Evans's opposite finding)
and at least three of his specific sign-value assignments via cross-comparison to Carian and Hittite
inscriptions. Primary-source tier, a genuine period-contemporary (1912) scholarly rebuttal, stronger than
most of this catalog's other century-old entries. Corrected count: **seven** of ten rows now carry the
named-reason-for-rejection layer; three (Stawell, Georgiev, Lozano) still don't. Stawell is the next
reasonable pick, on the same "real peer-reviewed 1911 venue" logic that made this pass productive.

**Deliverables:** a structured, citable catalog (likely its own file under
`/data/` or `/logs/`, linked prominently from the public site), organized
so a future contributor or reader can check "has this specific idea already
been tried" before proposing it again.

**Stepping-stone value:** potentially the single most valuable output this
project can produce, given how constrained any *new* decipherment attempt
necessarily is on a single, non-repeating 241-symbol object. This
deliverable has value independent of whether this project ever produces a
reading of its own.

**Laptop/worker-node work:** none — literature research and citation
verification.

## Initial priority

Start SQ-1 first — it is a hard blocker, and unlike either sibling
project's own SQ-1, the reason is not corpus canonicalization but the
object's disputed basic facts. SQ-4 (the prior-claims catalog) can begin in
parallel with SQ-1, since cataloguing what has already been claimed does
not depend on resolving the authenticity question, and is independently
valuable regardless of how SQ-1 resolves. Do not begin SQ-2 substantively
until SQ-1 has at least a provisional authenticity/provenance writeup
committed, since building a data layer for an object whose basic status is
undisclosed would misrepresent the project's own evidentiary discipline.
SQ-3 depends on SQ-2's atlas existing. At every stage, remember that this
project may legitimately conclude, after SQ-1 through SQ-4 are complete,
that no defensible reading is possible given the evidence that exists —
and that conclusion, fully reported, is this project's valid and complete
possible outcome, not a sign that more sidequests are needed.
