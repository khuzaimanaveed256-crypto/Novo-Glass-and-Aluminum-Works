with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.section-doors-windows .gallery-products-grid')
print(css[idx:idx+350])
