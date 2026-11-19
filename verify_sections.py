import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = ['bathroom-showers', 'shower-partitions', 'railings-staircases', 'doors-windows']

for s_id in sections:
    idx = html.find(f'id="{s_id}"')
    end_idx = html.find('</section>', idx)
    titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', html[idx:end_idx])
    print(f"\nSection #{s_id} ({len(titles)} cards):")
    for t in titles:
        print(f"  - {t}")

print("\n--- NAV CHECK ---")
for line in html.splitlines():
    if 'nav-item' in line or 'drawer-link' in line:
        print(line.strip())
