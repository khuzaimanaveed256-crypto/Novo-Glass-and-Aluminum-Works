import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="railings-staircases"')
end_idx = text.find('</section>', idx)
stair_text = text[idx:end_idx]
stair_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', stair_text)
print(f'STAIRCASE TITLES ({len(stair_titles)}):')
for t in stair_titles:
    print(' -', t)

# Also check for any occurrences of those two cards in index.html
print("\nCheck occurrences in entire file:")
print('Panoramic Frameless Terrace Balustrade in file:', 'Panoramic Frameless Terrace Balustrade' in text)
print('Modern Minimalist Structural Glass Railing in file:', 'Modern Minimalist Structural Glass Railing' in text)
