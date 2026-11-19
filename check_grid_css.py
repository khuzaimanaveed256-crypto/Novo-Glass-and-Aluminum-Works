with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's check the rules for doors-windows and shower-partitions
for term in ['.section-doors-windows', '.section-shower-partitions']:
    idx = css.find(term)
    print(f"=== {term} ===")
    print(css[idx:idx+350])
