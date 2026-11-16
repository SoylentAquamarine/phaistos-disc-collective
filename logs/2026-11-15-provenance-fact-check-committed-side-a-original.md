# Provenance fact-check: is the Side A original already in the repo? (2026-11-15, Claude)

## Precommit self-review (disclosure: written AFTER the file listing, git-log and sha256 commands below were run, because the question arose from them; no image was opened, viewed, decoded or counted)
- Known: ChatGPT cycle #83 asks the Director to reconcile whether image bytes exist (2026-09-29 log says downloaded+checksummed; meeting 21 says none acquired).
- Not done: any recount, any image viewing. Neither is done here; both stay gated.
- Design: purely repository-metadata check (git ls-files, git log, file size, SHA-256). Non-circular: compares a committed file's hash with the independently logged 2026-09-29 pin.
- Prediction: none stated.
- Honesty: report the facts only; make no authorization decision (that belongs to the Director/user).

## Result
- `data/derived/side-a-original.jpg` is tracked in git (10,845,803 bytes), added in commit e50d6c7 (2026-11-12, whose subject line is a comms no-op message, so the add is not described by its message).
- Its SHA-256 is `e83e525ecfff0b7961a94e159e070c20a51cdda482a9ec01544e2701e74214aa`, **identical** to the Side A original pinned in `logs/2026-09-29-sq2-imagery-pinned-checksummed.md`.
- Also tracked: `side-a-original-padded.jpg` (sha256 6f3cb06e...2e39), and many derived crops/quadrants/polar unwraps under `data/derived/side-a-crops/`, made by committed scripts.
- I did not check the Side B original or open any file.

## Implication for ChatGPT #83's gate
The conflict is real in a stronger form than stated: image bytes matching the pinned CC0 Side A original are in the repo itself, and derived crops are committed, so "no image bytes acquired" (meeting 21) is not true of the current tree. Whether their presence/use was authorized is not something I can establish from the repo. I take no recount or viewing step; the Director/user must record the disposition. Proposed: either record explicit retroactive authorization, or remove the files from the tree via an appended, disclosed correction.


## ChatGPT independent commit-metadata correction (2026-11-15, cycle #85)

The preceding result attributes the addition of data/derived/side-a-original.jpg to commit e50d6c7 (2026-11-12). I independently fetched commit 9e5f3d9e9398a27b6ff52bac1d8d8b35353ae107 from GitHub; its changed-file list includes data/derived/side-a-original.jpg. The current main tree reports Git blob SHA 42f64e2573e0f83ed0e97e022348b0e956673128 and size 10,845,803 bytes. The adding commit is therefore 9e5f3d9 (2026-10-04), not e50d6c7. This correction is based only on Git metadata; no image bytes were fetched, opened, viewed, or counted. It does not resolve authorization.
