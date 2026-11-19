with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = list(re.finditer(r'\.mirror-product-media[^{]*\{[^}]+\}', css))
for m in matches:
    print(m.group(0))
    print("-" * 50)
