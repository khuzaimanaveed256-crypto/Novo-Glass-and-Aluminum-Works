import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Locate railings-staircases section
idx_start = html.find('id="railings-staircases"')
# find comment before it
comment_idx = html.rfind('<!--', 0, idx_start)
end_idx = html.find('</section>', idx_start) + len('</section>')

section_blob = html[comment_idx:end_idx]

# Extract all cards
articles = re.findall(r'<article class="gallery-product-card">.*?</article>', section_blob, re.DOTALL)
assert len(articles) == 7, f"Expected 7 articles, got {len(articles)}"

cards_by_title = {}
for a in articles:
    t = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', a)
    if t:
        title = t.group(1).replace('&amp;', '&').strip()
        cards_by_title[title] = a.strip()

staircase_titles = [
    'Grand Curved Staircase Glass Balustrade',
    'Cantilever Staircase Smoked Glass Railing',
    'Smoked Glass Staircase with Pin Mounts',
    'Marble Staircase Black Post Glass Balustrade',
    'Clear Glass Staircase & Black Aluminum Rail'
]

balcony_titles = [
    'Cantilever Balcony Glass Railing with LED',
    'Spigot-Mounted Villa Balcony Balustrade'
]

for t in staircase_titles + balcony_titles:
    assert t in cards_by_title, f"Missing card: {t}"

staircase_cards_html = '\n\n          '.join([cards_by_title[t] for t in staircase_titles])
balcony_cards_html = '\n\n          '.join([cards_by_title[t] for t in balcony_titles])

# Section: Staircase Glass & Balustrades
staircase_section_html = f"""<!-- ========================================================================
         SECTION 5: STAIRCASE GLASS & BALUSTRADES
         ======================================================================== -->
    <section class="section-gallery section-staircase-glass" id="staircase-glass" aria-label="Staircase Glass & Balustrades">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">STRUCTURAL INTERIOR GLASS</span>
          <h2 class="gallery-title">STAIRCASE GLASS &amp; BALUSTRADES</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Precision-engineered curved glass balustrades, floating cantilever staircase railings, and modern point-supported glass steps. Designed for maximum architectural grandeur, structural rigidity, and uncompromised safety.
          </p>
        </div>

        <div class="gallery-products-grid gallery-products-grid-3 staircase-grid">
          
          {staircase_cards_html}

        </div>
      </div>
    </section>"""

# Section: Terrace & Balcony Glass Railings
balcony_section_html = f"""<!-- ========================================================================
         SECTION 6: TERRACE & BALCONY GLASS RAILINGS
         ======================================================================== -->
    <section class="section-gallery section-balcony-glass" id="balcony-glass" aria-label="Terrace & Balcony Glass Railings">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">EXTERIOR ARCHITECTURAL BALUSTRADES</span>
          <h2 class="gallery-title">TERRACE &amp; BALCONY GLASS RAILINGS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Heavy-duty exterior glass railings, cantilever balcony barriers with integrated LED profiles, and duplex marine-grade spigot systems. Built to withstand environmental exposure while maximizing panoramic outdoor vistas.
          </p>
        </div>

        <div class="gallery-products-grid gallery-products-grid-2 balcony-grid">
          
          {balcony_cards_html}

        </div>
      </div>
    </section>"""

replacement_sections = staircase_section_html + "\n\n    " + balcony_section_html

html = html[:comment_idx] + replacement_sections + html[end_idx:]

# 2. Update Header Navigation
nav_old = """      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#bathroom-showers" class="nav-item">Bathroom Showers</a>
        <a href="#shower-partitions" class="nav-item">Glass Partitions</a>
        <a href="#railings-staircases" class="nav-item">Glass Railings</a>
        <a href="#doors-windows" class="nav-item">Sliding Doors &amp; Windows</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>"""

nav_new = """      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#bathroom-showers" class="nav-item">Bathroom Showers</a>
        <a href="#shower-partitions" class="nav-item">Glass Partitions</a>
        <a href="#staircase-glass" class="nav-item">Staircase Glass</a>
        <a href="#balcony-glass" class="nav-item">Terrace &amp; Balcony Glass</a>
        <a href="#doors-windows" class="nav-item">Sliding Doors &amp; Windows</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>"""

assert nav_old in html, "nav_old not found in html"
html = html.replace(nav_old, nav_new, 1)

# 3. Update Drawer Navigation
drawer_old = """      <nav class="drawer-nav">
        <a href="#hero" class="drawer-link">Home</a>
        <a href="#services" class="drawer-link">Our Services</a>
        <a href="#mirrors" class="drawer-link">LED Mirrors</a>
        <a href="#bathroom-showers" class="drawer-link">Bathroom Showers</a>
        <a href="#shower-partitions" class="drawer-link">Glass Partitions</a>
        <a href="#railings-staircases" class="drawer-link">Glass Railings</a>
        <a href="#doors-windows" class="drawer-link">Sliding Doors &amp; Windows</a>
        <a href="#collection-preview" class="drawer-link">Craftsmanship</a>
        <a href="#contact" class="drawer-link">Contact &amp; Location</a>
        <a href="#customModal" class="drawer-link open-modal-trigger">Request Custom Quote</a>
      </nav>"""

drawer_new = """      <nav class="drawer-nav">
        <a href="#hero" class="drawer-link">Home</a>
        <a href="#services" class="drawer-link">Our Services</a>
        <a href="#mirrors" class="drawer-link">LED Mirrors</a>
        <a href="#bathroom-showers" class="drawer-link">Bathroom Showers</a>
        <a href="#shower-partitions" class="drawer-link">Glass Partitions</a>
        <a href="#staircase-glass" class="drawer-link">Staircase Glass</a>
        <a href="#balcony-glass" class="drawer-link">Terrace &amp; Balcony Glass</a>
        <a href="#doors-windows" class="drawer-link">Sliding Doors &amp; Windows</a>
        <a href="#collection-preview" class="drawer-link">Craftsmanship</a>
        <a href="#contact" class="drawer-link">Contact &amp; Location</a>
        <a href="#customModal" class="drawer-link open-modal-trigger">Request Custom Quote</a>
      </nav>"""

assert drawer_old in html, "drawer_old not found in html"
html = html.replace(drawer_old, drawer_new, 1)

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated with separate Staircase Glass and Terrace & Balcony Glass sections!")
