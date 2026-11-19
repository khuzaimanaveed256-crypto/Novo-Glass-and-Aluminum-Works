import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="railings-staircases"')
end_idx = html.find('</section>', idx)
section_text = html[idx:end_idx]

articles = re.findall(r'<article class="gallery-product-card">.*?</article>', section_text, re.DOTALL)
print(f"Total articles in railings-staircases: {len(articles)}")
for i, a in enumerate(articles):
    t = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', a)
    img = re.search(r'<img[^>]+src="([^"]+)"', a)
    print(f"Card {i+1}: {t.group(1) if t else 'N/A'} | {img.group(1) if img else 'N/A'}")
