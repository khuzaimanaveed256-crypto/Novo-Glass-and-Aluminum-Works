import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all cards
articles = re.findall(r'<article class="gallery-product-card">.*?</article>', html, re.DOTALL)
cards = {}
for a in articles:
    t_match = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', a)
    if t_match:
        title = t_match.group(1).replace('&amp;', '&').strip()
        cards[title] = a.strip()

# 1. Bathroom Showers (3 cards)
shower_titles = [
    'Matte Black Framed Shower Cabin',
    'Frameless Double Walk-In Shower Suite',
    'Tinted Sliding Glass Shower Cabin'
]
shower_cards_html = '\n\n          '.join([cards[t] for t in shower_titles])

bathroom_showers_section = f"""<!-- ========================================================================
         SECTION 3: BATHROOM SHOWERS
         ======================================================================== -->
    <section class="section-gallery section-bathroom-showers" id="bathroom-showers" aria-label="Bathroom Showers">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">LUXURY BATHROOM INSTALLATIONS</span>
          <h2 class="gallery-title">BATHROOM SHOWERS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Bespoke frameless shower enclosures, tinted glass shower cabins, and luxury walk-in suites. Handcrafted with heavy tempered architectural safety glass, precision hardware fittings, and waterproof base profiles.
          </p>
        </div>

        <div class="gallery-products-grid gallery-products-grid-3 shower-cabins-grid">
          
          {shower_cards_html}

        </div>
      </div>
    </section>"""

# 2. Glass Partitions (2 cards)
partition_titles = [
    'Aluminum Grid Office Glass Partition',
    'Commercial Acoustic Glass Wall & Door'
]
partition_cards_html = '\n\n          '.join([cards[t] for t in partition_titles])

glass_partitions_section = f"""<!-- ========================================================================
         SECTION 4: GLASS PARTITIONS & OFFICE SYSTEMS
         ======================================================================== -->
    <section class="section-gallery section-shower-partitions" id="shower-partitions" aria-label="Glass Partitions">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">ARCHITECTURAL ACOUSTIC SYSTEMS</span>
          <h2 class="gallery-title">GLASS PARTITIONS &amp; OFFICE SYSTEMS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Modular acoustic glass walls, commercial entrance systems, and frosted privacy partitions engineered for modern executive suites and corporate workspaces.
          </p>
        </div>

        <div class="gallery-products-grid">
          
          {partition_cards_html}

        </div>
      </div>
    </section>"""

# 3. Staircase Glass & Railings (7 cards)
staircase_titles = [
    'Grand Curved Staircase Glass Balustrade',
    'Cantilever Staircase Smoked Glass Railing',
    'Cantilever Balcony Glass Railing with LED',
    'Spigot-Mounted Villa Balcony Balustrade',
    'Smoked Glass Staircase with Pin Mounts',
    'Marble Staircase Black Post Glass Balustrade',
    'Clear Glass Staircase & Black Aluminum Rail'
]
staircase_cards_html = '\n\n          '.join([cards[t] for t in staircase_titles])

staircase_section = f"""<!-- ========================================================================
         SECTION 5: STAIRCASE GLASS & RAILINGS
         ======================================================================== -->
    <section class="section-gallery section-railings-staircases" id="railings-staircases" aria-label="Staircase Glass & Railings">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">STRUCTURAL BALUSTRADES &amp; STAIRWAYS</span>
          <h2 class="gallery-title">STAIRCASE GLASS &amp; RAILINGS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Engineered curved and straight staircase glass balustrades, floating cantilever barriers, and exterior panoramic railings. Designed to deliver uncompromised architectural elegance, safety compliance, and luminous openness.
          </p>
        </div>

        <div class="gallery-products-grid gallery-products-grid-3">
          
          {staircase_cards_html}

        </div>
      </div>
    </section>"""

# 4. Sliding Doors, Windows & Aluminum Systems (6 cards)
doors_titles = [
    'Luxury Aluminum Bi-Fold Glass Doors',
    'Barn-Style Sliding Frosted Glass Door',
    'Triple-Track Aluminum Sliding Patio Doors',
    'Architectural Sliding Glass Terrace Doors',
    'Slimline Black Aluminum Glass French Door',
    'Champagne Bronze Aluminum Window System'
]
doors_cards_html = '\n\n          '.join([cards[t] for t in doors_titles])

doors_section = f"""<!-- ========================================================================
         SECTION 6: SLIDING DOORS & ALUMINUM SYSTEMS
         ======================================================================== -->
    <section class="section-gallery section-doors-windows" id="doors-windows" aria-label="Sliding Doors & Aluminum Systems">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">ARCHITECTURAL SLIDING &amp; ENTRANCE SYSTEMS</span>
          <h2 class="gallery-title">SLIDING DOORS &amp; ALUMINUM SYSTEMS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Precision-engineered architectural sliding glass doors, barn-style interior sliding doors, bi-fold patio systems, and high-performance insulated window frames. Crafted for seamless indoor-outdoor transitions and luxury modern living.
          </p>
        </div>

        <div class="gallery-products-grid gallery-products-grid-3">
          
          {doors_cards_html}

        </div>
      </div>
    </section>"""

# Reconstruct all 4 sections combined
all_four_sections = "\n\n    " + "\n\n    ".join([
    bathroom_showers_section,
    glass_partitions_section,
    staircase_section,
    doors_section
]) + "\n\n    "

# Find boundaries in existing html:
# From end of mirrors section to start of collection-preview section
mirrors_end_idx = html.find('</section>', html.find('id="mirrors"')) + len('</section>')
glance_start_idx = html.find('id="collection-preview"')
# Find comment before collection-preview
glance_comment_idx = html.rfind('<!--', 0, glance_start_idx)

new_html = html[:mirrors_end_idx] + all_four_sections + html[glance_comment_idx:]

# Update navigation links
new_html = new_html.replace(
    '<a href="#doors-windows" class="nav-item">Doors &amp; Windows</a>',
    '<a href="#doors-windows" class="nav-item">Sliding Doors &amp; Windows</a>'
)
new_html = new_html.replace(
    '<a href="#doors-windows" class="drawer-link">Doors &amp; Windows</a>',
    '<a href="#doors-windows" class="drawer-link">Sliding Doors &amp; Windows</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully reconstructed index.html!")
