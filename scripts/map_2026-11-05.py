"""Draw the XAUUSD H4 mapping on top of the original chart screenshot.

Usage:  python3 scripts/map_2026-11-05.py
Input:  maps/2026-11-05/original.jpg
Output: maps/2026-11-05/mapping.png
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "maps" / "2026-11-05" / "original.jpg"
OUT = ROOT / "maps" / "2026-11-05" / "mapping.png"

# Price-axis calibration taken from the screenshot's labels
# (4166.00 sits at y=258, 4111.30 at y=345  ->  0.6287 $ per pixel).
REF_PRICE, REF_Y, PER_PX = 4166.00, 258, 0.6287
CHART_RIGHT = 1205  # right edge of the plot area (price scale starts after)


def y(price: float) -> float:
    return REF_Y + (REF_PRICE - price) / PER_PX


FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
f_s = ImageFont.truetype(FONT, 12)
f_m = ImageFont.truetype(FONT_B, 13)
f_l = ImageFont.truetype(FONT_B, 15)

RED = (239, 83, 80)
GREEN = (38, 166, 154)
LIME = (102, 220, 120)
YELLOW = (255, 202, 40)
PURPLE = (171, 120, 255)
GREY = (160, 160, 170)
ORANGE = (255, 152, 0)
WHITE = (235, 235, 240)

base = Image.open(SRC).convert("RGBA")
overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
d = ImageDraw.Draw(overlay)


def zone(lo, hi, x0, color, alpha=55, outline=True):
    d.rectangle([x0, y(hi), CHART_RIGHT, y(lo)], fill=color + (alpha,))
    if outline:
        d.rectangle([x0, y(hi), CHART_RIGHT, y(lo)], outline=color + (200,), width=1)


def hline(price, x0, color, dash=8, gap=6, width=1):
    yy = y(price)
    x = x0
    while x < CHART_RIGHT:
        d.line([x, yy, min(x + dash, CHART_RIGHT), yy], fill=color + (230,), width=width)
        x += dash + gap


def label(x, yy, text, color, font=f_s, anchor="lm", pad=3):
    bbox = d.textbbox((x, yy), text, font=font, anchor=anchor)
    d.rectangle([bbox[0] - pad, bbox[1] - pad, bbox[2] + pad, bbox[3] + pad],
                fill=(12, 12, 16, 215), outline=color + (220,))
    d.text((x, yy), text, font=font, fill=color + (255,), anchor=anchor)


def dashed_path(points, color, width=2, dash=7, gap=5):
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        n = max(int(length // (dash + gap)), 1)
        for i in range(n):
            t0 = i * (dash + gap) / length
            t1 = min((i * (dash + gap) + dash) / length, 1)
            d.line([x1 + (x2 - x1) * t0, y1 + (y2 - y1) * t0,
                    x1 + (x2 - x1) * t1, y1 + (y2 - y1) * t1],
                   fill=color + (240,), width=width)


def arrow_head(x, yy, color, up=True, size=8):
    s = -size if up else size
    d.polygon([(x, yy), (x - size, yy - s), (x + size, yy - s)], fill=color + (255,))


# ---- Zones -----------------------------------------------------------------
zone(4190, 4200, 640, RED, 50)            # R2
zone(4160, 4170, 640, RED, 50)            # R1
zone(4118, 4126, 700, YELLOW, 45)         # pivot / red MA retest
zone(4068, 4118, 742, PURPLE, 22)         # H4 FVG of the 4 Nov 20:00 impulse
zone(4055, 4068, 660, LIME, 55)           # Demand 1
zone(4000, 4030, 560, GREEN, 50)          # Demand 2 (flip + blue MA)

# Accumulation range box (31 Oct – 4 Nov)
d.rectangle([248, y(3972), 606, y(3890)], fill=GREY + (18,), outline=GREY + (170,), width=1)
label(254, y(3972) - 12, "Accumulation range 3890 – 3972", GREY)

# Major swing low
hline(3870, 200, RED, width=1)
label(CHART_RIGHT - 6, y(3870), "Swing low 3870 – bull invalidation (macro)", RED, anchor="rm")

# Range high that got broken -> BOS
hline(3972, 360, WHITE, dash=4, gap=4)
label(612, y(3972) + 14, "BOS 3972", WHITE, f_m)

# ---- Zone labels (placed in the empty future area) ---------------------------
LX = CHART_RIGHT - 6
label(LX, y(4195), "R2  4190 – 4200  ·  psych 4200 / TP2", RED, anchor="rm")
label(LX, y(4165), "R1  4160 – 4170  ·  TP1", RED, anchor="rm")
label(LX, y(4122), "Pivot 4118 – 4126  ·  red MA retest", YELLOW, anchor="rm")
label(LX, y(4093), "H4 FVG / imbalance 4068 – 4118", PURPLE, anchor="rm")
label(LX, y(4061.5), "Demand 1  4055 – 4068  ·  buy zone", LIME, anchor="rm")
label(LX, y(4015), "Demand 2  4000 – 4030  ·  flip + blue MA", GREEN, anchor="rm")

# ---- Structure marks ---------------------------------------------------------
label(234, y(3870) + 16, "LL", RED, f_m, anchor="mm")
label(468, y(3906) + 18, "HL", LIME, f_m, anchor="mm")
label(546, y(3925) + 18, "HL", LIME, f_m, anchor="mm")
label(702, y(4056) + 16, "HL", LIME, f_m, anchor="mm")
label(754, y(4141) - 16, "HH", LIME, f_m, anchor="mm")

# ---- Scenarios ---------------------------------------------------------------
# A: shallow dip into the pivot, continuation to R1 then R2
pa = [(768, y(4137)), (800, y(4122)), (850, y(4166)), (880, y(4152)), (940, y(4196))]
dashed_path(pa, LIME)
arrow_head(*pa[-1], LIME, up=True)
label(780, y(4196) - 24, "A: hold 4118 → 4166 → 4195", LIME, f_m, anchor="lm")

# B: deeper pullback into the FVG / Demand 1, then continuation
pb = [(768, y(4137)), (830, y(4062)), (900, y(4125)), (950, y(4163))]
dashed_path(pb, ORANGE)
arrow_head(*pb[-1], ORANGE, up=True)
label(832, y(4062) + 20, "B: fill FVG → buy 4055–4068", ORANGE, f_m, anchor="lm")

# ---- Header ------------------------------------------------------------------
hx, hy = 60, 82
lines = [
    ("XAUUSD · H4 MAPPING · 5 Nov 2026", WHITE, f_l),
    ("Bias: BULLISH while H4 closes above 4055", LIME, f_m),
    ("Price reclaimed red MA (~4120) · blue MA rising (~4014)", WHITE, f_s),
    ("Bull invalid < 4055 → look 4000–4030 · bearish shift < 4000", RED, f_s),
]
widths = [d.textbbox((0, 0), t, font=f)[2] for t, _, f in lines]
d.rectangle([hx - 8, hy - 8, hx + max(widths) + 10, hy + 22 * len(lines)],
            fill=(12, 12, 16, 225), outline=(90, 90, 110, 255))
for i, (t, c, f) in enumerate(lines):
    d.text((hx, hy + i * 22), t, font=f, fill=c + (255,))

out = Image.alpha_composite(base, overlay).convert("RGB")
out.save(OUT, optimize=True)
print(f"saved {OUT.relative_to(ROOT)}")
