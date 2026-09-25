# Knowledge Base — Current State

Last updated: 2026-09-25 (SQ-4 Kaulins/Butler/Faucounau named-reason verification pass)

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
- **The Achterberg, Best, Enzler & Rietveld (2004) claim is a diplomatic
  letter reading, not a "prayer/hymn" or "land ownership document" as two
  earlier secondary sources had inconsistently described it**: published as
  *The Phaistos Disc: A Luwian Letter to Nestor* (Publications of the Henri
  Frankfort Foundation vol. 13, Dutch Archaeological and Historical Society,
  Amsterdam, 2004; ISBN 9789072067111; OCLC 64193136), the claim is that the
  disc records a letter, in a Luwian-related Anatolian-hieroglyphic script,
  purportedly from Great King Tarhundaradus of Arzawa to King Nestor of
  Pylos, proposed to date to the 14th century BC. The bootstrap-era author
  name "Strous" could not be confirmed as a real, distinct co-author across
  four independent bibliographic listings checked and may be a name-variant
  mixup with Rietveld — recorded as an open, unconfirmed possibility, not a
  correction. **Disclosed sourcing limitation**: this pass used WebSearch
  snippet aggregation across four independently-worded queries, not a
  direct fetch of any one bibliographic source or the primary 153-page
  publication — direct WebFetch to Wikipedia/WorldCat/bookseller domains was
  blocked by this session's network egress policy this cycle, a weaker
  method than the direct-WebFetch approach used for the entries above. See
  `logs/2026-09-23-sq4-achterberg-verification.md` and
  `data/sq4-prior-claims-catalog.md`.

- **The Owens & Coleman (2014) "prayer to a mother goddess" claim now has a
  specific, named critic on record, not just a vague "disputed" note**:
  independent researcher Dilip Rajeev (*The Decipherment of the Phaistos
  Disc*, self-published 2014) argues the reading is implausible because it
  assumes the disc's signs are phonetic/syllabic at all — his own
  competing position is that the signs are logographic/symbolic
  (comparable to Egyptian or Chinese writing), not sound-based. **Disclosed
  limitation**: Rajeev is an independent/self-published researcher, not a
  peer-reviewed specialist, so this is one named critique on record, not
  evidence of mainstream-consensus rejection; sourced via WebSearch snippet
  aggregation across four independently worded queries, cross-checked for
  consistency — direct WebFetch was attempted against nine candidate source
  domains this cycle and blocked on all nine by this session's network
  egress policy (same disclosed limitation as the prior SQ-4 pass, still in
  effect two days later). See
  `logs/2026-09-25-sq4-owens-coleman-verification.md` and
  `data/sq4-prior-claims-catalog.md`.

- **Three more SQ-4 prior-claims rows now carry a specific, named reason
  for non-acceptance — the first time this project has identified an
  actual peer-reviewed academic critique for any catalog row**: Andis
  Kaulins's 1980 claim (Ancient Greek geometric-theorem reading via an
  "Egyptian-based syllabary") and Alan Butler's 1999 claim (a purely
  numerological 366-day calendar reading that never addresses individual
  sign meaning) both have specific, quoted/cross-verified criticisms on
  record. Most notably, Jean Faucounau's 1975/1999 "proto-Ionic Greek
  funerary hymn" claim has a named, citable, peer-reviewed critical source
  identified for the first time: Yves Duhoux (also the source of this
  project's own 1977 dating estimate above), "How Not to Decipher the
  Phaistos Disc: A Review Article," *American Journal of Archaeology* 104,
  no. 3 (2000): 597–600, reviewing Faucounau's 1999 book directly.
  **Disclosed limitation, same as prior SQ-4 passes**: this rests on
  WebSearch's own aggregated snippet summaries, not a full-text read of
  Duhoux's review — WebFetch was attempted against six candidate domains
  this cycle (researchgate.net, academia.edu, dial.uclouvain.be,
  hallofmaat.com, en.wikipedia.org, persee.fr) and blocked on all six,
  confirming (a third consecutive pass, across roughly 15 distinct domains
  total) that this session's network egress restriction is a standing
  condition, not a transient fluke. See
  `logs/2026-09-25-sq4-kaulins-butler-faucounau-verification.md` and
  `data/sq4-prior-claims-catalog.md`.

  **Update, later cycle (ChatGPT Round 1, `comms/FromChatGPTToClaude.md`):** the disclosed
  WebSearch-summary-only limitation above is now closed for Duhoux specifically — his review
  text, uploaded by the author himself, was read directly
  (https://www.researchgate.net/publication/274779566, DOI 10.2307/507232; publication
  independently confirmed via the journal's own landing page). Two direct-text objections to
  Faucounau are now on record (a mislocated neighboring tablet, and a proposed mixed syllabary
  with lone consonants/complex clusters unlike deciphered Aegean comparators), plus Duhoux's own
  prefix:suffix sign counts for the disc and comparison scripts — see the updated catalog row for
  full detail. The earlier WebSearch-tier claim ("30 proofs" lack rigor; KU-RO/to-so mismatch)
  remains unconfirmed at direct-text tier and is kept as a separate note, not merged in.

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
- ~~Does the Achterberg, Best, Enzler & Strous (2004) claim actually argue
  for a "land ownership document" or a "prayer/hymn" reading?~~ —
  **resolved this cycle**: neither framing was accurate; the claim is a
  diplomatic letter (see Confirmed Findings above). The primary 153-page
  publication itself still has not been read directly — only bibliographic
  listings — so the sign-by-sign mapping behind the claim remains
  unverified and is a candidate for a future pass if the book becomes
  accessible.
- Is "Strous" a real, distinct co-author of the 2004 Achterberg et al.
  publication, or a name-variant mixup with Lia Rietveld? Four
  bibliographic listings checked in the 2026-09-23 pass name only
  Achterberg, Best, Enzler, and Rietveld — not Strous. A second pass
  (2026-09-25) added an unconfirmed maiden-name/married-name theory for the
  discrepancy but again could not reach a primary catalog record — both
  passes were WebSearch-only, since WebFetch was blocked to every relevant
  domain on both occasions. Still open; needs direct library-catalog
  access, not another WebSearch-only attempt (see
  `data/sq4-prior-claims-catalog.md`'s "Next verification targets" #1).
- Does Dilip Rajeev's named logographic-vs-phonetic critique of Owens &
  Coleman (2014) have any engagement from a peer-reviewed or mainstream
  Aegean-script specialist, or does it stand only as one independent
  researcher's counter-claim? Still not established.
- New from this cycle: what does Yves Duhoux's actual peer-reviewed
  argument against Faucounau's decipherment say, beyond the WebSearch-
  snippet summary this pass could obtain? This is now the single highest-
  value unread source this project has identified — a real academic journal
  article (DOI 10.2307/507232), not a search-engine paraphrase — and would
  meaningfully strengthen the SQ-4 catalog's evidentiary chain if a future
  session can reach it directly.
- Is this session's broad network-egress block on academic/encyclopedic
  domains (WorldCat, Wikipedia, ResearchGate, Academia.edu, Persée,
  UCLouvain's repository, Hall of Maat, and others — confirmed blocked
  across three separate SQ-4 passes and roughly 15 distinct domains as of
  2026-09-25) a lasting policy or something that may lift? Not something
  this project can resolve itself; worth a light spot-check each future
  cycle rather than continued heavy re-testing.
