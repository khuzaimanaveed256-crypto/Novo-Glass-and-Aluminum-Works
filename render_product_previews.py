import os
from PIL import Image, ImageOps

products = [
    # Shower & Partitions
    ("shower-01-matte-black.jpg", "Matte Black Framed Shower Cabin", "assets/images/shower-01-matte-black.jpg"),
    ("shower-02-luxury-frameless.jpg", "Frameless Double Walk-In Shower Suite", "assets/images/shower-02-luxury-frameless.jpg"),
    ("partition-01-aluminum-office.jpg", "Aluminum Grid Office Glass Partition", "assets/images/partition-01-aluminum-office.jpg"),
    ("partition-02-acoustic-commercial.jpg", "Commercial Acoustic Glass Wall & Door", "assets/images/partition-02-acoustic-commercial.jpg"),
    # Railings & Balustrades
    ("railing-01-architectural-balcony.jpg", "Cantilever Balcony Glass Railing with LED", "assets/images/railing-01-architectural-balcony.jpg"),
    ("novo-glass-balcony.jpg", "Panoramic Frameless Terrace Balustrade", "assets/images/novo-glass-balcony.jpg"),
    ("novo-railing-balcony.jpg", "Modern Minimalist Structural Glass Railing", "assets/images/novo-railing-balcony.jpg"),
]

print("=== VERIFYING PRODUCT IMAGES INTEGRITY & METRICS ===")
for filename, title, path in products:
    assert os.path.exists(path), f"Missing: {path}"
    with Image.open(path) as im:
        w, h = im.size
        mode = im.mode
        aspect = w / h
        print(f"[{filename}] - {title}: {w}x{h} ({mode}), aspect ratio = {aspect:.2f}")

print("\n=== VERIFYING ALL 31 MIRRORS IN ASSETS/IMAGES ===")
for i in range(1, 28):
    m_path = f"assets/images/mirror-{i:02d}.jpg"
    assert os.path.exists(m_path), f"Missing mirror: {m_path}"
    with Image.open(m_path) as im:
        pass

for extra in ["mirror-calligraphy.jpg", "mirror-floral-custom.jpg", "mirror-geometric-pattern.jpg", "mirror-round-halo.jpg"]:
    e_path = f"assets/images/{extra}"
    assert os.path.exists(e_path), f"Missing mirror: {e_path}"
    with Image.open(e_path) as im:
        pass

print("ALL 31 MIRRORS verified intact and readable!")

# Generate preview composite of the 4 Shower & Partition products
w_card, h_card = 400, 320
composite_shower = Image.new("RGB", (w_card * 4 + 50, h_card + 40), (12, 12, 14))
for idx, (_, _, path) in enumerate(products[:4]):
    im = Image.open(path)
    thumb = ImageOps.fit(im, (w_card, h_card), method=Image.Resampling.LANCZOS)
    composite_shower.paste(thumb, (idx * (w_card + 10) + 10, 20))
composite_shower.save("preview_shower_partitions.png")
print("Saved preview_shower_partitions.png")

# Generate preview composite of the 3 Railing products
composite_railings = Image.new("RGB", (w_card * 3 + 40, h_card + 40), (10, 10, 12))
for idx, (_, _, path) in enumerate(products[4:]):
    im = Image.open(path)
    thumb = ImageOps.fit(im, (w_card, h_card), method=Image.Resampling.LANCZOS)
    composite_railings.paste(thumb, (idx * (w_card + 10) + 10, 20))
composite_railings.save("preview_railings.png")
print("Saved preview_railings.png")
