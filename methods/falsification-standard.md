# Falsification and Promotion Standard

This is the minimum bar for moving an interpretation into **Active
Hypotheses**. It is deliberately stricter than the bar for recording a
measurement in **Confirmed Findings**. A measurement can be reliable while
supporting several incompatible explanations — and on this project's
single-object corpus, that gap between "reliable measurement" and
"defensible interpretation" is wider than in any sibling project.

## Minimum bar for Confirmed Findings

Confirmed Findings is a much lower bar than Active Hypotheses — a
measurement or result, not an interpretation, and it doesn't need
alternatives explicitly ruled out. But every entry should still be well
documented and reproducible, not left to habit. Before a PR adds a bullet
to `knowledge-base/state.md`'s Confirmed Findings, it should have:

- a script, a manifest, or a directly-read and cited image/text protocol
  that produced the number or claim — not a description of a result
  alone, with nothing behind it a reader could rerun;
- the actual output (a summary JSON, a report, or both) committed to the
  repo, not only quoted or paraphrased inline in the bullet;
- enough provenance (source commit, checksum, seed, sample definition)
  that a third party could rerun it and reasonably expect the same
  result;
- for anything resting on an external secondary source (a search-engine
  summary, a paper or catalog not read directly), an explicit disclosure
  of that limitation in the same entry — never presented as if it were
  independently verified when it wasn't. This applies with particular
  force here: much of what is "commonly cited" about the Phaistos Disc in
  casual secondary sources (sign-impression counts, sign-type counts,
  word-group counts, dating, authenticity, and specific decipherment
  claims all vary by source or are contested in the primary scholarly
  literature), so a claim's provenance chain matters more than usual.

This does not require independent adversarial review the way Active
Hypotheses does — that remains the harder bar. It requires that a
Confirmed Finding always be *checkable*, even when no one has checked it
yet.

## Required hypothesis card

Before running its decisive test, the proponent must record:

1. **Claim** — one operational statement narrow enough to fail.
2. **Alternatives** — at least the strongest rival reading(s) already
   catalogued under SQ-4, and a reason each is not equally consistent with
   the same observation, or a reason a given alternative family is
   inapplicable.
3. **Discriminating prediction** — an outcome expected under the claim and
   not equally expected under the named alternatives.
4. **Failure condition** — a numerical threshold, internal-consistency
   mismatch, or catalog mismatch that would count against the claim. This
   may not be invented after seeing the result.
5. **Units and controls** — the faces, spiral positions, word-groups, sign
   types, and comparison corpora (e.g. Cretan Hieroglyphic) used, and any
   exclusions.
6. **Dependencies** — sign-catalog identity, position/sequence
   segmentation, and word-group-boundary assumptions that could
   manufacture the result.
7. **The single-exemplar statement, mandatory for this project only** —
   an explicit statement of what, if anything, could ever distinguish this
   claim from an equally plausible rival reading, given that no second
   object bearing the same script exists anywhere to test generalization
   against. If the honest answer is "nothing could," the hypothesis card
   must say so and may not proceed to promotion.

## Evidence required for promotion

A candidate can enter **Active Hypotheses** only when all of the following
are present:

- a reproducible script or a cited, inspectable image/catalog protocol;
- an effect size and uncertainty or an equally explicit qualitative
  decision rule, not only a p-value — with explicit acknowledgment of how
  little a sample of 241 sign-impressions and 45 sign types can support;
- a negative or shuffled control appropriate to the claim;
- sensitivity to at least the material sign-catalog/segmentation and
  word-group-boundary confounds identified in the hypothesis card;
- a test against the *entire* inscription, not a cherry-picked passage —
  the single most common, specific, and publicly documented failure mode
  in the history of Phaistos Disc decipherment claims;
- independent adversarial review by the other collaborator, including
  reproduction of the headline result or a documented reason reproduction
  is impossible;
- a statement of what the result does **not** distinguish, given the
  no-second-exemplar constraint.

Promotion means "worth sustained falsification," not "probably deciphered."
Confirmation requires surviving the Skeptic's targeted test and explaining
evidence that the strongest alternative does not explain equally well —
including every applicable claim already catalogued under SQ-4.

## Automatic stop conditions

Do not promote when any of these applies:

- the observation was selected after inspecting the same material with no
  holdout, or (since no genuine holdout is possible on a single object) no
  attempt was made to test against a portion of the inscription not used
  to construct the reading;
- the effect disappears under one reasonable sign-catalog or word-group
  segmentation policy;
- the proposed mechanism has enough unconstrained choices to fit
  arbitrary sequences — a specific, well-documented risk given only 45
  sign types to assign values to;
- the result only restates a known property of the object (e.g. the
  spiral layout or the incised dividers) without a prediction that
  separates mechanisms;
- an upstream correction has not been propagated through the full
  dependent analysis chain;
- the claim rests on matching a handful of signs to a story or reading
  without addressing the full inscription — the specific, publicly
  documented failure mode behind nearly every prior claimed decipherment
  of this object, catalogued under SQ-4;
- the hypothesis card's required single-exemplar statement (item 7 above)
  says nothing could distinguish the claim from a rival reading, yet the
  claim is proposed for promotion anyway.

## Current consequence

At launch, the repository has no Confirmed Findings and no Active
Hypotheses — this is a genuine bootstrap state, not a placeholder awaiting
cleanup. The first substantive work is the authenticity and provenance
audit (`config/sidequests.md`, SQ-1), which is itself infrastructure, not
a finding. Given this project's single-object, no-second-exemplar
constraint, it should be treated as a live, real possibility — not a
failure mode to be talked around — that this project's most rigorous,
final output is a fully-documented conclusion that no candidate reading
can meet this standard, rather than a promoted Active Hypothesis.
