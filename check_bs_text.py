with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check section heading and text in #bathroom-showers
idx_bs = text.find('id="bathroom-showers"')
idx_bs_end = text.find('</section>', idx_bs)
print(text[idx_bs:idx_bs+800])
