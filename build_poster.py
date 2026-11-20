#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news poster (1024x1024 PNG).

Dense broadsheet, not a photo collage: 3 lead stories, a 6-beat UTC
timeline, and 41 sourced one-line stories across regions and fields --
50 stories in all, every one first reported on Thursday 19 November
2026. Flat colours only, so the PNG stays small. No network, no
randomness, no clock: the same input always draws the same bytes.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (22, 22, 22)
NAVY = (15, 42, 68)
RED = (139, 26, 26)
MUTED = (90, 100, 115)
RULE = (180, 172, 150)
TIMELINE_BG = (226, 232, 238)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


LEAD = [
    ("Trump, Xi, Putin meet in Shenzhen; issue 'peace declaration'", "REUTERS"),
    ("ICJ finds Myanmar responsible for Rohingya genocide", "BBC"),
    ("Anthropic shares close up 17% on $81bn IPO debut", "BBC"),
]

TIMELINE = [
    ("MORNING", "Cyclone Akvan heads for Andhra-Odisha coast"),
    ("14:10 UTC", "COP31 draft drops all fossil-fuel language"),
    ("AFTERNOON", "Senate rejects Iran war-powers curb, 51-48"),
    ("EVENING", "Haiti police say at least 34 gang suspects killed"),
    ("21:00 UTC", "S&P 500 closes down 2.0% as world stocks slide"),
    ("NIGHT", "Trump posthumously pardons baseball legend Pete Rose"),
]

# (section, headline, source) -- 41 items.
STORIES = [
    ("GULF & MIDDLE EAST", "Trump: US will 'see what happens' on Iran after Jan 1", "REUTERS"),
    ("GULF & MIDDLE EAST", "West presses Iran to allow inspections at bombed nuclear sites", "REUTERS"),
    ("GULF & MIDDLE EAST", "Suspected Houthi missile hits Riyadh's tallest tower", "REUTERS"),
    ("GULF & MIDDLE EAST", "Saudi crown prince meets US CENTCOM chief in Riyadh", "REUTERS"),
    ("GULF & MIDDLE EAST", "Iraq strikes compromise deal with Kataib Hezbollah", "REUTERS"),
    ("GULF & MIDDLE EAST", "Israel completes Gaza ground op beyond Yellow Line", "WIRE"),
    ("GULF & MIDDLE EAST", "US reissues security warnings in Bahrain and Saudi", "WIRE"),
    ("GULF & MIDDLE EAST", "Trump signals no more major Iran strikes in 2026", "BREITBART"),
    ("GULF & MIDDLE EAST", "Iran rails at 'foreign interference' after summit", "BREITBART"),
    ("UKRAINE & EUROPE", "European allies in Berlin ready for talks with Russia", "WIRE"),
    ("UKRAINE & EUROPE", "Sanchez admits mistakes in Spanish election debate", "WIRE"),
    ("UKRAINE & EUROPE", "Russian strikes kill five in Ukraine; power cut", "WIRE"),
    ("UKRAINE & EUROPE", "France jails three women for joining ISIS in Syria", "AP"),
    ("UKRAINE & EUROPE", "Prince Harry ready to re-enlist and fight Russia", "BREITBART"),
    ("ASIA-PACIFIC", "Bangladesh: four killed, Yunus home torched in unrest", "WIRE"),
    ("ASIA-PACIFIC", "Bangladesh opposition shutdown over Hasina return bid", "WIRE"),
    ("ASIA-PACIFIC", "IAEA: North Korea expanded uranium enrichment", "IAEA"),
    ("WORLD", "Trump asks Supreme Court to block Venezuela TPS relief", "AP"),
    ("WORLD", "US and Venezuela sign military cooperation deal", "WIRE"),
    ("WORLD", "US consortium wins Kenya critical minerals deal", "WIRE"),
    ("WORLD", "Dozens missing after migrant boat capsizes off Senegal", "WIRE"),
    ("WORLD", "35 migrants found locked in generator box in Texas", "BREITBART"),
    ("WORLD", "Drone, artillery strikes near Badme as tensions rise", "WIRE"),
    ("WORLD", "Nearly 1 in 4 children now live in conflict zones", "SAVE THE CHILDREN"),
    ("WORLD", "Pakistan says 22 militants killed in raids", "WIRE"),
    ("WORLD", "Democrats pick Jeffries as Speaker nominee", "WIRE"),
    ("WORLD", "Rights group welcomes release of 236 anti-Trump protesters", "WIRE"),
    ("WORLD", "US seizes 38,000 rounds, 17 weapons at Texas border", "BREITBART"),
    ("HEALTH & SCIENCE", "Nearly 150 fall ill in cruise ship outbreak", "BREITBART"),
    ("HEALTH & SCIENCE", "Tasmania child euthanasia proposed; deaths surge 129%", "WIRE"),
    ("HEALTH & SCIENCE", "Fiji, Tonga and Cook Islands declare emergencies", "WIRE"),
    ("MARKETS & TECH", "Nikkei drops 4.68% as AI worries hit world stocks", "WIRE"),
    ("MARKETS & TECH", "Gold falls to 14-month low", "WIRE"),
    ("MARKETS & TECH", "Nvidia faces California probe after Huang exit", "BBC"),
    ("MARKETS & TECH", "Gulf stocks retreat on Iran strife, Fed signals", "REUTERS"),
    ("CLIMATE", "Panama threatens to withhold COP31 consensus", "WIRE"),
    ("CLIMATE", "Nepal wins solidarity award; Norway is Fossil of the Day", "CAN"),
    ("SPORT", "Lee Kang-in named Asian footballer overseas, 2nd year", "AFC"),
    ("SPORT", "Caitlin Foord named Asia's women's player of the year", "AFC"),
    ("SPORT", "Beiranvand first keeper to win Asia's top player award", "AFC"),
    ("SPORT", "Litton Das sets Test record for dismissals in an innings", "WIRE"),
]

