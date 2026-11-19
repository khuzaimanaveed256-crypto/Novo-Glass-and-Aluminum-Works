with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="shower-partitions"')
print(repr(text[idx-150:idx+250]))
