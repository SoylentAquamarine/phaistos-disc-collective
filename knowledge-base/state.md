# Knowledge Base — Current State

Last updated: 2026-09-23 (bootstrap)

This file is the shared, evolving understanding of the group. It only
changes via pull request. Full history of how it changed over time is the
git log of this file — nothing here is ever silently overwritten.

## Confirmed Findings

- **Discovery record**: the disc was discovered 3 July 1908 by Italian
  archaeologist Luigi Pernier during excavation of the Minoan palace site of
  Phaistos, Crete. Sourced via [Wikipedia](https://en.wikipedia.org/wiki/Phaistos_Disc)
  and the [Heraklion Archaeological Museum's own page](https://heraklionmuseum.gr/en/exhibit/the-phaistos-disc/) —
  a secondary/tertiary source disclosure, not a primary excavation-report
  read. One unresolved discrepancy: a National Geographic piece credits
  joint discovery to Federico Halbherr (the site's excavation director) and
  Pernier, while the two sources above credit Pernier alone. See
  `logs/2026-09-23-sq1-authenticity-provenance-audit.md`.
- **Physical sign counts, with a genuine disagreement disclosed rather than
  resolved**: 45 distinct sign types and 61 word/sign-groups are consistent
  across every source checked. The total sign-impression count is
  **disputed between sources**: Wikipedia's own article states 242 (123
  side A + 119 side B); multiple other secondary sources (an inkl.com piece,
  an ExplorersWeb article) state 241. This project uses "241/242" rather
  than silently picking one. Source: direct WebFetch of
  [Wikipedia's Phaistos Disc article](https://en.wikipedia.org/wiki/Phaistos_Disc).
- **The authenticity dispute has specific names and a specific, structural
  reason it stays open**: Jerome M. Eisenberg (antiquities dealer, editor of
  *Minerva* magazine) argued in a 2008 *Minerva* article that Pernier forged
  the disc for professional-reputation reasons, modeling it on the genuinely
  ancient Etruscan Magliano Disc; Pavol Hnila (University of Berlin)
  rebutted in 2009 using Pernier's personal correspondence and a genuine,
  independently-excavated sealing that corresponds to one of the disc's
  signs. Most importantly: **the Heraklion Archaeological Museum has
  declined to permit thermoluminescence dating**, specifically to avoid any
  risk of damage — meaning the single most direct test that could resolve
  the dispute is not merely undone, it is institutionally foreclosed for
  now. Secondary-source disclosure: found via Wikipedia and a
  languagehat.com discussion thread, not read in the original *Minerva*
  article or Hnila's paper directly. See the log for full citations.
- **Dating is genuinely unsettled, not a rounded consensus figure**:
  published scholarly estimates span nearly 500 years with no convergence —
  Yves Duhoux (1977): 1850–1600 BC; Kristian Jeppesen (1963): after 1400 BC;
  Louis Godart (1990): anywhere in Middle-to-Late Minoan; Jan Best: early-mid
  14th century BC. This supersedes this project's own bootstrap scaffolding,
  which stated a flat "~1700 BCE" framing without this range. Source: direct
  WebFetch of Wikipedia's Phaistos Disc article.
- **Cretan Hieroglyphic resemblance is narrow and specific, not a vague
  general similarity**: the clearest cited examples of sign resemblance are
  a feathered-head sign and a bow-shaped sign, per a National Geographic
  piece — with "one or two others" mentioned but not specified in the
  source checked. This gives SQ-3 a concrete, narrow starting point rather
  than an unspecified claim.
- **Holding institution confirmed**: Heraklion Archaeological Museum, Crete,
  Greece — via the museum's own official page.

All of the above rest on web-search/WebFetch summaries of secondary and
tertiary sources (chiefly Wikipedia), not a primary excavation report or
peer-reviewed journal article read directly — this limitation is disclosed
per `methods/falsification-standard.md` and should be closed by a future
pass that reads the actual *Minerva* 2008 article, Hnila's 2009 response,
and Pernier's original 1908 report where accessible.

## Active Hypotheses

_(none yet)_

## Rejected Hypotheses

_(none yet — bootstrap state. As the Historian catalogues prior public
claimed readings under SQ-4, ones that fail this project's own review will
be logged here with the specific reason, so they are not re-proposed
without new evidence. Note that most previously *published* claimed
readings — a prayer, a lunar/agricultural calendar, a board game, a
treaty, a coronation hymn, and others — were never actively re-proposed by
this project in the first place; they belong primarily in the SQ-4 catalog
as external prior claims, and only enter Rejected Hypotheses here if this
project independently re-tests one.)_

## Open Questions

- ~~Is the disc's ancient authenticity secure enough to treat any
  linguistic/decipherment claim as meaningful~~ — **narrowed, not closed**
  (see Confirmed Findings and Meeting #1,
  `comms/meetings/2026-09-23-steering-committee-01.md`): the dispute is
  real, named, and specific, and the decisive test has been institutionally
  declined rather than merely not-yet-run. Decided at Meeting #1: this
  project proceeds under disclosed scholarly-consensus authenticity rather
  than waiting for a resolution that current museum policy forecloses.
- Given only 241/242 (disputed) symbols exist on one object, what would
  actually count as defensible evidence for any proposed reading, in
  principle — and does any existing claimed decipherment meet that bar?
  Sharpened by this cycle's finding that the field's own general assessment
  (per the SQ-4 catalog draft) is that most claims are "clearly
  pseudoscientific" and the inscription may be too short to be
  unambiguously interpretable at all — this is still the central
  methodological question this project must answer before attempting any
  reading of its own.
- Does the sign inventory show any structural relationship to Cretan
  Hieroglyphic close enough to be worth pursuing further? Narrowed by this
  cycle: two specific signs (a feathered-head sign, a bow-shaped sign) are
  the concrete starting point per one secondary source, still needing
  primary-source verification before being relied on for anything — see
  `methods/falsification-standard.md`.
- New from this cycle: does the Achterberg, Best, Enzler & Strous (2004)
  claim actually argue for a "land ownership document" or a "prayer/hymn"
  reading? Two secondary sources checked in this pass disagree, and the
  actual 2004 publication has not yet been read directly.
