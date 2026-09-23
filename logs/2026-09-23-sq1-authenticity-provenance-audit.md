# SQ-1 authenticity/provenance audit — first pass

**Agent:** Claude (orchestrating session, not a delegated subagent — see note at bottom)
**Method:** live web search/fetch (WebSearch, WebFetch), not simulated. No files downloaded, no bulk data pulled, per this sidequest's standing rule.

## Discovery record

Discovered 3 July 1908 by Italian archaeologist Luigi Pernier during excavation of the Minoan palace site of Phaistos, Crete — confirmed consistently across [Wikipedia](https://en.wikipedia.org/wiki/Phaistos_Disc), the [Heraklion Archaeological Museum's own page](https://heraklionmuseum.gr/en/exhibit/the-phaistos-disc/), and multiple secondary sources.

**One discrepancy worth flagging, not silently resolved:** a National Geographic search snippet credited joint discovery to "Federico Halbherr and his student Luigi Pernier," while Wikipedia and the Heraklion Museum's own page credit Pernier alone (Halbherr was the site's excavation director and Pernier's supervisor, which may explain the attribution blending). Not independently resolved here — worth a follow-up primary-source check (e.g. Pernier's original 1908 excavation report) before treating either framing as settled.

## Physical facts

Per [Wikipedia](https://en.wikipedia.org/wiki/Phaistos_Disc) (direct fetch, not search-snippet inference):
- **242** total sign-impression occurrences (123 on side A, 119 on side B)
- **45** distinct sign types
- **61** word/sign-groups, divided by incised radial-stroke dividers (31 side A, 30 side B)

**Correction to the scaffold:** the scaffold (written from general background knowledge during bootstrap) used "241" throughout. Multiple secondary sources found in this pass (an inkl.com news piece, an ExplorersWeb article) also say "241." Wikipedia's own article states 242 as the sum of its own reported per-side counts (123+119). This is a genuine, citable disagreement between sources, not a typo on either side — recorded as such rather than silently picking one number. The 45 sign-type and 61 word-group figures are *not* disputed across any source checked.

## Dating

**Correction to the scaffold:** the scaffold's "commonly cited around 1700 BCE" framing understates how unsettled the dating actually is. Per Wikipedia's own article, published scholarly estimates span nearly 500 years and do not converge on a single figure:
- Yves Duhoux (1977): 1850–1600 BC (Middle Minoan III)
- Kristian Jeppesen (1963): after 1400 BC (Late Minoan II–III)
- Louis Godart (1990): anywhere within Middle or Late Minoan — i.e., most of the second millennium BC
- Jan Best: first half of the 14th century BC (Late Minoan IIIA)

This should replace the flat "~1700 BCE" framing in `README.md` and `knowledge-base/state.md` — see those files' updates in this same commit.

## Authenticity dispute — named, citable, and genuinely unresolved

This is the most substantive finding of this pass. The dispute has real names and a real, specific reason it remains unresolved rather than merely "some scholars disagree":

- **Jerome M. Eisenberg**, an antiquities dealer and editor of *Minerva* magazine, published a 2008 article in *Minerva* arguing the disc is a hoax perpetrated by Pernier himself — motivated, in Eisenberg's telling, by professional rivalry: Pernier, working at a site with comparatively few spectacular finds next to Arthur Evans' famous Knossos excavation, allegedly fabricated an untranslatable text (modeled on the genuinely ancient Etruscan Magliano Disc) to boost his own reputation. (Sources: [Wikipedia](https://en.wikipedia.org/wiki/Phaistos_Disc); a [languagehat.com](https://languagehat.com/phaistos-disc-a-forgery/) contemporaneous discussion thread; an academia.edu-hosted rebuttal paper.)
- **Pavol Hnila** (University of Berlin) published a rebuttal in 2009, arguing from Pernier's own personal letters that his conduct around the find was not consistent with a jealous forger's behavior, and separately noting that Sign 21 on the disc corresponds to a motif later found on a genuine, independently-excavated sealing — evidence favoring authenticity.
- **The decisive scientific test has never been run, by institutional choice, not oversight**: the Heraklion Archaeological Museum has declined to permit thermoluminescence dating (which could establish or rule out a firing date consistent with 1908 manufacture) specifically to avoid any risk of damage to the object, however slight. This means the authenticity question is not merely "debated" but **structurally undecidable by the most direct available method for the foreseeable future**, absent a change in museum policy.
- Mainstream/consensus position, per the sources checked: the disc "is now generally accepted by archaeologists as authentic," but this is a working consensus among specialists, not a scientifically closed question.

**Implication for this project, carried into Meeting #1 below:** this project should not wait for an authenticity resolution that institutional policy currently forecloses. Every downstream claim should carry the disclosed caveat that authenticity rests on scholarly consensus and indirect evidence (the sealing correspondence, Pernier's correspondence), not a direct physical dating test.

## Cretan Hieroglyphic resemblance

Confirmed via the [National Geographic piece](https://www.nationalgeographic.com/history/article/phaistos-clay-disk-minoans-mystery): some signs show *superficial* resemblance to specific Cretan Hieroglyphic signs — specifically a feathered-head sign and a bow-shaped sign are named as the clearest examples, with "one or two others" mentioned but not specified — but the resemblance is explicitly described as insufficient to establish the two scripts as the same writing system. This directly informs SQ-3's scope: there is a real, named, narrow starting point (two specific signs) rather than a vague "some scholars have noted resemblances."

## Holding institution

Confirmed: **Heraklion Archaeological Museum**, Crete, Greece, via the museum's own official page.

## Prior claimed decipherments (SQ-4 groundwork, done in parallel per this sidequest's own scope note)

Real, named, dated claims found via a dedicated [Wikipedia "Phaistos Disc decipherment claims" page](https://en.wikipedia.org/wiki/Phaistos_Disc_decipherment_claims):

| Proposer | Year | Claimed script/language | Claimed reading type |
|---|---|---|---|
| George Hempl | 1911 | Ionic Greek, syllabic | Religious/ritual hymn |
| F.M. Stawell | 1911 | Homeric Greek, syllabic | Religious invocation |
| Jean Faucounau | 1975 | Proto-Ionic Greek, syllabic | Funerary hymn |
| Vladimir Georgiev | 1976 | Hittite, syllabic | Unspecified |
| Steven R. Fischer | 1988 | A Greek dialect, syllabic | Linguistic text (unspecified genre) |
| Achterberg, Best, Enzler & Strous | 2004 | Luwian/Anatolian hieroglyphic | Land ownership document |
| Gareth Owens & John Coleman | 2014 | Minoan/Linear-tradition | Prayer to a goddess |
| Lozano | 2014 | — | Calendar reading |
| Andis Kaulins | — | — | Proof of a geometric theorem (in Greek) |
| Alan Butler | — | — | Astronomical calendar/calculating device |

**Discrepancy worth flagging:** an initial web-search snippet described the Achterberg/Best/Enzler/Strous (2004) proposal as a "prayer/hymn" reading; the dedicated Wikipedia decipherment-claims page instead describes it as a "land ownership document" claim. Not resolved here — the dedicated page is treated as the more authoritative of the two sources checked, but this should be verified against the actual 2004 publication before being cited with confidence.

General scholarly assessment, per the same source: "a large part of the claims are clearly pseudoscientific," and linguists are doubtful the inscription is even long enough (241/242 signs across 61 short word-groups) to be unambiguously interpretable at all — directly relevant to this project's own Open Question about what would even count as defensible evidence given the object's size. Gareth Owens's 2014 prayer reading specifically is noted as disputed by other Aegean-script specialists, not accepted as a solution.

## What remains unverified

- Pernier's original 1908 excavation documentation itself was not directly read (only secondary accounts of it) — a genuine primary-source gap.
- The exact wording/scope of the Achterberg et al. 2004 claim (prayer vs. land-ownership-document framing conflict, above).
- Whether any peer-reviewed source (rather than encyclopedia/blog coverage) has directly weighed Eisenberg's 2008 forgery argument against Hnila's 2009 rebuttal — both were found via secondary discussion, not read in primary journal form.

## Note on process

This work was originally assigned to a delegated background subagent, which correctly declined: its working directory was a `clambakesanta` git worktree, this machine's `C:\git\.session-project` scope-lock file was set to `voynich-collective`, and the task target was a third, unrelated repository (`phaistos-disc-collective`) — exactly the cross-project situation `C:\git\CLAUDE.md`'s scope guard exists to prevent, and a relayed task prompt correctly does not constitute the user's own chat authorization to cross it. The orchestrating session (this one) has that authorization directly, repeatedly, and explicitly from the user across this entire conversation, so this work was completed directly here instead of re-delegating into the same wall.
