import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', text)
for i, t in enumerate(titles):
    print(i+1, t)

# Also show which section each title is in by checking context
print("\n\n=== SHOWER SECTION PRODUCTS ===")
idx = text.find('id="shower-partitions"')
end_idx = text.find('</section>', idx)
shower_text = text[idx:end_idx]
shower_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', shower_text)
for t in shower_titles:
    print("SHOWER:", t)

print("\n=== STAIRCASE SECTION PRODUCTS ===")
idx2 = text.find('id="railings-staircases"')
end_idx2 = text.find('</section>', idx2)
stair_text = text[idx2:end_idx2]
stair_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', stair_text)
for t in stair_titles:
    print("STAIRCASE:", t)
