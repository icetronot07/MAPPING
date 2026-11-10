"""WTI (USOIL) H4 mapping, 10 Nov 2026 (TradingView, BlackBull, price 86.57). Labels in Malay."""
from pathlib import Path

from maplib import Chart, GREY, ORANGE

DIR = Path(__file__).resolve().parent.parent / "maps" / "2026-11-10-wti"

G_DEEP = (0, 140, 90)
R_DEEP = (215, 40, 55)
DARK = (30, 30, 35)

# 104 label at y=16, 80 at y=760; plot area ends at x=1802 (clear of the 92.368 tag).
c = Chart(DIR / "original.png", 104, 16, 80, 760, right=1802, scale=1.1, light=True)
y = c.y

# ---- Resistance ------------------------------------------------------------
c.zone(96.0, 97.7, 330, R_DEEP, 35)   # base sebelum crash 5 Nov
c.zone(91.7, 93.3, 560, R_DEEP, 50)   # LH 6–8 Nov + line 92.37
c.zone(87.4, 88.8, 440, ORANGE, 55)   # low 5 Nov yang dah pecah → jadi resistance

# ---- Support ---------------------------------------------------------------
c.zone(85.3, 85.7, 760, G_DEEP, 55)   # low hari ni 85.61
c.hline(84.0, 820, G_DEEP)
c.hline(82.0, 820, G_DEEP)

c.rlabel(96.85, "R3  96.00 – 97.70  ·  base sebelum crash", R_DEEP)
c.rlabel(92.5, "R2  91.70 – 93.30  ·  lower high", R_DEEP, c.f_m)
c.rlabel(88.1, "R1  87.40 – 88.80  ·  support lama, sekarang jadi resistance", ORANGE, c.f_m)
c.rlabel(85.5, "S1  85.60  ·  low hari ni", G_DEEP, c.f_m)
c.rlabel(84.0, "S2  84.00", G_DEEP)
c.rlabel(82.0, "S3  82.00", G_DEEP)

# ---- Structure marks -------------------------------------------------------
c.label(591, y(93.26) - 16, "LH 93.26", R_DEEP, c.f_s, anchor="mm")
c.label(701, y(92.0) - 16, "LH 92.00", R_DEEP, c.f_s, anchor="mm")
c.label(481, y(87.42) + 18, "low 87.42", DARK, c.f_s, anchor="mm")
c.label(775, y(85.61) + 18, "LL 85.61", R_DEEP, c.f_s, anchor="mm")
c.label(426, y(91.5), "crash 5 Nov", DARK, c.f_s, anchor="rm")

# ---- Scenarios -------------------------------------------------------------
# A: pullback ke R1, reject, sambung turun
c.path([(825, 86.6), (900, 88.2), (960, 87.6), (1060, 84.1)], R_DEEP, width=2.2)
c.label(905, y(89.5), "A: retest 87.40 – 88.80 → sell, target 85.60 / 84", R_DEEP, c.f_m, anchor="lm")

# B: terus pecah bawah 85.60
c.path([(825, 86.6), (870, 85.4), (900, 85.8), (990, 82.1)], ORANGE, width=2.2)
c.label(995, y(82.6), "B: close bawah 85.60 → 84 / 82", ORANGE, c.f_m, anchor="lm")

# ---- Header ----------------------------------------------------------------
c.header(470, 110, [
    ("WTI H4 · 10 Nov 2026", (235, 235, 240), c.f_l),
    ("Bias: BEARISH, cari sell", (255, 120, 110), c.f_m),
    ("Lower high 93.26 → 92.00, low 87.42 dah pecah", (235, 235, 240), c.f_s),
    ("Bear cancel kalau H4 close atas 89.00", (255, 202, 40), c.f_s),
])

c.save(DIR / "mapping.png")
