"""XAUUSD H4 mapping, 6 Nov 2026 (screenshot 14:24, price 4048.56)."""
from pathlib import Path

from maplib import Chart, GREEN, GREY, LIME, ORANGE, PURPLE, RED, WHITE, YELLOW

DIR = Path(__file__).resolve().parent.parent / "maps" / "2026-11-06"

# 4138.20 label at y=133, 3886.95 at y=1150; plot area ends at x=1890.
c = Chart(DIR / "original.jpg", 4138.20, 133, 3886.95, 1150, right=1890, scale=1.56)
y = c.y

# ---- Resistance ------------------------------------------------------------
c.zone(4138, 4150, 1150, RED, 45)    # 5 Nov top (4147) + 4150 rejection
c.zone(4100, 4118, 950, RED, 45)    # red MA ~4117 + 5 Nov sell-off origin
c.zone(4055, 4068, 700, ORANGE, 55) # yesterday's Demand 1 → now flipped supply

# ---- Support ---------------------------------------------------------------
c.zone(4035, 4040, 1060, YELLOW, 45)  # today's low 4035–4039
c.zone(4000, 4030, 590, GREEN, 50)    # Demand 2: blue MA ~4029 + 4 Nov breakout base + 4000
c.zone(3947, 3972, 560, LIME, 40)     # BOS level / top of old range

# Old accumulation range
c.box(140, 600, 3897, 3972, GREY)
c.label(150, y(3897) + 22, "Old range 3897 – 3972", GREY)

# ---- Labels ----------------------------------------------------------------
c.rlabel(4144, "R3  4138 – 4150  ·  5 Nov top (4147)", RED)
c.rlabel(4109, "R2  4100 – 4118  ·  red MA + sell-off origin", RED)
c.rlabel(4061.5, "R1  4055 – 4068  ·  old demand → now supply", ORANGE)
c.rlabel(4037.5, "S1  4035 – 4040  ·  today's low", YELLOW)
c.rlabel(4015, "S2  4000 – 4030  ·  blue MA + 4000  ·  KEY BUY ZONE", GREEN)
c.rlabel(3959.5, "S3  3947 – 3972  ·  BOS / old range top", LIME)
c.hline(3897, 140, RED)
c.rlabel(3897, "S4  3897  ·  range low", RED)

# ---- Structure marks -------------------------------------------------------
c.label(848, y(4147) - 22, "HH 4147", WHITE, c.f_m, anchor="mm")
c.label(930, y(4138) - 22, "LH", RED, c.f_m, anchor="mm")
c.label(1011, y(4118) - 22, "LH", RED, c.f_m, anchor="mm")
c.label(1092, y(4073) - 22, "LH", RED, c.f_m, anchor="mm")
c.label(1112, y(4035.6) + 26, "LL", RED, c.f_m, anchor="mm")
c.label(1160, y(4127), "5 red H4 candles in a row · 4 Nov gap fully filled", PURPLE, c.f_s, anchor="lm")

# ---- Scenarios -------------------------------------------------------------
# A: dip into S2, bounce, reclaim R1, then R2
c.path([(1150, 4048), (1230, 4022), (1330, 4066), (1380, 4056), (1440, 4108)], LIME)
c.label(1112, y(4092), "A: buy S2 → 4068 → 4110", LIME, c.f_m, anchor="lm")

# B: rejection at R1, break of 4000, run to S3
c.path([(1150, 4048), (1220, 4064), (1330, 4000), (1370, 4010), (1450, 3962)], RED)
c.label(1462, y(3990), "B: H4 close < 4000 → 3972 → 3950", RED, c.f_m, anchor="lm")

# ---- Header ----------------------------------------------------------------
c.header(640, 935, [
    ("XAUUSD · H4 MAPPING · 6 Nov 2026", WHITE, c.f_l),
    ("Bias: pullback inside the bigger uptrend · decision at 4000–4030", YELLOW, c.f_m),
    ("Rejected at 4147 + red MA (~4117) · lost 4055 · blue MA ~4029", WHITE, c.f_s),
    ("Bulls need an H4 close back above 4068 · bears need a close < 4000", RED, c.f_s),
])

c.save(DIR / "mapping.png")
