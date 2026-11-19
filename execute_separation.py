import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Locate blob between mirrors section end and staircase section start
start_idx = html.find('<!-- ========================================================================\n         SECTION 3: BATHROOM SHOWER GLASS & PARTITIONS')
if start_idx == -1:
    start_idx = html.find('SECTION 3: BATHROOM SHOWER')
    start_idx = html.rfind('<!--', 0, start_idx)

end_idx = html.find('<!-- ========================================================================\n         SECTION 4: STAIRCASE GLASS & RAILINGS')
if end_idx == -1:
    end_idx = html.find('id="railings-staircases"')
    end_idx = html.rfind('<!--', 0, end_idx)

section_blob = html[start_idx:end_idx]

# Extract articles
articles = re.findall(r'<article class="gallery-product-card">.*?</article>', section_blob, re.DOTALL)
assert len(articles) == 6, f"Expected 6 articles, got {len(articles)}"

cards_by_title = {}
for a in articles:
    t = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', a)
    if t:
        title = t.group(1).replace('&amp;', '&').strip()
        cards_by_title[title] = a.strip()

shower_titles = [
    'Matte Black Framed Shower Cabin',
    'Frameless Double Walk-In Shower Suite',
    'Tinted Sliding Glass Shower Cabin',
    'Barn-Style Sliding Frosted Glass Door'
]

partition_titles = [
    'Aluminum Grid Office Glass Partition',
    'Commercial Acoustic Glass Wall & Door'
]

# Verify all are present
for t in shower_titles + partition_titles:
    assert t in cards_by_title, f"Missing card: {t}"

# Indent cards nicely
shower_cards_html = '\n\n          '.join([cards_by_title[t] for t in shower_titles])
partition_cards_html = '\n\n          '.join([cards_by_title[t] for t in partition_titles])

new_sections_html = f"""<!-- ========================================================================
         SECTION 3: BATHROOM SHOWERS
         ======================================================================== -->
    <section class="section-gallery section-bathroom-showers" id="bathroom-showers" aria-label="Bathroom Showers">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">LUXURY BATHROOM INSTALLATIONS</span>
          <h2 class="gallery-title">BATHROOM SHOWERS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Bespoke frameless shower enclosures, tinted glass cabins, walk-in suites, and sliding bathroom doors. Handcrafted with heavy tempered architectural safety glass and precision hardware fittings.
          </p>
        </div>

        <div class="gallery-products-grid">
          
          {shower_cards_html}

        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION: GLASS PARTITIONS & OFFICE SYSTEMS
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
    </section>

    """

html = html[:start_idx] + new_sections_html + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully!")
