"""Small drawing helpers for marking up MT5 chart screenshots."""
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

RED = (239, 83, 80)
GREEN = (38, 166, 154)
LIME = (102, 220, 120)
YELLOW = (255, 202, 40)
PURPLE = (171, 120, 255)
GREY = (160, 160, 170)
ORANGE = (255, 152, 0)
WHITE = (235, 235, 240)


class Chart:
    """A screenshot plus its price-axis calibration.

    Calibrate with two price labels from the screenshot's scale:
    (price_a, y_a) and (price_b, y_b).  `scale` multiplies line widths,
    font sizes and padding so the same layout reads well on bigger images.
    """

    def __init__(self, src, price_a, y_a, price_b, y_b, right, scale=1.0):
        self.base = Image.open(src).convert("RGBA")
        self.overlay = Image.new("RGBA", self.base.size, (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.overlay)
        self.pa, self.ya = price_a, y_a
        self.per_px = (price_a - price_b) / (y_b - y_a)
        self.right = right
        self.k = scale
        self.f_s = ImageFont.truetype(FONT, round(12 * scale))
        self.f_m = ImageFont.truetype(FONT_B, round(13 * scale))
        self.f_l = ImageFont.truetype(FONT_B, round(15 * scale))

    def y(self, price):
        return self.ya + (self.pa - price) / self.per_px

    def zone(self, lo, hi, x0, color, alpha=55):
        box = [x0, self.y(hi), self.right, self.y(lo)]
        self.d.rectangle(box, fill=color + (alpha,))
        self.d.rectangle(box, outline=color + (200,), width=max(1, round(self.k)))

    def box(self, x0, x1, lo, hi, color, alpha=18):
        self.d.rectangle([x0, self.y(hi), x1, self.y(lo)], fill=color + (alpha,),
                         outline=color + (170,), width=max(1, round(self.k)))

    def hline(self, price, x0, color, dash=8, gap=6, width=1):
        yy, x = self.y(price), x0
        dash, gap, width = dash * self.k, gap * self.k, max(1, round(width * self.k))
        while x < self.right:
            self.d.line([x, yy, min(x + dash, self.right), yy], fill=color + (230,), width=width)
            x += dash + gap

    def label(self, x, yy, text, color, font=None, anchor="lm"):
        font = font or self.f_s
        pad = 3 * self.k
        b = self.d.textbbox((x, yy), text, font=font, anchor=anchor)
        self.d.rectangle([b[0] - pad, b[1] - pad, b[2] + pad, b[3] + pad],
                         fill=(12, 12, 16, 215), outline=color + (220,))
        self.d.text((x, yy), text, font=font, fill=color + (255,), anchor=anchor)

    def rlabel(self, price, text, color, font=None):
        """Label right-aligned against the plot edge at a given price."""
        self.label(self.right - 6 * self.k, self.y(price), text, color, font, anchor="rm")

    def path(self, points, color, width=2, dash=7, gap=5, head=True):
        """Dashed projection path; points are (x, price). Arrow head at the end."""
        pts = [(x, self.y(p)) for x, p in points]
        width, dash, gap = max(1, round(width * self.k)), dash * self.k, gap * self.k
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            n = max(int(length // (dash + gap)), 1)
            for i in range(n):
                t0 = i * (dash + gap) / length
                t1 = min((i * (dash + gap) + dash) / length, 1)
                self.d.line([x1 + (x2 - x1) * t0, y1 + (y2 - y1) * t0,
                             x1 + (x2 - x1) * t1, y1 + (y2 - y1) * t1],
                            fill=color + (240,), width=width)
        if head:
            (xa, ya), (xb, yb) = pts[-2], pts[-1]
            s = 8 * self.k * (1 if yb < ya else -1)
            self.d.polygon([(xb, yb), (xb - 8 * self.k, yb + s), (xb + 8 * self.k, yb + s)],
                           fill=color + (255,))

    def header(self, x, y, lines):
        """lines: [(text, color, font)] drawn in a dark panel."""
        step = 22 * self.k
        widths = [self.d.textbbox((0, 0), t, font=f)[2] for t, _, f in lines]
        self.d.rectangle([x - 8 * self.k, y - 8 * self.k,
                          x + max(widths) + 10 * self.k, y + step * len(lines)],
                         fill=(12, 12, 16, 225), outline=(90, 90, 110, 255))
        for i, (t, c, f) in enumerate(lines):
            self.d.text((x, y + i * step), t, font=f, fill=c + (255,))

    def save(self, out):
        Image.alpha_composite(self.base, self.overlay).convert("RGB").save(out, optimize=True)
        print(f"saved {out}")
