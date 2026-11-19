with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
header_nav = re.search(r'<nav class="nav-links"[^>]*>.*?</nav>', text, re.DOTALL)
if header_nav:
    print("HEADER NAV:")
    print(header_nav.group(0))

drawer_nav = re.search(r'<nav class="drawer-nav"[^>]*>.*?</nav>', text, re.DOTALL)
if drawer_nav:
    print("\nDRAWER NAV:")
    print(drawer_nav.group(0))
