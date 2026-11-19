import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# verify #bathroom-showers section exists and has the right products
idx_showers = html.find('id="bathroom-showers"')
idx_showers_end = html.find('</section>', idx_showers)
shower_section = html[idx_showers:idx_showers_end]
shower_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', shower_section)
print("BATHROOM SHOWERS section products:")
for t in shower_titles:
    print(" -", t)

# verify #shower-partitions section only has partition products
idx_part = html.find('id="shower-partitions"')
idx_part_end = html.find('</section>', idx_part)
part_section = html[idx_part:idx_part_end]
part_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', part_section)
print("\nGLASS PARTITIONS section products:")
for t in part_titles:
    print(" -", t)

# verify #railings-staircases section no longer has the two deleted products
idx_rail = html.find('id="railings-staircases"')
idx_rail_end = html.find('</section>', idx_rail)
rail_section = html[idx_rail:idx_rail_end]
rail_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', rail_section)
print("\nSTAIRCASE GLASS & RAILINGS section products:")
for t in rail_titles:
    print(" -", t)

assert 'Panoramic Frameless Terrace Balustrade' not in ' '.join(rail_titles), "ERROR: Terrace Balustrade still in staircase section!"
assert 'Modern Minimalist Structural Glass Railing' not in ' '.join(rail_titles), "ERROR: Minimalist Railing still in staircase section!"
print("\nCONFIRMED: Both targeted cards removed from staircase section!")

# check nav has bathroom-showers
assert 'href="#bathroom-showers"' in html, "ERROR: #bathroom-showers missing from nav!"
print("CONFIRMED: #bathroom-showers is in navigation!")

print("\nAll checks PASSED!")
