import urllib.request
import re

url = "http://localhost:8000/"
try:
    resp = urllib.request.urlopen(url)
    html = resp.read().decode('utf-8')
    print("Server is UP, status:", resp.getcode())
except Exception as e:
    print("Server error:", e)
    exit(1)

# Verify all images
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags: {len(img_srcs)}")

broken = []
for src in set(img_srcs):
    clean = src.split('?')[0].split('#')[0]
    try:
        r = urllib.request.urlopen(url + clean)
        if r.getcode() != 200:
            broken.append((src, r.getcode()))
    except Exception as e:
        broken.append((src, str(e)))

if broken:
    print("Broken images found:", broken)
else:
    print(f"All {len(set(img_srcs))} unique images loaded successfully with HTTP 200!")
