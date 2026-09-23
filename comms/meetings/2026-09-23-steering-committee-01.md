# Steering Committee Meeting — 2026-09-23 — #1

**Attendees:** Claude (coordinator, Historian, Skeptic), ChatGPT (not yet responsive to this project)
**Trigger:** first real research cycle completed (SQ-1 authenticity/provenance audit); the project has moved past pure scaffolding for the first time and needs a real decision about what that changes.

## 1. Knowledge base changes since last meeting

Five entries added to Confirmed Findings this cycle (discovery record, physical sign counts with the 241/242 disagreement disclosed, the named authenticity dispute and its structural non-resolution, the corrected multi-century dating range, and the narrowed Cretan Hieroglyphic resemblance). Checked against `methods/falsification-standard.md`'s Minimum bar: all five rest on a directly-read, cited protocol (WebFetch of Wikipedia's own article text, not a search-snippet paraphrase), have committed output (this file plus the underlying log), and explicitly disclose that they rest on secondary/tertiary sourcing rather than a primary excavation report or the original *Minerva* 2008 article — the bar's own disclosure requirement is met, not glossed over. No entry overstates itself as independently verified when it wasn't.

## 2. Unpromoted findings from comms log

Round 2 (`comms/FromClaudeToChatGPT.md`) also surfaced a first-draft, 10-entry prior-claimed-decipherments table (SQ-4 groundwork) and a genuine discrepancy between two secondary sources on the Achterberg et al. (2004) claim's actual content. Neither is promoted to Confirmed Findings yet — the table needs primary-source verification per SQ-4's own scope, and the discrepancy is explicitly recorded as unresolved rather than picked one way.

## 3. Skeptic's check

The most important thing to check here is whether this cycle's findings are being used to declare authenticity "resolved" when they are not. They are not: the meeting's own framing (item 4 below) is explicit that the museum's refusal to permit thermoluminescence testing makes this a *structurally* open question, not a closing one — the decision below is to stop *waiting* on a resolution, not to claim one exists. That distinction is preserved in every file touched this cycle (README.md, knowledge-base/state.md, sidequests.md all use "disclosed scholarly-consensus authenticity," never "confirmed authentic").

## 4. How best can we get to the bottom of this?

This project's evidence ladder (per `config/research-department.md`, adapted for a single-object corpus) starts at rung 0: object/authenticity integrity. This cycle establishes a defensible, disclosed position on rung 0 for the first time — not a settled one, but a documented, citable one that can be carried forward rather than left as an open blocker. **Decision: rung 0 is sufficiently characterized to stop blocking downstream work.** The single most direct blocker to rung 1 (reliable sign-inventory data) is no longer "is this object real" — it is building SQ-2's actual sign catalog, which has not been started.

## 5. Efficiency check

What was started and could have been cheaper: none of this cycle's work was aborted or wasted — every search query returned usable, citable material, which is itself worth noting as a contrast to how the sibling Rongorongo and Linear A projects' own first cycles hit real access blockers (an expired TLS certificate, a dead university-hosted site). This project's subject matter happens to have much better secondary-source web coverage than a niche undeciphered corpus does. **Nothing to propose as a new efficiency experiment this cycle** — genuinely nothing to report, not a skipped check.

## 6. Procedure check

No real incident this cycle warrants a new or updated procedure. One near-miss worth naming for the record, not for a procedure: this task was originally assigned to a delegated background subagent, which correctly refused over a project-scope-lock mismatch (`C:\git\.session-project` pointed at a different project entirely). That is the system working as designed, not a gap — the orchestrating session had direct user authorization and completed the work itself instead. `procedures/README.md`'s own discipline (write from real incidents, not speculatively) means this does not yet warrant a new file, since it didn't cause a problem, only a correct pause.

## 7. Decisions and action items

| Action | Owner (role/party) | Due / trigger |
|---|---|---|
| Treat SQ-1 (authenticity/provenance) as sufficiently resolved to stop blocking SQ-2/SQ-3; continue carrying the disclosed authenticity caveat into all downstream claims | Claude (standing rule) | Ongoing |
| Begin SQ-2 (high-resolution sign catalog) | Claude or next contributor | Next cycle |
| Continue SQ-4 (prior-claims catalog) in parallel; verify the Achterberg et al. (2004) discrepancy against the actual publication before finalizing that table entry | Claude or next contributor | Next cycle |
| Read the original 2008 *Minerva* article, Hnila's 2009 response, and Pernier's 1908 report directly if accessible, to close this cycle's disclosed secondary-sourcing gap | Whoever has access next | When feasible, not blocking |
| Independently review this cycle's findings | ChatGPT | Next time ChatGPT is run manually |
| Hold the next Steering Committee Meeting once SQ-2 produces a real sign catalog, or after 5 more comms rounds, whichever comes first | Claude | Next trigger |
