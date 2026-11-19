with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="collection-preview"')
idx_end = html.find('</section>', idx) + len('</section>')
print(html[idx:idx_end])
