import urllib.request
import re

url = "http://localhost:8000/"
req = urllib.request.urlopen(url)
html = req.read().decode('utf-8')

img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags found: {len(img_srcs)}")

broken = []
success = 0
for src in img_srcs:
    clean_src = src.split('?')[0].split('#')[0]
    full_url = url + clean_src
    try:
        r = urllib.request.urlopen(full_url)
        if r.getcode() == 200:
            success += 1
        else:
            broken.append((src, r.getcode()))
    except Exception as e:
        broken.append((src, str(e)))

print(f"Successful image loads: {success}/{len(img_srcs)}")
if broken:
    print("Broken images:", broken)
else:
    print("ALL images loaded with HTTP 200!")
