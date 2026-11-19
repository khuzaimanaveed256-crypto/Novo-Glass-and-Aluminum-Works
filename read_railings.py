with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="railings-staircases"')
end_idx = text.find('</section>', idx) + len('</section>')
print("Found section len:", end_idx - idx)
print(text[idx:idx+400])
