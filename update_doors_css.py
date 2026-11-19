css_additions = """
/* Section Doors & Windows styling continuity */
.section-doors-windows {
  background: #09090b;
  background: radial-gradient(circle at 50% 0%, rgba(198, 164, 91, 0.04) 0%, rgba(9, 9, 11, 0.99) 70%);
  border-top: 1px solid rgba(198, 164, 91, 0.12);
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    style_content = f.read()

if '.section-doors-windows' not in style_content:
    with open('css/style.css', 'a', encoding='utf-8') as f:
        f.write("\n" + css_additions)
    print("Added .section-doors-windows to style.css")
else:
    print(".section-doors-windows already in style.css")
