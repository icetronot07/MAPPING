"""XAUUSD H4 mapping, 10 Nov 2026 (TradingView, ICE feed, price 4118.70). Labels in Malay."""
from pathlib import Path

from maplib import Chart, GREY, ORANGE

DIR = Path(__file__).resolve().parent.parent / "maps" / "2026-11-10"

G_DEEP = (0, 140, 90)
R_DEEP = (215, 40, 55)
DARK = (30, 30, 35)

# 4150 label at y=189, 4100 at y=396; plot area ends at x=1825.
c = Chart(DIR / "original.png", 4150, 189, 4100, 396, right=1825, scale=1.1, light=True)
y = c.y

# ---- Zones -----------------------------------------------------------------
c.zone(4170, 4180, 900, R_DEEP, 35)    # target after breakout
c.zone(4140, 4150, 380, R_DEEP, 55)    # triple top 4147–4148
c.zone(4098, 4107, 600, ORANGE, 55)    # 2-day range low
c.zone(4060, 4077, 540, G_DEEP, 50)    # BOS + impulse base
c.hline(4026, 520, R_DEEP)

c.rlabel(4175, "Target breakout  4170 – 4180", R_DEEP)
c.rlabel(4145, "Atap  4140 – 4150  ·  triple top, kena reject lagi", R_DEEP, c.f_m)
c.rlabel(4102.5, "Lantai range  4098 – 4107", ORANGE, c.f_m)
c.rlabel(4068.5, "Zon BUY  4060 – 4077", G_DEEP, c.f_m)
c.rlabel(4026, "4026  ·  bawah ni bull cancel", R_DEEP)

# ---- Marks -----------------------------------------------------------------
c.label(661, y(4148.3) - 16, "sweep 4148", DARK, c.f_s, anchor="mm")
c.label(395, y(4146.9) - 16, "4147", DARK, c.f_s, anchor="mm")
c.label(528, y(4025.8) + 16, "HL 4026", G_DEEP, c.f_s, anchor="mm")
c.label(648, y(4084) + 16, "range 2 hari", GREY, c.f_s, anchor="mm")

# ---- Scenarios -------------------------------------------------------------
# A: pecah atas 4150 → 4170–4180
c.path([(712, 4119), (760, 4140), (800, 4134), (880, 4175)], G_DEEP, width=2.2)
c.label(885, y(4160), "A: close atas 4150 → 4170 / 4180", G_DEEP, c.f_m, anchor="lm")

# B: main range — turun lantai, lantun balik
c.path([(712, 4119), (770, 4103), (850, 4138)], ORANGE, width=2.2)
c.label(855, y(4125), "B: main range  4100 ↔ 4145", ORANGE, c.f_m, anchor="lm")

# C: pecah bawah 4098 → zon buy
c.path([(712, 4119), (790, 4096), (830, 4102), (920, 4068)], R_DEEP, width=2.2)
c.label(925, y(4085), "C: close bawah 4098 → tunggu 4060–4077", R_DEEP, c.f_m, anchor="lm")

# ---- Header ----------------------------------------------------------------
c.header(22, 140, [
    ("XAUUSD H4 · 10 Nov 2026", (235, 235, 240), c.f_l),
    ("Bias: sideways 4100 – 4148", (255, 202, 40), c.f_m),
    ("4147 kena reject 3 kali", (235, 235, 240), c.f_s),
    ("Trend besar masih naik", (102, 220, 120), c.f_s),
    ("News US minggu ni, jaga lot", (255, 120, 110), c.f_s),
])

c.save(DIR / "mapping.png")
