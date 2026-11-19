from PIL import Image

for f in ['assets/images/shower-01-matte-black.jpg', 'assets/images/shower-02-luxury-frameless.jpg', 'assets/images/shower-03-tinted-sliding-cabin.jpg']:
    im = Image.open(f)
    w, h = im.size
    print(f"{f}: {w}x{h}, aspect={w/h:.3f}, inverted={h/w:.3f}")
