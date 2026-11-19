import os, hashlib
from PIL import Image

uploaded = [
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858675919_f6bb360a.jpg',
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858678712_2aebc454.jpg',
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858681582_8a074e47.jpg',
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858683446_08564ea0.jpg',
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858686289_897b45d7.jpg'
]

for p in uploaded:
    with open(p, 'rb') as f:
        data = f.read()
    h = hashlib.md5(data).hexdigest()
    im = Image.open(p)
    print(f"{os.path.basename(p)}: size={im.size}, bytes={len(data)}, md5={h}")
