#!/usr/bin/env python3
"""从物理作业照片中裁剪图表 - 扩大范围确保完整"""
from PIL import Image, ImageOps
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "diagrams")
os.makedirs(OUT, exist_ok=True)

def load(name):
    img = Image.open(os.path.join(BASE, name))
    return ImageOps.exif_transpose(img)

def crop(img, box, out_name):
    w, h = img.size
    box = (max(0,box[0]), max(0,box[1]), min(w,box[2]), min(h,box[3]))
    cropped = img.crop(box)
    path = os.path.join(OUT, out_name)
    cropped.save(path, quality=95)
    print(f"  {out_name}: {cropped.size}")

# === IMG_9580 - 页1 ===
img = load("IMG_9580.JPG")
crop(img, (2050, 400, 3500, 1150), "p1_snake.png")
crop(img, (250, 1650, 1500, 2200), "p1_carrier.png")
crop(img, (2200, 3500, 3500, 4500), "p1_circle.png")

# === IMG_9581 - 页2-3 ===
img = load("IMG_9581.JPG")
crop(img, (3000, 50, 4200, 750), "p2_axis.png")
crop(img, (2500, 700, 3700, 1500), "p2_vt.png")
crop(img, (50, 300, 800, 1400), "p3_setup.png")
crop(img, (950, 2700, 1900, 3700), "p3_photo.png")
crop(img, (50, 4300, 1000, 5300), "p3_gate.png")

# === IMG_9582 - 页4-5 ===
img = load("IMG_9582.JPG")
crop(img, (2500, 100, 3700, 1300), "p4_triangle.png")
crop(img, (50, 500, 700, 1400), "p5_xt.png")
crop(img, (400, 2700, 2100, 3800), "p5_table.png")

# === IMG_9583 - 页6-7 ===
img = load("IMG_9583.JPG")
crop(img, (2500, 1100, 3800, 2200), "p6_door.png")
crop(img, (2000, 2100, 3500, 3100), "p6_vt.png")
crop(img, (1100, 2500, 2500, 3700), "p7_gate.png")
crop(img, (50, 4100, 1800, 5500), "p7_table.png")

# === IMG_9584 - 页8-9 ===
img = load("IMG_9584.JPG")
crop(img, (2500, 50, 4200, 1100), "p8_expt.png")
crop(img, (1900, 1000, 4100, 2600), "p8_tape.png")
crop(img, (1300, 2400, 2500, 3400), "p9_figA.png")
crop(img, (1000, 3200, 2300, 4200), "p9_figB.png")

# === IMG_9585 - 页10-11 ===
img = load("IMG_9585.JPG")
crop(img, (2500, 200, 3800, 1100), "p10_plane.png")
crop(img, (100, 2700, 1800, 4300), "p11_relay.png")

# === IMG_9586 - 页12-13 ===
img = load("IMG_9586.JPG")
crop(img, (2000, 1700, 3500, 2900), "p12_vt.png")
crop(img, (150, 1300, 1200, 2700), "p12_photos.png")
crop(img, (1500, 3400, 2750, 4500), "p13_spring.png")

# === IMG_9587 - 页14 ===
img = load("IMG_9587.JPG")
crop(img, (1350, 0, 1900, 700), "p14_drop.png")
crop(img, (450, 2700, 1700, 3700), "p14_slide.png")

print("\n裁剪完成")