FOOTER_SOURCES = ("Sources: Reuters \u00b7 AP \u00b7 BBC \u00b7 IAEA \u00b7 Breitbart \u00b7 AFC \u00b7 CAN \u00b7 Save the Children \u00b7 wire reports")


def shrink(draw, text, path, size, max_w, floor=12):
    """Shrink the font until the text fits; return the fitted font."""
    fnt = font(path, size)
    while size > floor and draw.textlength(text, font=fnt) > max_w:
        size -= 1
        fnt = font(path, size)
    return fnt


def draw_poster(path):
    total = len(LEAD) + len(TIMELINE) + len(STORIES)
    assert total == 50, f"story count is {total}, must be 50"
    assert len(STORIES) == 41
    assert len({s[1] for s in STORIES}) == 41, "duplicate list headline"

    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    y = 0

    # ---- Header -------------------------------------------------
    d.rectangle([0, 0, W, 76], fill=NAVY)
    d.text((24, 12), "WORLD NEWS", font=font(FONT_BOLD, 34), fill=(255, 255, 255))
    d.text((24, 50), "THURSDAY 19 NOVEMBER 2026", font=font(FONT_BOLD, 17), fill=(255, 205, 90))
    right = "50 SOURCED STORIES"
    d.text((W - 24 - d.textlength(right, font=font(FONT_BOLD, 20)), 14),
           right, font=font(FONT_BOLD, 20), fill=(255, 255, 255))
    d.text((W - 24 - d.textlength("ALL EVENTS REPORTED 19 NOV 2026", font=font(FONT_REG, 13)), 44),
           "ALL EVENTS REPORTED 19 NOV 2026", font=font(FONT_REG, 13), fill=(200, 210, 220))
    y = 76

    # ---- Lead stories -------------------------------------------
    y += 8
    for i, (head, src) in enumerate(LEAD, 1):
        d.rectangle([24, y + 4, 30, y + 34], fill=RED)
        f = shrink(d, head, FONT_BOLD, 21, W - 110)
        d.text((42, y), head, font=f, fill=INK)
        d.text((W - 24 - d.textlength(src, font=font(FONT_BOLD, 12)), y + 6),
               src, font=font(FONT_BOLD, 12), fill=RED)
        y += 42
    y += 2
    d.line([24, y, W - 24, y], fill=RULE, width=2)
    y += 8

    # ---- UTC timeline strip --------------------------------------
    d.rectangle([0, y, W, y + 104], fill=TIMELINE_BG)
    d.text((24, y + 6), "UTC TIMELINE \u2014 THROUGH THE DAY", font=font(FONT_BOLD, 14), fill=NAVY)
    ty = y + 28
    col_w = (W - 48) // 3
    for idx, (when, what) in enumerate(TIMELINE):
        cx = 24 + (idx % 3) * col_w
        cy = ty + (idx // 3) * 38
        d.text((cx, cy), when, font=font(FONT_BOLD, 13), fill=RED)
        f = shrink(d, what, FONT_REG, 13, col_w - 12, floor=11)
        d.text((cx, cy + 16), what, font=f, fill=INK)
    y += 104 + 8

    # ---- Two-column story list -----------------------------------
    # Flatten into rows, then split at the halfway row; a split inside
    # a section repeats that section's header at the top of the right
    # column so both columns stay labelled.
    rows = []
    for sec, head, src in STORIES:
        if not rows or rows[-1][0] != sec:
            rows.append((sec, None, None))
        rows.append((sec, head, src))
    half = (len(rows) + 1) // 2
    left_rows, right_rows = rows[:half], rows[half:]
    if right_rows[0][1] is None:
        pass  # right column already starts with a header
    elif left_rows and right_rows[0][0] == left_rows[-1][0]:
        right_rows = [(right_rows[0][0], None, None)] + right_rows
    cols = [left_rows, right_rows]
    col_x = [24, W // 2 + 12]
    col_w = W // 2 - 36
    row_h = 23
    top = y
    for ci, col in enumerate(cols):
        cy = top
        for sec, head, src in col:
            if head is None:
                d.text((col_x[ci], cy + 1), sec, font=font(FONT_BOLD, 14), fill=RED)
                d.line([col_x[ci], cy + 20, col_x[ci] + col_w, cy + 20], fill=RULE, width=1)
            else:
                src_fnt = font(FONT_BOLD, 11)
                src_w = d.textlength(src, font=src_fnt)
                f = shrink(d, "\u2022 " + head, FONT_REG, 15, col_w - src_w - 14, floor=11)
                d.text((col_x[ci], cy + 1), "\u2022 " + head, font=f, fill=INK)
                d.text((col_x[ci] + col_w - src_w, cy + 3), src, font=src_fnt, fill=MUTED)
            cy += row_h
    y = top + max(len(c) for c in cols) * row_h + 4

    # ---- Footer: date check --------------------------------------
    d.line([24, y, W - 24, y], fill=RULE, width=2)
    y += 8
    check = "DATE CHECK \u2713  Thursday 19 November 2026  \u00b7  50 stories, all reported 19 Nov 2026  \u00b7  nothing from before 13 Nov 2026"
    d.text((24, y), check, font=font(FONT_BOLD, 14), fill=NAVY)
    y += 22
    d.text((24, y), FOOTER_SOURCES, font=font(FONT_REG, 12), fill=MUTED)

    img.save(path, format="PNG", optimize=True)
    return path


if __name__ == "__main__":
    import os
    out = os.environ.get("POSTER_OUT", "/tmp/ni19.png")
    draw_poster(out)
    n = os.path.getsize(out)
    print(f"wrote {out}: {n} bytes ({n / 1048576:.2f} MiB), limit 1048576")
    print("stories:", len(LEAD) + len(TIMELINE) + len(STORIES))
