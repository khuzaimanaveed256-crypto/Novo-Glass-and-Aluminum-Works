import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find where the shower/partition area begins and ends
start_pos = text.find('BATHROOM SHOWER GLASS &amp; PARTITIONS')
if start_pos == -1:
    start_pos = text.find('id="shower-partitions"')
# Find the start of the section or comment before it
comment_pos = text.rfind('<!--', 0, start_pos)
end_pos = text.find('</section>', start_pos) + len('</section>')

print(f"Area bounds: {comment_pos} to {end_pos}")
area_text = text[comment_pos:end_pos]

# Find all cards in this area
cards = re.findall(r'<article class="gallery-product-card">.*?</article>', area_text, re.DOTALL)
print(f"Total cards found in this area: {len(cards)}")

for i, card in enumerate(cards):
    title = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', card)
    tag = re.search(r'<span class="gallery-product-tag">([^<]+)</span>', card)
    img = re.search(r'<img[^>]+src="([^"]+)"', card)
    print(f"\nCard {i+1}:")
    print(f"  Title: {title.group(1) if title else 'N/A'}")
    print(f"  Tag:   {tag.group(1) if tag else 'N/A'}")
    print(f"  Img:   {img.group(1) if img else 'N/A'}")
