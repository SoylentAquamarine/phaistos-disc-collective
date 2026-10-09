# Data

Source material for the project, versioned so every finding is
reproducible.

## Present

- [`sq4-prior-claims-catalog.md`](sq4-prior-claims-catalog.md) — the SQ-4
  prior-claimed-decipherments catalog. Ten entries drafted, one
  (Achterberg, Best, Enzler & Rietveld, 2004) independently verified against
  bibliographic listings; nine still need the same treatment. See
  `logs/2026-09-23-sq4-achterberg-verification.md`.

No sign catalog yet. Unlike a multi-object corpus, there is no existing
canonical transcription to import or select between here — the Phaistos
Disc is a single physical object, and any digital sign catalog must be
built and sourced directly from publicly available high-resolution images
or published scholarly catalogs, with provenance recorded per image and per
sign. See `config/sidequests.md` SQ-1 (authenticity/provenance, first) and
SQ-2 (high-resolution sign catalog, blocked on SQ-1).

## Needed

- **Authenticity/provenance writeup** — the SQ-1 deliverable: excavation
  record, dating evidence, and the disputed-authenticity minority position,
  with primary-source citations. Not yet compiled.
- **High-resolution sign catalog** — a checksummed digital catalog of all
  241 sign-impressions (commonly cited, unverified) across both faces, with
  position/spiral-sequence/word-group metadata, sourced directly from
  publicly available images or published catalogs since no third-party
  machine-readable transcription can be simply adopted for a single unique
  object. Not yet selected or built. Do not bulk-download candidate image
  sources without explicit user authorization.
- **Prior-claims catalog** — the SQ-4 deliverable: a structured, cited
  record of the many decades of publicly claimed readings and the specific
  reason each is unaccepted. Not yet compiled.
- **Reference/comparator material** — a Cretan Hieroglyphic sign catalog
  (and, more distantly, Linear A/B) for the Linguist's and Cryptanalyst's
  comparative work (SQ-3). To be added once SQ-2's atlas exists, not
  bulk-loaded up front.

## Tooling

- **`scripts/index_corpus_qdrant.py`** — embeds this repo's own `logs/`,
  `comms/`, `steering/meetings/`, `knowledge-base/state.md`, and `methods/`
  into a Qdrant vector collection (`phaistos-disc-collective`) via the
  linuxbox's `nomic-embed-text` model, for semantic search/navigation over
  this project's own prior work. Within the compute policy's authorized
  scope (`config/research-department.md`): a navigation aid only, never a
  substitute for Claude/ChatGPT's own research judgment or adversarial
  review. Re-run after any substantive comms/logs/knowledge-base update to
  keep the index current — it fully rebuilds the collection each run.

## Convention

Any file added here should note its source URL, retrieval date, and
version/checksum in a companion `.source.md` (or in this README) so
provenance is never lost.
