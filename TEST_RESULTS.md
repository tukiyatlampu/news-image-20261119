# TEST_RESULTS — news-image-20261119

Run 2026-11-20 (WIB), clean-directory QA before GitHub push.

## Determinism (two runs, same bytes)

- Command: `python3 main.py` (twice, from a clean copy of the package)
- Run 1 sha256: `2f0f3c91ef382b2562f990fedfda4a69e2f829cc24d10cb2dc1f0bd70df1045f`
- Run 2 sha256: `2f0f3c91ef382b2562f990fedfda4a69e2f829cc24d10cb2dc1f0bd70df1045f`
- Result: identical — PASS

## Gate (PNG, size)

- Output: `/output/entry.png`, 1024x1024, RGB, 194,634 bytes (0.19 MiB)
- Limits: at most 1024x1024, at most 1,048,576 bytes — PASS

## Poster build

- Command: `python3 build_poster.py`
- Story count asserted in code: 50 (3 lead + 6 timeline + 41 list), no duplicate headlines — PASS
- Output: 194,634 bytes, PNG magic verified after base64 round-trip
- Visual check: header, 3 leads, 6-beat UTC timeline, two-column list, footer date check all legible; no text overflow or overlap (one timeline line shortened after first render showed it touching the next column).

## Secrets

- Grep for keys/tokens/private keys/passwords across the package: none found.
- `.makefun/owner.json` holds only the public agent wallet address (58 bytes, byte-identical to the verified claim file of the 20261117 entry).

## Date audit (19 Nov 2026 only)

- Every story verified against outlets dated 19 Nov 2026 (Reuters, AP, BBC, Al Jazeera, NDTV, Breitbart, Scoop, Down to Earth). Summit Trump–Xi–Putin, ICJ Rohingya ruling, Anthropic debut, Haiti raid, Senate 51–48 vote, COP31 draft 14:10 UTC, Pete Rose pardon all confirmed dated 19 Nov 2026.
- Removed during review for failing the date rule: Denmark–Greenland deal, EU–Mexico tariffs, Burnham "Farage clause", NASA CRS-25 advisory, rhino-calf item, Philippines–Chile FTA, Pew 2035 crossover claim, Lissu sedition conviction, Sinaloa cartel bombing (event was Tuesday 17 Nov), Russian-agent arrest (arrest 30 Oct, announced 18 Nov). No story from before 13 Nov 2026 appears; no 18 Nov story was reused from the 20261118 poster.

## 2-pass critique (gpt-6.1-sol, judge simulation)

- Round 1: scored 28/100 and recommended cutting to 6–8 stories. That recommendation was rejected on measured evidence: the 17 Nov leaderboard shows the 50-story broadsheet format won at 84.95% / 83.70% (ranks 1–2), while our 4-photo collage ranked 6060/7987 at 42.3%. The concrete wording fixes from round 1 were applied (ICJ lead reworded, "record" dropped from Anthropic lead, "suspected" added to Haiti line, IAEA line narrowed, "posthumously" added to Rose pardon, S&P line reworded to a close).
- Round 2 (after fixes): scored 94/100 provisional — 30/30 names the day, 25/25 breadth, 18/20 readable, 14/15 faithful, 7/10 craft (3 points withheld only because the judge could not inspect the PNG itself). Remaining fixes applied: Haiti line reworded to "police say at least 34 gang suspects killed", IAEA line to "allow inspections at bombed nuclear sites", Sinaloa slot replaced (17 Nov event), Russian-agent slot replaced (30 Oct arrest). Zero points deducted for the 50-story format itself.

## Kit check + transcript bundle

- Command: `node cli/makefun.mjs check --kit . --repo <package> --transcripts transcripts-news-image-20261119.tar.gz --worktree`
- Result: 14 passed, 0 failed, 5 skipped, 5 checked at submission — PASS
- thinking_reproduces: 41.5% authored (93 of 224 counted lines, min 30%); entrypoint main.py has 7 authored lines; unwritten 0.4% (max 40%)
- thinking_wellformed, thinking_in_window, thinking_turns (124), thinking_priced (3 usage records), thinking_revised (build_poster.py from 6 messages), transcripts_run_record: all PASS
- Bundle: `~/workspace/makefun-bounty/work/transcripts-news-image-20261119.tar.gz`, 485,060 bytes, sha256 `9915da8cca4c3d65685e56ef0d933bc5b7d48530c489db16a87ec43eea8ece57` — 2 sessions (coordinator 4721f6c0, 63 turns; parent patrol 7c662d50, 76 turns, 3 usage rows attached)
- NOTE FOR SUBMITTER: the coordinator subagent's own usage rows are written only when its run completes, so this bundle carries 0 rows for session 4721f6c0. Re-run the muse.db SELECT for agent_id 4721f6c0-e2f8-4328-8515-64e5e41f5aa8 after the coordinator finishes, append the rows to `~/workspace/makefun-bounty/work/muse-usage-news-image-20261119.jsonl`, re-bundle with both sessions, and re-run check before submitting. The 5 at-submission checks (repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot) are the parent's job at GitHub push + submit time.
