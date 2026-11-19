import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ===========================================================================
# STEP 1: Remove two specific staircase cards from #railings-staircases:
#   - "Panoramic Frameless Terrace Balustrade" (novo-glass-balcony.jpg)
#   - "Modern Minimalist Structural Glass Railing" (novo-railing-balcony.jpg)
# ===========================================================================

def remove_article_block(html, comment_marker):
    """Find and remove an <article>...</article> block identified by a comment right before it."""
    idx_comment = html.find(comment_marker)
    if idx_comment == -1:
        raise ValueError(f"Comment marker not found: {comment_marker!r}")
    # find the <article> start after the comment
    idx_article_start = html.find('<article', idx_comment)
    if idx_article_start == -1:
        raise ValueError(f"No <article> after comment: {comment_marker!r}")
    # find the matching </article>
    idx_article_end = html.find('</article>', idx_article_start) + len('</article>')
    # remove the comment + whitespace before article + the article itself
    # remove from comment start to article end
    removed = html[idx_comment:idx_article_end]
    # also strip up to 2 leading newlines before the comment
    new_html = html[:idx_comment].rstrip('\n') + '\n' + html[idx_article_end:]
    print(f"REMOVED block ({len(removed)} chars): starting with {removed[:80]!r}")
    return new_html

# Remove "Panoramic Frameless Terrace Balustrade" card
html = remove_article_block(html, '<!-- Railing 02 (Terrace Balustrade) -->')
print()

# Remove "Modern Minimalist Structural Glass Railing" card
html = remove_article_block(html, '<!-- Railing 03 (Post & Clamp System) -->')
print()

# ===========================================================================
# STEP 2: Identify shower products in #shower-partitions
# Shower products: Matte Black Framed Shower Cabin, Frameless Double Walk-In Shower Suite,
#                  Barn-Style Sliding Frosted Glass Door, Tinted Sliding Glass Shower Cabin
# Partition products: Aluminum Grid Office Glass Partition, Commercial Acoustic Glass Wall & Door
# ===========================================================================

# Extract full shower section
idx_shower = html.find('id="shower-partitions"')
idx_shower_end = html.find('</section>', idx_shower) + len('</section>')
shower_section_html = html[idx_shower:idx_shower_end]

# Extract all article blocks from the shower section
article_blocks = re.findall(
    r'(<!--[^-]*?-->\s*<article class="gallery-product-card">.*?</article>)',
    shower_section_html,
    re.DOTALL
)

print(f"Found {len(article_blocks)} article blocks in shower section:")
for i, block in enumerate(article_blocks):
    title = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', block)
    print(f"  {i+1}. {title.group(1) if title else '???'}")

# Categorize: shower ones go to new section, partition ones stay in partitions section
SHOWER_TITLES = {
    'Matte Black Framed Shower Cabin',
    'Frameless Double Walk-In Shower Suite',
    'Barn-Style Sliding Frosted Glass Door',
    'Tinted Sliding Glass Shower Cabin'
}

shower_cards = []
partition_cards = []

for block in article_blocks:
    title_match = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', block)
    title = title_match.group(1) if title_match else ''
    if title in SHOWER_TITLES:
        shower_cards.append(block)
    else:
        partition_cards.append(block)

print(f"\nShower cards to move: {len(shower_cards)}")
print(f"Partition cards to keep: {len(partition_cards)}")

# ===========================================================================
# STEP 3: Rebuild #shower-partitions section with ONLY partition cards
# ===========================================================================

partition_grid_content = '\n\n          '.join(partition_cards)

new_partitions_section = f"""<section class="section-gallery section-shower-partitions" id="shower-partitions" aria-label="Glass Partitions">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">ARCHITECTURAL GLASS SOLUTIONS</span>
          <h2 class="gallery-title">GLASS PARTITIONS &amp; OFFICE SYSTEMS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Modular glass partition systems for corporate offices, commercial interiors, and professional spaces. Engineered with acoustic-rated safety glass, slim aluminum framing, and precision hardware.
          </p>
        </div>

        <div class="gallery-products-grid">
          
          {partition_grid_content}

        </div>
      </div>
    </section>"""

# Replace the old shower-partitions section in html
html = html[:idx_shower - len('<section class="section-gallery section-shower-partitions" ')] \
    + '' + html[idx_shower:]
# More precise replacement: replace entire section
# Find the start of the <section> tag that contains id="shower-partitions"
section_start_match = re.search(r'<section[^>]*id="shower-partitions"[^>]*>', html)
if section_start_match:
    sec_tag_start = section_start_match.start()
    # find from the beginning of the line
    line_start = html.rfind('\n', 0, sec_tag_start) + 1
    # Find end of section
    sec_end = html.find('</section>', sec_tag_start) + len('</section>')
    old_section = html[line_start:sec_end]
    html = html[:line_start] + '    ' + new_partitions_section + html[sec_end:]
    print(f"\nReplaced partition section (len {len(old_section)} -> {len(new_partitions_section)})")

# ===========================================================================
# STEP 4: Build new BATHROOM SHOWERS section and insert it BEFORE partitions
# ===========================================================================

shower_grid_content = '\n\n          '.join(shower_cards)

new_shower_section = f"""<!-- ========================================================================
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

        <div class="gallery-products-grid">
          
          {shower_grid_content}

        </div>
      </div>
    </section>

    """

# Insert the new shower section before the partitions section
# Find the partitions section again (it may have moved after replacement)
section_start_match2 = re.search(r'<section[^>]*id="shower-partitions"[^>]*>', html)
if section_start_match2:
    insert_pos = section_start_match2.start()
    # find line start
    line_start2 = html.rfind('\n', 0, insert_pos) + 1
    html = html[:line_start2] + new_shower_section + html[line_start2:]
    print("Inserted new #bathroom-showers section before #shower-partitions")

# ===========================================================================
# STEP 5: Update navigation — header and mobile drawer
# ===========================================================================

# Update header nav
old_nav = """      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#shower-partitions" class="nav-item">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="nav-item">Glass Railings</a>
        <a href="#doors-windows" class="nav-item">Doors &amp; Windows</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>"""

new_nav = """      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#bathroom-showers" class="nav-item">Bathroom Showers</a>
        <a href="#shower-partitions" class="nav-item">Glass Partitions</a>
        <a href="#railings-staircases" class="nav-item">Glass Railings</a>
        <a href="#doors-windows" class="nav-item">Doors &amp; Windows</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>"""

assert old_nav in html, "old_nav NOT FOUND in html"
html = html.replace(old_nav, new_nav, 1)
print("Updated header nav")

# Update mobile drawer
old_drawer = """      <nav class="drawer-nav">
        <a href="#hero" class="drawer-link">Home</a>
        <a href="#services" class="drawer-link">Our Services</a>
        <a href="#mirrors" class="drawer-link">LED Mirrors</a>
        <a href="#shower-partitions" class="drawer-link">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="drawer-link">Glass Railings</a>
        <a href="#doors-windows" class="drawer-link">Doors &amp; Windows</a>
        <a href="#collection-preview" class="drawer-link">Craftsmanship</a>
        <a href="#contact" class="drawer-link">Contact &amp; Location</a>
        <a href="#customModal" class="drawer-link open-modal-trigger">Request Custom Quote</a>
      </nav>"""

new_drawer = """      <nav class="drawer-nav">
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
      </nav>"""

assert old_drawer in html, "old_drawer NOT FOUND in html"
html = html.replace(old_drawer, new_drawer, 1)
print("Updated mobile drawer nav")

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nindex.html saved successfully!")
