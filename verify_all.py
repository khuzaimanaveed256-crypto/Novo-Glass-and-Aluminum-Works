import re
import urllib.request

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check sections
sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', html)
print("Sections found:", sections)

expected_sections = [
    'hero',
    'services',
    'mirrors',
    'bathroom-showers',
    'shower-partitions',
    'railings-staircases',
    'doors-windows',
    'collection-preview',
    'contact'
]
assert sections == expected_sections, f"Sections mismatch!\nFound: {sections}\nExpected: {expected_sections}"

# 2. Check Bathroom Showers products
idx_bs = html.find('id="bathroom-showers"')
idx_bs_end = html.find('</section>', idx_bs)
bs_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', html[idx_bs:idx_bs_end])
print("\nBATHROOM SHOWERS titles (count = " + str(len(bs_titles)) + "):")
for t in bs_titles:
    print(" -", t)
assert len(bs_titles) == 4, f"Expected 4 shower titles, got {len(bs_titles)}"

# 3. Check Partitions products
idx_sp = html.find('id="shower-partitions"')
idx_sp_end = html.find('</section>', idx_sp)
sp_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', html[idx_sp:idx_sp_end])
print("\nGLASS PARTITIONS titles (count = " + str(len(sp_titles)) + "):")
for t in sp_titles:
    print(" -", t)
assert len(sp_titles) == 2, f"Expected 2 partition titles, got {len(sp_titles)}"

# 4. Check Staircase products
idx_rs = html.find('id="railings-staircases"')
idx_rs_end = html.find('</section>', idx_rs)
rs_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', html[idx_rs:idx_rs_end])
print("\nSTAIRCASE & RAILINGS titles (count = " + str(len(rs_titles)) + "):")
for t in rs_titles:
    print(" -", t)

# Verify the two removed cards are NOT present
assert 'Panoramic Frameless Terrace Balustrade' not in html, "Panoramic Frameless Terrace Balustrade still in file!"
assert 'Modern Minimalist Structural Glass Railing' not in html, "Modern Minimalist Structural Glass Railing still in file!"
print("\nCONFIRMED: The two targeted staircase cards are REMOVED!")

# 5. Check Navigation
assert 'href="#bathroom-showers"' in html, "href=#bathroom-showers missing from nav!"
assert 'href="#shower-partitions"' in html, "href=#shower-partitions missing from nav!"
assert 'href="#railings-staircases"' in html, "href=#railings-staircases missing from nav!"
print("CONFIRMED: All navigation links are present and correct!")

# 6. Check HTTP status of all images
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"\nChecking all {len(img_srcs)} image tags across site:")
broken = []
for src in set(img_srcs):
    clean = src.split('?')[0].split('#')[0]
    try:
        req = urllib.request.urlopen("http://localhost:8000/" + clean)
        if req.getcode() != 200:
            broken.append((src, req.getcode()))
    except Exception as e:
        broken.append((src, str(e)))

if broken:
    print("BROKEN IMAGES:", broken)
    exit(1)
else:
    print(f"ALL {len(set(img_srcs))} unique images returned HTTP 200 OK!")

print("\n=== ALL VERIFICATIONS PASSED SUCCESSFULLY! ===")
