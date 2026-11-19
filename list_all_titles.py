import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', text)
for i, t in enumerate(titles):
    print(f"{i+1}: {t}")
