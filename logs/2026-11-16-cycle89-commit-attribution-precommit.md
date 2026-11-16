# Precommit: which commit added side-a-original.jpg (cycle #89 claim)
Date: 2026-11-16. Written BEFORE running git.
- Known: my 2026-11-15 fact-check named e50d6c7 as the adding commit; ChatGPT #89 says it was 9e5f3d9 (2026-10-04) and e50d6c7 only touched comms.
- Design: `git log --diff-filter=A --follow --format=... -- data/derived/side-a-original.jpg` plus `git show --stat e50d6c7`. Metadata only: no image bytes opened, viewed or hashed (authorization is a Director decision).
- Prediction: ChatGPT is right and my earlier attribution was wrong.
- Honesty precommitment: report verbatim; if my earlier text was wrong, append a disclosed correction, not an overwrite.
