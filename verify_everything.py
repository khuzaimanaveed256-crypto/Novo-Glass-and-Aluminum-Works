import re
import urllib.request

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Sections list
sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', html)
print("Sections found in DOM order:")
for s in sections:
    print(f"  - #{s}")

expected_sections = [
    'hero',
    'services',
    'mirrors',
    'bathroom-showers',
    'shower-partitions',
    'staircase-glass',
    'balcony-glass',
    'doors-windows',
    'collection-preview',
    'contact'
]
assert sections == expected_sections, f"Sections mismatch!\nFound: {sections}\nExpected: {expected_sections}"

# 2. Check each product section
product_sections = {
    'bathroom-showers': 3,
    'shower-partitions': 4,
    'staircase-glass': 6,
    'balcony-glass': 2,
    'doors-windows': 8
}

for s_id, count in product_sections.items():
    idx = html.find(f'id="{s_id}"')
    end_idx = html.find('</section>', idx)
    titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', html[idx:end_idx])
    print(f"\n#{s_id} ({len(titles)} cards, expected {count}):")
    for t in titles:
        print(f"  * {t}")
    assert len(titles) == count, f"Mismatch in #{s_id}: got {len(titles)}, expected {count}"

# 3. Check mirrors
idx_m = html.find('id="mirrors"')
end_m = html.find('</section>', idx_m)
mirror_titles = re.findall(r'<h3 class="mirror-product-title">([^<]+)</h3>', html[idx_m:end_m])
print(f"\n#mirrors: {len(mirror_titles)} mirror cards")
assert len(mirror_titles) == 31, f"Expected 31 mirrors, got {len(mirror_titles)}"

# 4. Check Navigation
print("\n--- Header Nav Links ---")
header_nav = re.search(r'<nav class="nav-links"[^>]*>.*?</nav>', html, re.DOTALL).group(0)
for m in re.finditer(r'<a href="([^"]+)"[^>]*>([^<]+)</a>', header_nav):
    print(f"  {m.group(1)} -> {m.group(2)}")

assert 'href="#staircase-glass"' in header_nav
assert 'href="#balcony-glass"' in header_nav
assert 'href="#bathroom-showers"' in header_nav
assert 'href="#shower-partitions"' in header_nav
assert 'href="#doors-windows"' in header_nav

# 5. Check HTTP 200 for all images
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

print("\n=== ALL COMPREHENSIVE VERIFICATIONS PASSED! ===")
