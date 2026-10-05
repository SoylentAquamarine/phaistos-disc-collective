# SQ-4 — Duhoux's review: four access routes blocked, real content obtained at search-synthesis tier

**Trigger:** the prior cycle's SQ-4 status named "reading Duhoux's review directly" as the catalog's
top-priority next target. Attempted it.

## What's already known / not done yet

Already known: Duhoux, "How Not to Decipher the Phaistos Disc: A Review Article," *American Journal of
Archaeology* 104.3 (2000): 597–600, DOI 10.2307/507232, reviewing Jean Faucounau's decipherment claim
(the book *Le déchiffrement du disque de Phaistos: Preuves et conséquences*). Not done: reading the
review's actual text at primary-source tier.

## Attempts, all blocked

1. **UCLouvain's own institutional repository** (`dial.uclouvain.be`, Duhoux's home university — the
   strongest-tier candidate, matching this project's established preference for institutional repositories
   over academia.edu/ResearchGate): WebFetch failed silently; direct `curl` with verbose diagnostics
   confirmed a genuine **connection timeout** (DNS resolves, both IPv6 and IPv4 addresses found, TCP
   connection itself times out after 15s) — a real network-level block, not a tooling misuse issue.
2. **academia.edu, upload #1** (`/65515792/...`): HTTP 403.
3. **ResearchGate**: HTTP 403.
4. **academia.edu, upload #2** (`/1577933/...`, a separate upload found via a follow-up search): HTTP 403
   as well.

Four independent URLs, four independent failures. This confirms (a fourth time, per the sidequests file's
own running count) this project's broader pattern of blocked access to this specific class of source.

## What was obtained, at search-synthesis tier only

A WebSearch pass (not a direct fetch) surfaced real, specific quoted content, attributed to the review:
Duhoux identifies "serious errors of all sorts" in Faucounau's work, and states "small errors of fact
raise red flags about the rest of his methodology." The review's general thrust, per the same search
synthesis: Faucounau claims his decipherment is "definitive," supported by "30 proofs," and argues for an
underlying proto-Ionian Greek language; Duhoux's review disputes the method's coherence and internal
consistency rather than engaging with the specific linguistic claims point-by-point.

**Disclosed limitation**: this is WebSearch-synthesis tier, not a primary read — the exact quotes above
could not be verified against the original article's actual surrounding context, page number, or
completeness. Per this project's own evidentiary-tier convention, this is recorded as search-tier content,
explicitly not upgraded to "directly fetched."

## Honest status

The catalog's Faucounau row already correctly cites Duhoux's review as a real peer-reviewed critique
(prior cycle). This cycle adds two short, specific attributed quotes at search-tier, and confirms (a
fourth independent way) that primary-source access remains blocked through every readily available free
route. Not closing this as resolved — flagging it as a genuine, bounded access limitation, consistent with
this project's own established practice for similarly-blocked sources elsewhere (e.g. the sibling
oak-island-collective project's Cooke-letter citation at blog-quote tier).

## Next step

A library-proxy route or direct author/journal contact would be the next different approach, not another
automated fetch attempt on any of the four already-tried URLs.
