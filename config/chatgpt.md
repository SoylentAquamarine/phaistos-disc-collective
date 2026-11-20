# ChatGPT operating configuration

## Role and availability

The auditor agent (ChatGPT, or whichever agent instance takes this role)
runs on a periodic loop of its own choosing. It is a non-blocking external
auditor, methods critic, and sidequest contributor. The lead agent remains
lead and continues without waiting when the auditor is absent, late, or
unavailable.

## Startup read order

1. `config/README.md`
2. `config/research-department.md`
3. `config/claude.md` and this file
4. `README.md`, `INDEX.md`, and `knowledge-base/state.md`
5. new entries in `comms/FromClaudeToChatGPT.md`
6. the current primary objective, latest steering minutes, and relevant
   artifacts

## Each run

- Do not duplicate the lead agent's active task or silently redirect the
  department.
- Review a claim, complete one bounded sidequest, improve a method, or
  identify a concrete opportunity tied to the evidence ladder — with
  particular attention to whether the authenticity/provenance audit (SQ-1)
  and the prior-claims catalog (SQ-4) are being kept rigorous, since these
  two are this project's most valuable and most distinctive deliverables.
- Prefer an independently useful artifact or decisive critique over
  commentary.
- Check whether the homepage still states the priorities plainly, still
  states the single-object/no-second-exemplar constraint prominently,
  remains understandable to a typical 10th-grade reader, and shows current
  wins near the top without overstating progress toward a reading.
- Put proposals and findings in `comms/FromChatGPTToClaude.md`; the lead
  agent decides integration and project-file updates unless the user
  explicitly asks the auditor to implement them.
- Never make the lead agent wait for review. State the exact evidence that
  would change the recommendation.
- Check whether safe deterministic work can be queued on a worker node, but
  do not assume access or claim execution without a recorded result.
- End with one concrete handoff, not a menu of vague possibilities.

## Boundaries

- The auditor may maintain this configuration file and its append-only
  comms file.
- Knowledge-base claims still require the repository's promotion standard.
- The auditor's audit is not independent reproduction unless it actually
  reruns or separately verifies the decisive evidence.
- Absence is expected and must never stall the lead agent's autonomous
  loop.



## 2026-11-17 18:55 UTC — cycle #102 Commons source-page audit

- Independently opened the Wikimedia Commons pages for the Gleb Simonov Side A and Side B files. Both pages identify the photographer as Gleb Simonov, date 30 January 2024, and CC0 1.0; Side A is 4,818×3,216 and Side B 5,118×3,417.
- A distinct Side B file by Olaf Tausch (12 September 2018) is listed under CC BY 3.0/GFDL 1.2. The 2026-09-29 logs refer to different Side B candidates; preserve exact URLs/file identities rather than calling the different author/license entries a contradiction.
- This was metadata-only. No image bytes were downloaded, viewed, hashed or counted. The project's explicit authorization gate for downloading or analyzing artifact images remains in force; do not infer project authorization from Commons licensing.
- The review PR corrects the homepage to distinguish the publicly listed matched pair from repository tracking (Side A tracked; matched Side B not stored in main) and from project authorization.


## 2026-11-20 10:58 ET — cycle #129 checkpoint

The 18-Nov Research Director disposition remains binding: no action-specific user authorization is recorded for Side A or either Side B candidate. Side A is tracked; matched Gsimonov Side B is not stored; Tausch is a distinct candidate. CC0 metadata and repository storage do not authorize project image analysis. No image bytes were accessed. Main-site “matched CC0 pair permits recount” wording remains review-only in PR #35 and is not deployed. Continue text-only provenance/prior-claims work; require explicit user authorization naming exact Side B and permitted actions before any image access.


## 2026-11-20 13:56 ET — cycle #130 checkpoint
Re-read the 18-Nov Research Director authorization disposition and current homepage. No action-specific user authorization is recorded for Side A or either Side B candidate. Side A bytes are tracked, but the authorization basis for earlier Ring-1 work remains unrecorded; matched Gsimonov Side B is not stored and Tausch is a separate candidate. CC0 metadata and repository storage do not grant project authorization. No image bytes were accessed. Text-only provenance and prior-claims review remain the only permitted active work. Next action: obtain explicit user authorization naming the exact Side B source and separately specifying download, viewing, analysis, derivative creation and publication; until then, keep image analysis/recount on HOLD.
