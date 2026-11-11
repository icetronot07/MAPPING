"""XAUUSD H4 mapping, 11 Nov 2026 (TradingView, price 4058.7). Labels in Malay."""
from pathlib import Path

from maplib import Chart, GREY, ORANGE

DIR = Path(__file__).resolve().parent.parent / "maps" / "2026-11-11"

G_DEEP = (0, 140, 90)
R_DEEP = (215, 40, 55)
DARK = (30, 30, 35)

# 4140 label at y=130, 4020 at y=395; plot area ends at x=1250 (clear of the 3995 tag).
c = Chart(DIR / "original.png", 4140, 130, 4020, 395, right=1250, scale=1.0, light=True)
y = c.y

# ---- Resistance ------------------------------------------------------------
c.zone(4140, 4150, 370, R_DEEP, 40)    # triple top
c.zone(4088, 4105, 430, R_DEEP, 45)    # lantai range lama yang dah pecah
c.zone(4060, 4077, 455, ORANGE, 60)    # zon buy semalam → sekarang resistance

# ---- Support ---------------------------------------------------------------
c.zone(4027, 4035, 515, G_DEEP, 45)    # low bounce hari ni
c.zone(4013, 4018, 480, G_DEEP, 60)    # LL 4014
c.zone(3995, 4000, 600, G_DEEP, 40)    # 4000 + line 3995
c.hline(3960, 600, GREY)

c.rlabel(4145, "4140 – 4150  ·  triple top", R_DEEP)
c.rlabel(4096.5, "R2  4088 – 4105  ·  lantai range lama", R_DEEP)
c.rlabel(4068.5, "R1  4060 – 4077  ·  zon buy semalam, sekarang resistance", ORANGE, c.f_m)
c.rlabel(4031, "S1  4027 – 4035", G_DEEP)
c.rlabel(4015.5, "S2  4014  ·  low semalam", G_DEEP, c.f_m)
c.rlabel(3997.5, "S3  3995 – 4000", G_DEEP, c.f_m)
c.rlabel(3960, "3960", GREY)

# ---- Structure marks -------------------------------------------------------
c.label(383, y(4148.2) - 14, "4148", DARK, c.f_s, anchor="mm")
c.label(487, y(4013.8) + 16, "LL 4014", R_DEEP, c.f_s, anchor="mm")
c.label(238, y(4030.1) + 16, "low lama 4030", DARK, c.f_s, anchor="mm")

# ---- Scenarios -------------------------------------------------------------
# A: reject di R1, sambung turun
c.path([(565, 4059), (610, 4072), (650, 4064), (730, 4016)], R_DEEP, width=2.2)
c.label(735, y(4045), "A: reject 4060 – 4077 → sell, target 4030 / 4015", R_DEEP, c.f_m, anchor="lm")

# B: close atas 4077 → naik ke R2
c.path([(565, 4059), (640, 4082), (670, 4076), (740, 4098)], G_DEEP, width=2.2)
c.label(745, y(4112), "B: close atas 4077 → 4090 – 4105", G_DEEP, c.f_m, anchor="lm")

# ---- Header ----------------------------------------------------------------
c.header(22, 520, [
    ("XAUUSD H4 · 11 Nov 2026", (235, 235, 240), c.f_l),
    ("Bias: jangka pendek BEARISH", (255, 120, 110), c.f_m),
    ("Triple top 4148, lepas tu pecah bawah 4030", (235, 235, 240), c.f_s),
    ("Sekarang tengah bounce ke resistance", (255, 202, 40), c.f_s),
    ("News US 12 & 13 Nov, jaga lot", (255, 120, 110), c.f_s),
])

c.save(DIR / "mapping.png")
