with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .section-doors-windows .gallery-products-grid to 4 columns on desktop
old_dw_grid = """.section-doors-windows .gallery-products-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.2rem;
  width: 100%;
}"""

new_dw_grid = """.section-doors-windows .gallery-products-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  width: 100%;
}"""

assert old_dw_grid in css, "old_dw_grid not found"
css = css.replace(old_dw_grid, new_dw_grid, 1)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with 4-column layout for doors & windows!")
