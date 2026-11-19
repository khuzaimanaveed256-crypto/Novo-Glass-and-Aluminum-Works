from PIL import Image, ImageOps

target_w, target_h = 380, 480

for name, f in [
    ("shower1", "assets/images/shower-01-matte-black.jpg"),
    ("shower2", "assets/images/shower-02-luxury-frameless.jpg"),
    ("shower3", "assets/images/shower-03-tinted-sliding-cabin.jpg")
]:
    im = Image.open(f)
    # contain simulation: scale to fit within (target_w-16, target_h-16) keeping aspect ratio
    bg = Image.new("RGB", (target_w, target_h), (12, 12, 14))
    im_fit = ImageOps.contain(im, (target_w - 16, target_h - 16), method=Image.Resampling.LANCZOS)
    x = (target_w - im_fit.width) // 2
    y = (target_h - im_fit.height) // 2
    bg.paste(im_fit, (x, y))
    bg.save(f"scratch/test_{name}_contain.png")
    print(f"Saved test_{name}_contain.png: image size={im_fit.size}, pasted at ({x}, {y})")
