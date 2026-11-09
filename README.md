# MAPPING

XAUUSD chart mappings. Each one marks up a chart screenshot with key zones, structure and trade scenarios.

| Date | TF | Price | Bias | Mapping |
|---|---|---|---|---|
| 9 Nov 2026 | H4 | 4121.56 | Bullish while 4026 holds, under 4147 double top | [maps/2026-11-09](maps/2026-11-09/README.md) |
| 6 Nov 2026 | H4 | 4048.56 | Pullback, decision at 4000–4030 *(Plan A played: low 4026, TP 4110 hit)* | [maps/2026-11-06](maps/2026-11-06/README.md) |
| 5 Nov 2026 | H4 | 4137.31 | Bullish above 4055 *(invalidated 5 Nov)* | [maps/2026-11-05](maps/2026-11-05/README.md) |

## Layout

```
maps/<date>/original.*     screenshot as received
maps/<date>/mapping.png    marked-up chart
maps/<date>/README.md      levels, scenarios, notes
scripts/maplib.py          drawing helpers (zones, labels, paths)
scripts/map_<date>.py      one script per mapping
```

Requires Pillow (`pip install pillow`). Run a script from the repo root, for example:

```bash
python3 scripts/map_2026-11-06.py
```

> Educational chart mappings only, not financial advice.
