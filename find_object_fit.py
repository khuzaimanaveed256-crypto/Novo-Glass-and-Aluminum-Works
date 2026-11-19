with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
# Find all occurrences of object-fit
matches = re.finditer(r'([^{}]*object-fit\s*:[^;]+;[^{}]*)', css)
for m in matches:
    # Print the selector context
    start = css.rfind('{', 0, m.start())
    sel_start = css.rfind('\n', 0, start)
    selector = css[sel_start:start].strip()
    rule = m.group(0).strip()
    print(f"SELECTOR: {selector}\n  -> {rule}\n")
