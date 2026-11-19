with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("=== NAVIGATION LINKS ===")
for m in re.finditer(r'<a\s+href="([^"]+)"\s+class="(?:nav-item|drawer-link)[^"]*"[^>]*>([^<]+)</a>', html):
    print(f"{m.group(1)} -> {m.group(2)}")
