with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

rule = """
/* Section Bathroom Showers styling continuity */
.section-bathroom-showers {
  background: #0d0d0f;
  background: radial-gradient(circle at 50% 0%, rgba(198, 164, 91, 0.045) 0%, rgba(13, 13, 15, 0.99) 70%);
  border-top: 1px solid rgba(198, 164, 91, 0.12);
}
"""

if '.section-bathroom-showers' not in css:
    with open('css/style.css', 'a', encoding='utf-8') as f:
        f.write("\n" + rule)
    print("Added .section-bathroom-showers to css/style.css")
else:
    print(".section-bathroom-showers already in css/style.css")
