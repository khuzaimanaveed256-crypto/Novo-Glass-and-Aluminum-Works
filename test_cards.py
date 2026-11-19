import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate the area between the mirrors section end and the staircase section start
start_idx = text.find('<!-- ========================================================================\n         SECTION 3: BATHROOM SHOWER GLASS & PARTITIONS')
if start_idx == -1:
    start_idx = text.find('SECTION 3: BATHROOM SHOWER')
    start_idx = text.rfind('<!--', 0, start_idx)

end_idx = text.find('<!-- ========================================================================\n         SECTION 4: STAIRCASE GLASS & RAILINGS')
if end_idx == -1:
    end_idx = text.find('id="railings-staircases"')
    end_idx = text.rfind('<!--', 0, end_idx)

section_blob = text[start_idx:end_idx]
print(f"Captured blob from {start_idx} to {end_idx} (len {len(section_blob)})")

# Extract each article
articles = re.findall(r'<article class="gallery-product-card">.*?</article>', section_blob, re.DOTALL)
print(f"Total articles found: {len(articles)}")

cards_by_title = {}
for a in articles:
    t = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', a)
    if t:
        title = t.group(1).replace('&amp;', '&')
        cards_by_title[title] = a
        print("Found card:", title)

# Verify we have all 6
expected = [
    'Matte Black Framed Shower Cabin',
    'Frameless Double Walk-In Shower Suite',
    'Aluminum Grid Office Glass Partition',
    'Commercial Acoustic Glass Wall & Door',
    'Barn-Style Sliding Frosted Glass Door',
    'Tinted Sliding Glass Shower Cabin'
]

for exp in expected:
    match = any(exp in k for k in cards_by_title)
    print(f"Checking '{exp}': {match}")
