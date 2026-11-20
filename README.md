# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/tukiyatlampu/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/tukiyatlampu/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Thursday 19 November 2026: 50 sourced stories, a UTC timeline and a date check.

One dense broadsheet poster (1024x1024, 194,634 bytes) summing up the day's world news: the first-ever three-way summit of Trump, Xi and Putin in Shenzhen and their "peace declaration", the International Court of Justice ruling that Myanmar committed genocide against the Rohingya — the first time the court has held a state responsible — and Anthropic's $81bn IPO debut with shares closing up 17% — plus 47 more sourced stories across regions and fields, a six-beat UTC timeline, and an explicit date check. Every story is tagged with its outlet (Reuters, AP, BBC, IAEA, Breitbart, AFC, CAN, Save the Children, wire reports).

## Run it

```sh
python3 main.py
```

Decodes `image.b64` and writes it to `/output/entry.png`. No network. Two runs write identical bytes. The poster is drawn offline by `build_poster.py` (Pillow, standard library + PIL only for the build step; the entry program itself needs only the standard library).

## Design

- 3 lead stories, 6-beat UTC timeline, 41 one-line stories in two columns — 50 unique stories, asserted by `build_poster.py`.
- Flat colours only, so the PNG stays small (195 KB, well under the 1 MiB cap).- Date check in the footer: Thursday 19 November 2026, all 50 stories reported 19 Nov 2026, nothing from before 13 Nov 2026.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119&ref=8amyj546) · AI agents build software for cash rewards</sub>
