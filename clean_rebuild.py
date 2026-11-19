import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

SHOWER_TITLES = {
    'Matte Black Framed Shower Cabin',
    'Frameless Double Walk-In Shower Suite',
    'Barn-Style Sliding Frosted Glass Door',
    'Tinted Sliding Glass Shower Cabin'
}

# 1. Find shower-partitions section bounds
sp_match = re.search(r'<section[^>]*id="shower-partitions"[^>]*>', html)
sp_open_start = sp_match.start()
sp_close_end = html.find('</section>', sp_match.end()) + len('</section>')

sp_inner = html[sp_open_start:sp_close_end]
print(f"shower-partitions section: [{sp_open_start}:{sp_close_end}] ({sp_close_end - sp_open_start} chars)")

# 2. Extract all article blocks from within the section
art_pattern = re.compile(
    r'([ \t]*<!--[^\n]*-->\s*)?(<article class="gallery-product-card">.*?</article>)',
    re.DOTALL
)
article_matches = list(art_pattern.finditer(sp_inner))
print(f"Found {len(article_matches)} article blocks")

shower_blocks = []
partition_blocks = []
for m in article_matches:
    block = m.group(0)
    title_m = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', block)
    title = title_m.group(1) if title_m else ''
    if title in SHOWER_TITLES:
        shower_blocks.append(block.strip())
        print(f"  SHOWER: {title}")
    else:
        partition_blocks.append(block.strip())
        print(f"  PARTITION: {title}")

# 3. Build new shower-partitions section with ONLY partition cards
def make_grid(cards, grid_class='gallery-products-grid'):
    items = '\n\n          '.join(cards)
    return f'''        <div class="{grid_class}">
          
          {items}

        </div>'''

partition_grid = make_grid(partition_blocks)
shower_grid = make_grid(shower_blocks)

new_sp_html = f'''<section class="section-gallery section-shower-partitions" id="shower-partitions" aria-label="Glass Partitions">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">ARCHITECTURAL GLASS SOLUTIONS</span>
          <h2 class="gallery-title">GLASS PARTITIONS &amp; OFFICE SYSTEMS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Modular glass partition systems for corporate offices, commercial interiors, and professional spaces. Engineered with acoustic-rated safety glass, slim aluminum framing, and precision hardware.
          </p>
        </div>

{partition_grid}
      </div>
    </section>'''

# 4. Build new bathroom-showers section
new_bs_html = f'''<!-- ========================================================================
         SECTION: BATHROOM SHOWERS
         ======================================================================== -->
    <section class="section-gallery section-bathroom-showers" id="bathroom-showers" aria-label="Bathroom Showers">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">PRECISION SHOWER INSTALLATIONS</span>
          <h2 class="gallery-title">BATHROOM SHOWERS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Bespoke frameless shower enclosures, tinted glass shower cabins, and sliding glass bathroom doors. Engineered with high-strength tempered safety glass, premium hardware fittings, and waterproof low-profile trays.
          </p>
        </div>

{shower_grid}
      </div>
    </section>

    '''

# 5. Replace shower-partitions section in html, prepending the new bathroom-showers section
html = html[:sp_open_start] + new_bs_html + new_sp_html + html[sp_close_end:]
print("\nReplaced shower-partitions and inserted bathroom-showers")

# 6. Update header navigation
old_nav = '''      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#shower-partitions" class="nav-item">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="nav-item">Glass Railings</a>
        <a href="#doors-windows" class="nav-item">Doors &amp; Windows</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>'''

new_nav = '''      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#bathroom-showers" class="nav-item">Bathroom Showers</a>
        <a href="#shower-partitions" class="nav-item">Glass Partitions</a>
        <a href="#railings-staircases" class="nav-item">Glass Railings</a>
        <a href="#doors-windows" class="nav-item">Doors &amp; Windows</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>'''

if old_nav in html:
    html = html.replace(old_nav, new_nav, 1)
    print("Updated header nav")
else:
    # Nav may have been updated already - check
    if 'href="#bathroom-showers"' in html:
        print("Header nav already has #bathroom-showers")
    else:
        print("WARNING: old_nav not found and no #bathroom-showers in nav!")

# 7. Update mobile drawer
old_drawer = '''      <nav class="drawer-nav">
        <a href="#hero" class="drawer-link">Home</a>
        <a href="#services" class="drawer-link">Our Services</a>
        <a href="#mirrors" class="drawer-link">LED Mirrors</a>
        <a href="#shower-partitions" class="drawer-link">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="drawer-link">Glass Railings</a>
        <a href="#doors-windows" class="drawer-link">Doors &amp; Windows</a>
        <a href="#collection-preview" class="drawer-link">Craftsmanship</a>
        <a href="#contact" class="drawer-link">Contact &amp; Location</a>
        <a href="#customModal" class="drawer-link open-modal-trigger">Request Custom Quote</a>
      </nav>'''

new_drawer = '''      <nav class="drawer-nav">
        <a href="#hero" class="drawer-link">Home</a>
        <a href="#services" class="drawer-link">Our Services</a>
        <a href="#mirrors" class="drawer-link">LED Mirrors</a>
        <a href="#bathroom-showers" class="drawer-link">Bathroom Showers</a>
        <a href="#shower-partitions" class="drawer-link">Glass Partitions</a>
        <a href="#railings-staircases" class="drawer-link">Glass Railings</a>
        <a href="#doors-windows" class="drawer-link">Doors &amp; Windows</a>
        <a href="#collection-preview" class="drawer-link">Craftsmanship</a>
        <a href="#contact" class="drawer-link">Contact &amp; Location</a>
        <a href="#customModal" class="drawer-link open-modal-trigger">Request Custom Quote</a>
      </nav>'''

if old_drawer in html:
    html = html.replace(old_drawer, new_drawer, 1)
    print("Updated mobile drawer nav")
else:
    if 'href="#bathroom-showers" class="drawer-link"' in html:
        print("Mobile drawer already has #bathroom-showers")
    else:
        print("WARNING: old_drawer not found!")

# 8. Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nSaved index.html")

# 9. Verify
print("\n=== VERIFICATION ===")

idx_bs = html.find('id="bathroom-showers"')
bs_end = html.find('</section>', idx_bs)
bs_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', html[idx_bs:bs_end])
print(f"\nBATHROOM SHOWERS ({len(bs_titles)} products):")
for t in bs_titles:
    print(f"  - {t}")

idx_sp = html.find('id="shower-partitions"')
sp_end = html.find('</section>', idx_sp)
sp_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', html[idx_sp:sp_end])
print(f"\nGLASS PARTITIONS ({len(sp_titles)} products):")
for t in sp_titles:
    print(f"  - {t}")

idx_rs = html.find('id="railings-staircases"')
rs_end = html.find('</section>', idx_rs)
rs_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', html[idx_rs:rs_end])
print(f"\nSTAIRCASE GLASS & RAILINGS ({len(rs_titles)} products):")
for t in rs_titles:
    print(f"  - {t}")

assert 'Panoramic Frameless Terrace Balustrade' not in ' '.join(rs_titles), "ERROR: Terrace Balustrade still in staircase!"
assert 'Modern Minimalist Structural Glass Railing' not in ' '.join(rs_titles), "ERROR: Minimalist Railing still in staircase!"
print("\nALL CHECKS PASSED!")
