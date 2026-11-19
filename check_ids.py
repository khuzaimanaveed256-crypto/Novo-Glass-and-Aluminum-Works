import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

hits = [(m.start(), m.group()) for m in re.finditer(r'id="([^"]+)"', text) if 'shower' in m.group() or 'bath' in m.group()]
print("All shower/bath related id attrs:")
for pos, h in hits:
    print(f"  pos={pos}: {h}")

# Check if bathroom-showers section exists
print("\nbathroom-showers in html:", 'id="bathroom-showers"' in text)
print("shower-partitions in html:", 'id="shower-partitions"' in text)
