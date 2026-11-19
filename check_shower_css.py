with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Search for section-bathroom-showers or shower styling in style.css
for line in css.splitlines():
    if 'bathroom-showers' in line or 'shower-cabins' in line:
        print(line)
