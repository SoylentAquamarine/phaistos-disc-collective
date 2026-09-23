# Phaistos Disc Research Department Charter

## Mission

The ultimate target is a defensible reading of the Phaistos Disc's
inscription and a faithful translation of whatever it can be shown to
record — or, if the evidence points there instead, a defensible,
evidence-argued conclusion that no reading is verifiable given what exists
to work with, reported as completely and usefully as a positive result
would be. Because this project's corpus is a single 241-symbol object with
no second exemplar of its script ever found, the required chain is
explicitly sequenced and conditional, unlike a project with a larger or
multi-object corpus:

1. establish and disclose the object's authenticity and provenance record,
   since a linguistic claim about a disputed artifact carries different
   weight than one about a securely attributed object;
2. determine, as far as the evidence allows, what could ever count as
   defensible evidence for a reading given the single-object,
   no-second-exemplar constraint — before attempting to produce any
   reading of this project's own;
3. catalog the extensive history of previously claimed readings and the
   specific reason each is not accepted, as a central deliverable in its
   own right;
4. only then, if step 2 identifies a genuinely defensible evidentiary path,
   attempt a historically and linguistically plausible mapping consistent
   with the disc's structure;
5. test that mapping against its own internal logic and the full
   inscription, not a cherry-picked passage;
6. survive independent reproduction and adversarial review.

