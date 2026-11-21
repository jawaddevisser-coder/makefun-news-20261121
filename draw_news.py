#!/usr/bin/env python3
"""Draw entry.png: 'The World Today' — a bright magazine-style global
briefing poster summing up Saturday 21 November 2026 in one image.

Everything is drawn with Pillow (vector shapes + text). Deterministic:
no randomness, no network, no timestamps in the output.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
M = 36  # outer margin

INK = (16, 36, 62)        # deep navy
RED = (214, 38, 61)       # signal red
TEAL = (14, 124, 123)     # teal
GOLD = (232, 163, 23)     # gold
PANEL = (237, 242, 247)   # pale blue-grey
GREY = (90, 107, 124)     # secondary text
BORDER = (217, 226, 236)  # hairlines
WHITE = (255, 255, 255)
EU_BLUE = (0, 51, 153)
UA_BLUE = (0, 87, 183)
UA_YELLOW = (255, 215, 0)
ID_RED = (206, 17, 38)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def draw_us_flag(d, x, y, w, h):
    stripe = h / 13.0
    for i in range(13):
        c = (179, 25, 66) if i % 2 == 0 else WHITE
        d.rectangle([x, y + i * stripe, x + w, y + (i + 1) * stripe], fill=c)
    cw, ch = w * 0.4, stripe * 7
    d.rectangle([x, y, x + cw, y + ch], fill=(10, 49, 97))
    for r in range(4):
        for c in range(5):
            cx = x + cw * (0.12 + 0.19 * c)
            cy = y + ch * (0.16 + 0.23 * r)
            d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=WHITE)


def draw_eu_flag(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=EU_BLUE)
    cx, cy, r = x + w / 2, y + h / 2, min(w, h) * 0.32
    for i in range(12):
        a = -math.pi / 2 + i * math.pi / 6
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 204, 0))


def draw_ua_flag(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 2], fill=UA_BLUE)
    d.rectangle([x, y + h / 2, x + w, y + h], fill=UA_YELLOW)


def draw_id_flag(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 2], fill=ID_RED)
    d.rectangle([x, y + h / 2, x + w, y + h], fill=WHITE)
    d.rectangle([x, y, x + w, y + h], outline=BORDER, width=1)


def draw_stop_sign(d, cx, cy, r):
    pts = []
    for i in range(8):
        a = math.pi / 8 + i * math.pi / 4
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=RED, outline=WHITE, width=4)
    f = font(SANS_B, 36)
    d.text((cx, cy - 4), "STOP", font=f, fill=WHITE, anchor="mm")


def draw_mercury(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(154, 163, 168))
    for (ox, oy, cr) in [(-18, -14, 9), (14, -20, 7), (20, 12, 11),
                          (-12, 18, 6), (2, 2, 8), (-26, 4, 5)]:
        d.ellipse([cx + ox - cr, cy + oy - cr, cx + ox + cr, cy + oy + cr],
                  fill=(120, 130, 136))
    d.ellipse([cx - r - 14, cy - r - 6, cx + r + 14, cy + r + 6],
              outline=TEAL, width=3)
    # tiny spacecraft riding the orbit ellipse, upper right
    sx = cx + (r + 14) * math.cos(-math.pi / 5)
    sy = cy + (r + 6) * math.sin(-math.pi / 5)
    d.rectangle([sx - 7, sy - 5, sx + 7, sy + 5], fill=WHITE,
                outline=TEAL, width=2)
    d.rectangle([sx + 7, sy - 3, sx + 15, sy + 3], fill=GOLD)


def draw_chart(d, x, y, w, h):
    f = font(SANS_B, 26)
    d.text((x + 10, y + 6), "-5.1%", font=f, fill=RED)
    d.line([(x + 8, y + h - 18), (x + w - 8, y + h - 18)], fill=GREY, width=2)
    pts = [(x + 10, y + 44), (x + 34, y + 52), (x + 58, y + 48),
           (x + 82, y + 70), (x + 106, y + 84), (x + w - 12, y + h - 26)]
    d.line(pts, fill=RED, width=5, joint="curve")
    ex, ey = pts[-1]
    d.polygon([(ex - 10, ey - 2), (ex + 2, ey - 12), (ex + 2, ey + 8)],
              fill=RED)


def draw_tanker(d, x, y, w, h):
    d.polygon([(x + 8, y + 52), (x + 8, y + 78), (x + w - 8, y + 78),
               (x + w - 22, y + 52)], fill=INK)
    d.rectangle([x + w - 52, y + 26, x + w - 30, y + 52], fill=INK)
    d.rectangle([x + 22, y + 38, x + 40, y + 52], fill=INK)
    for wy in (84, 96):
        for k in range(4):
            d.arc([x + k * 30 - 6, y + wy, x + k * 30 + 24, y + wy + 16],
                  start=180, end=360, fill=TEAL, width=3)
    d.polygon([(x + w - 14, y + 4), (x + w - 2, y + 22), (x + w - 26, y + 22)],
              fill=GOLD, outline=INK, width=2)
    f = font(SANS_B, 13)
    d.text((x + w - 14, y + 12), "!", font=f, fill=INK, anchor="mm")


def card(d, x, y, w, h, graphic, kicker, kcolor, headline, dek):
    d.rectangle([x, y, x + w, y + h], fill=WHITE, outline=BORDER, width=2)
    d.rectangle([x, y, x + w, y + 6], fill=kcolor)
    gx, gy, gw, gh = x + 14, y + 22, 132, h - 44
    d.rectangle([gx, gy, gx + gw, gy + gh], fill=PANEL)
    graphic(d, gx, gy, gw, gh)
    tx = gx + gw + 16
    tw = x + w - 16 - tx
    f_k = font(SANS_B, 17)
    d.text((tx, y + 20), kicker, font=f_k, fill=kcolor)
    f_h = font(SERIF_B, 23)
    lines = wrap(d, headline, f_h, tw)
    yy = text_block(d, tx, y + 46, lines, f_h, INK, 27)
    f_d = font(SANS, 17)
    dlines = wrap(d, dek, f_d, tw)
    text_block(d, tx, yy + 6, dlines, f_d, GREY, 21)


def trade_graphic(d, x, y, w, h):
    draw_eu_flag(d, x + 16, y + 14, w - 32, 52)
    d.polygon([(x + w / 2 - 8, y + 76), (x + w / 2 + 8, y + 76),
               (x + w / 2, y + 94)], fill=TEAL)
    d.line([(x + w / 2, y + 70), (x + w / 2, y + 92)], fill=TEAL, width=3)
    draw_id_flag(d, x + 16, y + 100, w - 32, 52)


def mercury_graphic(d, x, y, w, h):
    draw_mercury(d, x + w / 2, y + h / 2 + 4, 46)


def markets_graphic(d, x, y, w, h):
    draw_chart(d, x, y, w, h)


def hormuz_graphic(d, x, y, w, h):
    draw_tanker(d, x, y, w, h)


def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # --- masthead -------------------------------------------------------
    f_mast = font(SERIF_B, 58)
    d.text((M, 34), "THE WORLD TODAY", font=f_mast, fill=INK)
    d.rectangle([W - M - 208, 48, W - M - 196, 96], fill=TEAL)
    f_tag = font(SANS_B, 21)
    d.text((W - M - 184, 52), "GLOBAL", font=f_tag, fill=INK)
    d.text((W - M - 184, 76), "BRIEFING", font=f_tag, fill=TEAL)

    # --- date bar -------------------------------------------------------
    d.rectangle([0, 148, W, 184], fill=RED)
    f_date = font(SANS_B, 20)
    d.text((M, 157), "SATURDAY  •  21 NOVEMBER 2026", font=f_date, fill=WHITE)
    f_right = font(SANS_B, 18)
    tw = d.textlength("ONE DAY  •  ONE PICTURE", font=f_right)
    d.text((W - M - tw, 158), "ONE DAY  •  ONE PICTURE", font=f_right,
           fill=(255, 220, 224))

    # --- lead story -----------------------------------------------------
    ly, lh = 194, 288
    d.rectangle([M, ly, W - M, ly + lh], fill=WHITE, outline=BORDER, width=2)
    d.rectangle([M, ly, M + 8, ly + lh], fill=RED)
    px, py, pw, ph = M + 22, ly + 20, 260, lh - 40
    d.rectangle([px, py, px + pw, py + ph], fill=PANEL)
    draw_stop_sign(d, px + pw / 2, py + 78, 64)
    fy = py + ph - 74
    draw_us_flag(d, px + 18, fy, 66, 44)
    draw_eu_flag(d, px + 97, fy, 66, 44)
    draw_ua_flag(d, px + 176, fy, 66, 44)
    f_fl = font(SANS_B, 13)
    for i, lab in enumerate(("USA", "EU", "UKRAINE")):
        cx = px + 18 + i * 79 + 33
        d.text((cx, fy + 50), lab, font=f_fl, fill=GREY, anchor="ma")
    tx = px + pw + 26
    tw = W - M - 20 - tx
    f_k = font(SANS_B, 20)
    d.text((tx, ly + 20), "UKRAINE  •  WASHINGTON", font=f_k, fill=RED)
    f_h = font(SERIF_B, 44)
    lines = wrap(d, "TRUMP TELLS EUROPE: STOP FUNDING UKRAINE", f_h, tw)
    yy = text_block(d, tx, ly + 48, lines, f_h, INK, 50)
    f_d = font(SANS, 20)
    dek = ("Zelenskiy says Trump phoned allies in Berlin: Europe spends too "
           "much on the war \u2014 money it could keep at home once a peace "
           "deal is done.")
    dlines = wrap(d, dek, f_d, tw)
    text_block(d, tx, yy + 8, dlines, f_d, GREY, 25)

    # --- two rows of cards ----------------------------------------------
    cw = (W - 2 * M - 16) // 2
    y1, ch1 = 496, 214
    card(d, M, y1, cw, ch1, trade_graphic, "TRADE  •  BRUSSELS", TEAL,
         "EU & INDONESIA SIGN LANDMARK TRADE DEAL",
         "After 10 years of talks, tariffs fall on 90% of goods; the pact "
         "takes effect in early 2027.")
    card(d, M + cw + 16, y1, cw, ch1, mercury_graphic, "SPACE  •  MERCURY",
         (90, 60, 140),
         "BEPICOLOMBO REACHES MERCURY",
         "After an 8-year voyage, the ESA\u2013JAXA craft enters orbit \u2014 "
         "only the second ever to circle Mercury.")
    y2, ch2 = 724, 214
    card(d, M, y2, cw, ch2, markets_graphic, "MARKETS  •  NEW YORK", RED,
         "STOCKS SLIDE INTO CORRECTION",
         "An AI sell-off drags the S&P 500 into correction; Japan\u2019s "
         "Nikkei falls 5.1%.")
    card(d, M + cw + 16, y2, cw, ch2, hormuz_graphic, "GULF  •  HORMUZ",
         (150, 90, 20),
         "TANKERS HIT NEAR HORMUZ",
         "Projectiles strike tankers as US\u2013Iran talks stall; Trump "
         "weighs new strikes on Iran.")

    # --- ticker ----------------------------------------------------------
    d.rectangle([0, 952, W, 986], fill=INK)
    f_t = font(SANS_B, 17)
    ticker = ("UK\u2013EU sign 3 post-Brexit deals  \u2022  COP31 misses "
              "deadline  \u2022  Denmark expels Russian diplomat")
    assert d.textlength(ticker, font=f_t) <= W - 2 * M, "ticker too long"
    d.text((M, 961), ticker, font=f_t, fill=WHITE)

    # --- footer ----------------------------------------------------------
    f_f = font(SANS, 15)
    d.text((M, 994),
           "Headlines verified 21 Nov 2026  •  Reuters  •  AP  •  NYT  •  "
           "ESA  •  European Commission",
           font=f_f, fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
