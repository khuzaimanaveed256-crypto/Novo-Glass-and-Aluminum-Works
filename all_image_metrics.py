import re
from PIL import Image

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', html)
print(f"Total img tags: {len(img_tags)}")

for src, alt in img_tags:
    clean = src.split('?')[0].split('#')[0]
    if clean.endswith('.svg'):
        continue
    try:
        im = Image.open(clean)
        w, h = im.size
        print(f"[{clean}] {w}x{h} (ratio {w/h:.2f}) | {alt[:40]}")
    except Exception as e:
        print(f"[{clean}] ERROR: {e}")