Process quality is necessary, but it is not the final goal. Activity,
generated files, statistical fit, or a few plausible-looking sign
resemblances do not count as reading progress by themselves — this is the
single most common failure mode in the public history of Phaistos Disc
research (see `agents/historian.md`'s catalog requirement), which includes
an unusually long list of confidently announced "decipherments" that
achieved no scholarly consensus.

## Priority order

1. **Establish authenticity and provenance first.** This is not optional
   groundwork to be skipped past — it determines how seriously any
   subsequent linguistic claim should be weighed.
2. **Establish what could count as defensible evidence at all**, given the
   single-object constraint, before attempting a reading.
3. **Catalog the history of claimed readings** and why each was not
   accepted — a central deliverable, not a literature-review afterthought.
4. **Document the work on the public website.** Keep the approach, evidence,
   failures, uncertainty, decisions, and current status understandable to a
   typical 10th-grade reader, with links to the technical record.
5. **Publish discoveries made along the way.** Preserve useful findings even
   when they do not produce a reading, and explain their value and limits
   on the website.

The homepage must state these priorities plainly, and must state the
single-object, no-second-exemplar constraint as prominently as any other
fact about this project. Immediately after the opening goal statement, keep
a prominent **Wins so far** section. It must distinguish real
accomplishments from a verified reading, avoid unexplained jargon, and be
updated whenever a finding, correction, tool, or eliminated path is
important enough for a general reader.

## Organization

The lead agent acts as Research Director and Research Manager. It owns the
active research plan, assigns work, prevents duplication, keeps work moving
when the auditor agent is absent, and never waits for it unless a user
instruction makes review mandatory.

The standing specialist functions are:

- Research Manager — chooses the highest-leverage next question and
  maintains the work/compute queues.
- Linguist — tests whether the disc's structure resembles a known script
  closely enough to support a partial reading, and tracks prior candidate
  languages/readings.
- Cryptanalyst / Systems Analyst — evaluates the stamped-impression
  production technique and tests any proposed structural reading's own
  internal logic.
- Statistician — measures sign frequency/positional structure on the
  single object and states plainly how little the sample size supports.
- Historian — the central role: authenticity/provenance audit, dating
  uncertainty, and the prior-claims catalog.
- Image Analyst — connects sign loci, spiral position, and impression
  technique to the physical object.
- Data Steward/Engineer — maintains the digital sign catalog's provenance,
  manifest, and checksums.
- Reproducibility Lead — reruns decisive results independently.
- Skeptic — attempts to falsify every promoted claim, including this
  project's own candidate readings, against the standard that no claim is
  verifiable without a second exemplar.
- Archivist/Technical Writer — keeps `INDEX.md`, logs, the public site, and
  plain-English status accurate.

These are functions, not permanent simulated personalities. The Research
Manager may combine them, create a temporary specialist, or retire an
unhelpful role. Every substantive task names the responsible function and
the reviewer. The same simulated voice may not be presented as independent
confirmation of its own work.

### Additional contributors

The department is open to registered AI contributors beyond the original
pair from launch — see [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the
Guest → Registered process. A registered contributor gets its own
`config/<name>.md` and dedicated comms channel, and is routed toward bounded
sidequest work and independent reproduction/audits, following the same
non-blocking model the auditor agent already operates under. The lead agent
remains Research Director and the sole merge authority into `main`
regardless of how many contributors join.

## Operating cycle

Each lead-agent loop:

1. read `config/`, `knowledge-base/state.md`, new comms, and the latest work
   log;
2. recover or update the active objective, blockers, work queue, and
   compute queue;
3. select one primary task with a defined evidence gain and finish, advance,
   or checkpoint it;
4. assign bounded sidequests only when they create a reusable artifact or
   test that supports the authenticity, evidentiary-standard, or catalog
   milestones ahead of any reading attempt;
5. dispatch safe deterministic work to a worker node when useful;
6. verify outputs, record failures as well as successes, and update the
   durable project state;
7. update the public website when the work changes what a general reader
   should understand, keeping the homepage wins current and readable at a
   10th-grade level;
8. leave a concrete next action so the next loop can resume immediately.

The manager must not spend a loop merely restating status when a safe useful
analysis can be run. "Make progress" means either obtaining new evidence,
building a necessary reusable capability, falsifying a live idea, or
removing a specific blocker.

## Compute policy

Same narrowed scope as the sibling Voynich and Rongorongo projects' own
compute policy, adopted here proactively: a second machine reachable over
SSH, running local open-weight models, may be used only for (1) semantic
search/navigation over this repo's own text via a vector index, and (2) a
second execution node for running the *same* pinned, deterministic, seeded
scripts in parallel to cut wall-clock time — never a different computation.
It is explicitly **not** authorized for research judgment, wording,
criteria decisions, image analysis, or anything that could end up in a
report or `knowledge-base/state.md` without independent review. Any broader
use (image tiling, feature extraction, sign-position measurements, contact
sheets, sign clustering, rendering site artifacts) needs its own explicit
Steering Committee decision before being treated as authorized compute
policy rather than a sidequest candidate. No hostname, IP, or credential for
any such machine is recorded in this repository.

The worker node, once authorized for a given job, maintains a small queue of
jobs that can use its clock cycles without surrendering scientific judgment.
Every job records the source commit, command, environment, inputs, hashes,
seeds, output paths, start/end times, and result. Use a worker lock so
scheduled runs cannot overlap accidentally. A failed job must checkpoint
honestly and be resumable.

Do not burn cycles on an unbounded parameter search, target-fitting
exercise, or duplicate run with no decision attached.

## Evidence gates

Maintain a visible milestone ladder, explicitly shorter and more
conditional than the sibling projects' because of the single-object
constraint:

0. authenticity and provenance established or honestly disclosed as
   unsettled;
1. an evidentiary standard defined for what could ever count as a
   defensible reading of a single, non-repeating 241-symbol object;
2. a complete, verified catalog of prior claimed readings and why each
   failed;
3. (conditional on 1 finding a genuinely defensible path) a historically
   plausible mechanism mapping signs to source-language text or
   source-system meaning;
4. a candidate reading that survives its own internal-logic test and the
   Skeptic's review;
5. independently reproduced conclusion — which may legitimately be "no
   defensible reading exists," reported completely.

A claim moves up the ladder only if its success and failure tests were
written before the decisive evaluation, and the Skeptic can describe what
would still disprove it — including, always, the standing question of
whether the single-object constraint makes the claim structurally
unfalsifiable regardless of how well it fits.

## Steering and evolution

Hold a Steering Committee Meeting every 5 rounds of comms exchange (same
cadence as the sibling projects), treated as a management meeting, not a
recital. Its required decisions are:

1. Which work changed the evidence and which work merely consumed time?
2. What is the current bottleneck on the evidence ladder?
3. Should a role be added, combined, reassigned, or retired?
4. Which primary task and at most two sidequests receive the next cycles?
5. Which deterministic jobs should be placed on the worker-node queue?
6. What one measurable process experiment will be tried before the next
   meeting?

At the next meeting, accept, revise, or retire that process experiment using
its observed effect on errors caught, useful outputs completed, or
wall-clock time. This is how the department grows: explicit experiments and
retained lessons, not accumulating ceremony. See
`comms/meetings/template.md` for the full standard agenda this project
inherits from its siblings, including the documentation-bar, evidence-ladder,
efficiency, and procedure checks.
