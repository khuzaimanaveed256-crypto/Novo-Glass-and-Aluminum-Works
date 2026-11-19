import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', text)
print('Sections:', sections)

# Inspect #bathroom-showers
idx_bs = text.find('id="bathroom-showers"')
idx_bs_end = text.find('</section>', idx_bs)
print("\n--- BATHROOM SHOWERS SECTION ---")
print(text[idx_bs:idx_bs+500])
bs_cards = re.findall(r'<article class="gallery-product-card">.*?</article>', text[idx_bs:idx_bs_end], re.DOTALL)
print(f"Total cards in bathroom-showers: {len(bs_cards)}")
for i, c in enumerate(bs_cards):
    title = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', c)
    img = re.search(r'<img[^>]+src="([^"]+)"', c)
    print(f"Card {i+1}: {title.group(1) if title else 'N/A'} | {img.group(1) if img else 'N/A'}")

# Inspect #doors-windows
idx_dw = text.find('id="doors-windows"')
idx_dw_end = text.find('</section>', idx_dw)
print("\n--- DOORS & WINDOWS SECTION ---")
print(text[idx_dw:idx_dw+500])
dw_cards = re.findall(r'<article class="gallery-product-card">.*?</article>', text[idx_dw:idx_dw_end], re.DOTALL)
print(f"Total cards in doors-windows: {len(dw_cards)}")
for i, c in enumerate(dw_cards):
    title = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', c)
    img = re.search(r'<img[^>]+src="([^"]+)"', c)
    print(f"Card {i+1}: {title.group(1) if title else 'N/A'} | {img.group(1) if img else 'N/A'}")
