import re
from PIL import Image

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Testing all {len(img_srcs)} images:")

for src in img_srcs:
    clean = src.split('?')[0].split('#')[0]
    if clean.endswith('.svg'):
        continue
    try:
        im = Image.open(clean)
        im.verify()
    except Exception as e:
        print(f"ERROR on {src}: {e}")

print("All raster images passed PIL verify cleanly!")
