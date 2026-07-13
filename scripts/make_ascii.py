from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path

# Usage: python scripts/make_ascii.py assets/profile.jpg
img_path = Path(__import__('sys').argv[1])
img = Image.open(img_path).convert('RGB')
img = ImageOps.fit(img, (512, 512), method=Image.Resampling.LANCZOS)
chars = "@%#*+=-:. "
gray = ImageOps.grayscale(img)
gray = ImageEnhance.Contrast(gray).enhance(1.55)
width = 42
height = int(width * gray.height / gray.width * 0.45)
gray = gray.resize((width, height), Image.Resampling.LANCZOS)
lines = []
for y in range(height):
    line = ""
    for x in range(width):
        p = gray.getpixel((x, y))
        idx = int(p / 255 * (len(chars) - 1))
        line += chars[idx]
    lines.append(line.rstrip())
print("\n".join(lines))
