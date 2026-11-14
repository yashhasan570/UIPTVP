#!/usr/bin/env python3
"""Rebuild the UIPTVP icon set from scripts/icons/badge.png."""
import os, sys
from PIL import Image, ImageDraw, ImageFilter

root = sys.argv[1] if len(sys.argv) > 1 else "."
os.chdir(root)
res = "app/src/main/res"
src = Image.open(os.path.join("scripts", "icons", "badge.png")).convert("RGBA")
NAVY = (11, 15, 25, 255)

def sharp(img, pct):
    return img.filter(ImageFilter.UnsharpMask(radius=2, percent=pct, threshold=2))

def on_navy(size, pct=70):
    canvas = Image.new("RGBA", (size, size), NAVY)
    canvas.alpha_composite(sharp(src.resize((size, size), Image.LANCZOS), pct))
    return canvas

fg = Image.new("RGBA", (432, 432), NAVY)
inner = sharp(src.resize((300, 300), Image.LANCZOS), 70)
fg.alpha_composite(inner, ((432 - 300) // 2, (432 - 300) // 2))
fg.convert("RGB").save(res + "/drawable/ic_logo_fg.png")
on_navy(256).save(res + "/drawable/ic_brand_mark.png")
for dpi, size in [("mdpi", 48), ("hdpi", 72), ("xhdpi", 96), ("xxhdpi", 144), ("xxxhdpi", 192)]:
    sq = on_navy(size, 110 if size <= 96 else 80)
    sq.save(res + "/mipmap-%s/ic_launcher.webp" % dpi, "WEBP", quality=95)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    rnd = sq.copy()
    rnd.putalpha(mask)
    rnd.save(res + "/mipmap-%s/ic_launcher_round.webp" % dpi, "WEBP", quality=95)
banner = Image.new("RGB", (640, 360), (11, 15, 25))
b = sharp(src.resize((330, 330), Image.LANCZOS), 70).convert("RGB")
banner.paste(b, ((640 - 330) // 2, (360 - 330) // 2))
banner.save(res + "/drawable/banner.png")
print("icons installed")
