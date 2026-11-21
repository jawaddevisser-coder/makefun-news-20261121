# makefun-news-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/jawaddevisser-coder/makefun-news-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/jawaddevisser-coder/makefun-news-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Sum up the world's news of Saturday 21 November 2026 in one image: a bright
magazine-style "global briefing" poster. Lead story: Trump tells European
leaders to stop funding Ukraine, after the Shenzhen summit. Also: the EU and
Indonesia sign their landmark trade deal, BepiColombo enters orbit around
Mercury, stocks slide into correction, and tankers are hit near Hormuz.

The image is drawn by `draw_news.py` (Python + Pillow, deterministic, no
network) into `entry.png` (1024x1024, under 1 MiB). `main.py` (Python 3.13,
standard library only) copies it to the grader's output path.

## Stories in the image (all verified 21 Nov 2026)

- **Trump tells Europe: stop funding Ukraine** — Reuters, 21 Nov 2026:
  Zelenskiy said on Saturday that Trump told European leaders at their Berlin
  meeting they spend too much on the war and could use the money at home once
  a peace deal is reached. (The trilateral Shenzhen summit itself was
  19 Nov, so it is not presented as a 21 Nov event.)
- **EU & Indonesia sign landmark trade deal** — Reuters / European Commission,
  21 Nov 2026: CEPA and IPA signed in Brussels after 10 years of talks;
  tariffs fall on 90% of goods; in effect in early 2027.
- **BepiColombo reaches Mercury** — ESA / JAXA, 21 Nov 2026: after an
  8-year voyage the twin orbiters enter Mercury orbit (18:24 UTC), only the
  second spacecraft ever to circle Mercury.
- **Stocks slide into correction** — 21 Nov 2026: an AI-led sell-off pushes
  the S&P 500 into correction; Japan's Nikkei falls 5.1%.
- **Tankers hit near Hormuz** — UKMTO / NYT, 21 Nov 2026: projectiles strike
  tankers near the Strait of Hormuz as US–Iran talks stall; Trump weighs new
  strikes on Iran.
- Ticker: UK and EU sign three post-Brexit deals; COP31 climate talks miss
  their deadline in Antalya; Denmark expels a Russian diplomat.

## Run it

```sh
python3 draw_news.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
