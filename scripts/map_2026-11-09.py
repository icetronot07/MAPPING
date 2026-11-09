"""XAUUSD H4 mapping, 9 Nov 2026 (TradingView, ICE feed, price 4121.56)."""
from pathlib import Path

from maplib import Chart, GREY, ORANGE, PURPLE, RED, WHITE, YELLOW

DIR = Path(__file__).resolve().parent.parent / "maps" / "2026-11-09"

# Light chart: use deeper colours so zones and paths stay visible.
G_DEEP = (0, 140, 90)
R_DEEP = (215, 40, 55)

# 4160 label at y=29, 3980 at y=702; plot area ends at x=1428.
c = Chart(DIR / "original.png", 4160, 29, 3980, 702, right=1428, scale=1.15, light=True)
y = c.y

# ---- Resistance ------------------------------------------------------------
c.zone(4133, 4147.5, 560, R_DEEP, 55) # 5 Nov top 4146.6 + today's 4132–4134 wicks

# ---- Support ---------------------------------------------------------------
c.zone(4105, 4115, 600, YELLOW, 60)   # pivot: top of the 5 Nov sell-off, base of current candle
c.zone(4060, 4077, 740, G_DEEP, 50)   # base of the 8 Nov impulse + 6 Nov 4077 high
c.zone(4026, 4043, 700, G_DEEP, 40)   # 6 Nov higher low (4026) + 4041/4043 lows
c.hline(4000, 450, GREY)

# ---- Labels ----------------------------------------------------------------
c.rlabel(4140, "R1  4133 – 4147  ·  double top 4147 + today's wicks", R_DEEP, c.f_m)
c.rlabel(4110, "Pivot  4105 – 4115", ORANGE)
c.rlabel(4068.5, "S1  4060 – 4077  ·  BOS + impulse base · BUY ZONE", G_DEEP, c.f_m)
c.rlabel(4034.5, "S2  4026 – 4043  ·  HL 4026 · bull invalidation", G_DEEP)
c.rlabel(4000, "4000  ·  round number", GREY)

# ---- Structure marks -------------------------------------------------------
c.label(568, y(4146.6) - 16, "HH 4147", (30, 30, 35), c.f_m, anchor="mm")
c.label(718, y(4026) + 18, "HL 4026 ✓", G_DEEP, c.f_m, anchor="mm")
c.label(783, y(4134) - 18, "rejection wicks", R_DEEP, c.f_s, anchor="mm")

# ---- Scenarios -------------------------------------------------------------
# A: break and close above 4147, retest, run to 4180
c.path([(810, 4121), (860, 4151), (900, 4144), (950, 4160)], G_DEEP, width=2.2)
c.label(962, y(4159), "A: H4 close > 4147 → retest → 4160 / 4180", G_DEEP, c.f_m, anchor="lm")

# B: rejection at R1, pullback into S1, then back up
c.path([(810, 4121), (860, 4136), (960, 4070), (1060, 4122)], ORANGE, width=2.2)
c.label(965, y(4057), "B: reject 4133–4147 → buy 4060–4077 → 4120 / 4147", ORANGE, c.f_m, anchor="lm")

# ---- Header ----------------------------------------------------------------
c.header(30, 215, [
    ("XAUUSD · H4 MAPPING · 9 Nov 2026", WHITE, c.f_l),
    ("Bias: BULLISH while 4026 holds", (102, 220, 120), c.f_m),
    ("6 Nov plan A played: 4026 low → TP 4065 & 4110 hit", WHITE, c.f_s),
    ("Price under double top 4147 · wait for a break or a dip", YELLOW, c.f_s),
    ("US news this week (10 · 12 · 13 Nov) · expect spikes", (255, 120, 110), c.f_s),
])

c.save(DIR / "mapping.png")
