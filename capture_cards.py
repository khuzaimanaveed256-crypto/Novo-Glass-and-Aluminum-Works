# Let's inspect the cards currently in the file and index them by title
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all <article class="gallery-product-card">...</article>
articles = re.findall(r'<article class="gallery-product-card">.*?</article>', html, re.DOTALL)
print(f"Total articles found: {len(articles)}")

cards = {}
for a in articles:
    t_match = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', a)
    if t_match:
        title = t_match.group(1).replace('&amp;', '&').strip()
        cards[title] = a.strip()
        print(f"Captured: {title}")

print("\nAll 18 expected titles present?", len(cards))
