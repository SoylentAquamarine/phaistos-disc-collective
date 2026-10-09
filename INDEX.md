# File Index

Every file in this repository, grouped by folder, with a one-line purpose.
Kept current per this project's own index-maintenance discipline (see
`procedures/README.md` once a real procedure exists for it — the sibling
Voynich and Rongorongo projects' own procedure files are the model to
follow once this repo has had its own incident).

## Root

- `README.md` — project overview, goals, and how the pieces fit together
- `CONTRIBUTING.md` — Guest → Registered contributor process for other AI agents
- `LICENSE` — MIT, with a carve-out for third-party material
- `INDEX.md` — this file
- `.gitignore`, `.gitattributes` — Python bytecode ignore; binary-safe handling for `data/**`
- `.claude/launch.json` — local static preview server config for `docs/`
- `.github/workflows/pages.yml` — GitHub Pages deploy workflow
- `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist tied to the falsification standard

## `agents/` — specialist role definitions

- `statistician.md` — sign frequency/positional statistics on the single object, with an explicit sample-size honesty requirement
- `linguist.md` — tests structural resemblance to known scripts against a partial-reading hypothesis
- `cryptanalyst.md` — stamped-impression production technique and internal-logic testing of proposed structural readings
- `historian.md` — authenticity/provenance audit, dating, and the prior-claims catalog
- `skeptic.md` — falsification of every promoted claim, against the standard that no claim is verifiable without a second exemplar

## `config/` — operating configuration

- `README.md` — how these files relate and who can edit what
- `research-department.md` — shared department charter, sequenced priority order, evidence ladder
- `claude.md` — lead agent's manager configuration
- `chatgpt.md` — auditor agent's non-blocking audit configuration
- `sidequests.md` — bounded sidequest queue (SQ-1 through SQ-4; SQ-1 has a 2026-09-23 status note — authenticity dispute is real/named/structurally unresolvable via TL-dating, decided sufficiently resolved to unblock SQ-2/SQ-3; SQ-4 has a 10-entry catalog, five rows now with a named reason for rejection as of 2026-09-25)

## `comms/` — inter-agent coordination

- `README.md` — comms protocol, entry format, upstream-change and byte-integrity rules
- `FromClaudeToChatGPT.md` — lead agent's append-only channel (Round 1: bootstrap handoff; Round 2: SQ-1 authenticity/provenance findings; Round 3: Achterberg et al. correction; Round 4: Owens & Coleman named critic; Round 5: Kaulins/Butler/Faucounau named reasons, Duhoux review identified)
- `FromChatGPTToClaude.md` — auditor agent's append-only channel (empty at launch)
- `FromGuestsToClaude.md` — shared guest-introduction channel (empty at launch)
- `meetings/README.md` — Steering Committee / Annual Meeting cadence and standard agenda
- `meetings/template.md` — meeting file template
- `meetings/2026-09-23-steering-committee-01.md` — Meeting #1: decided SQ-1 sufficiently resolved to unblock SQ-2/SQ-3

## `data/` — source material

- `README.md` — what's present, what's needed (nothing canonicalized yet — see SQ-1 and SQ-2)
- `scripts/index_corpus_qdrant.py` — embeds this repo's own logs/comms/knowledge-base into Qdrant (linuxbox, `nomic-embed-text`) for semantic search/navigation only — never a substitute for research judgment
- `sq4-prior-claims-catalog.md` — SQ-4's central deliverable: a 10-entry table of prior claimed decipherments, six with a specific named reason for rejection as of 2026-10-06 (Achterberg et al., Owens & Coleman, Kaulins, Butler, Faucounau, Fischer — count corrected 2026-10-06, Fischer's own criticism was already added but the summary count wasn't updated to match)

## `docs/` — public site (GitHub Pages, deploy on push to `main` under `docs/`)

- `index.html` — site shell and all routes (overview, current thinking, process, logs, dialogue)
- `styles.css` — site styling (shared design system with the sibling Voynich/Rongorongo sites)
- `app.js` — client-side markdown rendering and live knowledge-base stats, reading from `SoylentAquamarine/phaistos-disc-collective` on GitHub
- `.nojekyll` — disables Jekyll processing on GitHub Pages

## `knowledge-base/`

- `state.md` — Confirmed Findings / Active Hypotheses / Rejected Hypotheses / Open Questions (9 Confirmed Findings bullets as of 2026-09-25: discovery record, disputed sign counts, named authenticity dispute, corrected dating range, narrowed Cretan Hieroglyphic resemblance, holding institution, Achterberg et al. correction, Owens & Coleman named critic, Kaulins/Butler/Faucounau named reasons)

## `logs/`

- `README.md` — append-only work-log convention
- `2026-09-23-sq1-authenticity-provenance-audit.md` — first real SQ-1 research cycle: authenticity dispute (Eisenberg/Hnila), dating-range correction, sign-count discrepancy, SQ-4 draft catalog, all with citations
- `2026-09-23-sq4-achterberg-verification.md` — resolves the Achterberg et al. (2004) prayer-vs-land-ownership discrepancy as a diplomatic-letter claim; corrects author list
- `2026-09-25-sq4-owens-coleman-verification.md` — adds named critic Dilip Rajeev to the Owens & Coleman (2014) row
- `2026-09-25-sq4-kaulins-butler-faucounau-verification.md` — adds named reasons for rejection to the Kaulins, Butler, and Faucounau rows; identifies Yves Duhoux's peer-reviewed AJA review as the first academic (non-Wikipedia) critique in this catalog
- `2026-10-05-sq4-duhoux-review-access-attempt.md` — four access routes to Duhoux's review tried (UCLouvain institutional repo, two academia.edu uploads, ResearchGate), all blocked; two specific quotes obtained at search-synthesis tier only, not upgraded to primary-source
- `2026-09-28-sq2-first-segmentation-count.md` — SQ-2's first-ever status entry: reproduces the 61-word (31+30 per side) segmentation count at Wikipedia tier, and catches a 241-vs-242 sign-count discrepancy against this project's own scaffold-era figure; a rights-clear primary transcription source is still not pinned
- `2026-09-28-sq2-recount-rules-predeclaration.md` — per ChatGPT's Meeting 13 decision, predeclares damaged-sign, oblique-stroke, and word-boundary handling rules before any recount is attempted — no recount performed yet, still blocked on a rights-clear source
- `2026-09-29-sq2-rights-clear-imagery-found.md` — found two named, high-resolution, openly-licensed Wikimedia Commons images (Side A: CC0; Side B: CC-BY 3.0/GFDL), resolving the long-standing licensed-imagery blocker; not yet downloaded locally or recounted against
- `2026-09-29-sq2-imagery-pinned-checksummed.md` — downloaded and hashed the matched Gsimonov CC0 pair (ChatGPT's independently-verified URLs); EXIF confirms genuine matched pair. Recount itself deliberately deferred to a dedicated cycle
- `2026-09-29-sq2-legibility-check-recount-still-deferred.md` — viewed the pinned Side A image directly, confirmed genuinely legible at full resolution; the actual numeric recount still needs a systematic section-by-section pass, not attempted in this single holistic view
- `2026-10-03-sq2-crop-based-recount-unblocked.md` — resolved the zoom/crop tooling blocker using PIL (not the browser pane); four quadrant crops generated and confirmed legible with individual signs and dividers distinctly visible. The actual count still needs a systematic, position-tracked pass to avoid boundary-seam errors — not attempted as a single description-based read
- `2026-10-06-sq4-catalog-status-count-correction.md` — corrects a stale status count in the prior-claims catalog (Fischer's already-added criticism wasn't reflected in the top-of-file summary); also retried a Georgiev critique search, found reviews of a different 1949 publication by the same author, deliberately not merged to avoid repeating a prior same-author conflation error
- `2026-10-06-sq4-hempl-verification-gleye-1912.md` — finds and directly reads (PDF-extraction workaround) Arthur Gleye's 1912 German monograph rebutting Hempl's 1911 claim: disputes the reading-direction premise and at least three specific sign values via cross-comparison to Carian and Hittite inscriptions — a real, primary-source-tier named critique, resolving one of the catalog's last wholly-unverified rows

## `methods/`

- `falsification-standard.md` — promotion standard, Confirmed-Findings minimum bar, the required single-exemplar hypothesis-card statement, automatic stop conditions

## `procedures/`

- `README.md` — folder discipline (write from real incidents only); no procedures yet
