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
