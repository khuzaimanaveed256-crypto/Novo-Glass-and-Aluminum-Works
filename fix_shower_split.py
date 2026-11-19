import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ==============================================================
# The issue: #bathroom-showers section exists but is EMPTY,
# and #shower-partitions still has ALL 6 products.
# 
# Fix: Directly extract articles from shower-partitions,
#       split them, place shower ones in bathroom-showers,
#       keep only partition ones in shower-partitions.
# ==============================================================

SHOWER_TITLES = {
    'Matte Black Framed Shower Cabin',
    'Frameless Double Walk-In Shower Suite',
    'Barn-Style Sliding Frosted Glass Door',
    'Tinted Sliding Glass Shower Cabin'
}

# 1. Find all article blocks in the entire file (with their preceding comments)
# Pattern: optional comment + <article>...</article>
all_articles = list(re.finditer(
    r'((?:[ \t]*<!--[^>]*?-->\s*)?<article class="gallery-product-card">.*?</article>)',
    html,
    re.DOTALL
))

print(f"Total articles found: {len(all_articles)}")
for m in all_articles:
    t = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', m.group(1))
    print(f"  [{m.start()}-{m.end()}] {t.group(1) if t else '???'}")

# 2. Find the #shower-partitions section and get its article blocks
idx_sp = html.find('id="shower-partitions"')
idx_sp_end = html.find('</section>', idx_sp) + len('</section>')

# 3. Find the #bathroom-showers section bounds
idx_bs = html.find('id="bathroom-showers"')
idx_bs_end = html.find('</section>', idx_bs) + len('</section>')

# 4. Find the gallery-products-grid div inside #shower-partitions
sp_section = html[idx_sp:idx_sp_end]

# Find all articles in the shower-partitions section
sp_articles = list(re.finditer(
    r'((?:[ \t]*<!--[^>]*?-->\s*)?<article class="gallery-product-card">.*?</article>)',
    sp_section,
    re.DOTALL
))

shower_card_htmls = []
partition_card_htmls = []

for m in sp_articles:
    block = m.group(1)
    t = re.search(r'<h3 class="gallery-product-title">([^<]+)</h3>', block)
    title = t.group(1) if t else ''
    if title in SHOWER_TITLES:
        shower_card_htmls.append(block.strip())
        print(f"SHOWER -> {title}")
    else:
        partition_card_htmls.append(block.strip())
        print(f"PARTITION -> {title}")

# 5. Build new #shower-partitions content (only partition cards)
partition_grid = '\n\n          '.join(partition_card_htmls)

new_sp_section = f"""<section class="section-gallery section-shower-partitions" id="shower-partitions" aria-label="Glass Partitions">
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
          
          {partition_grid}

        </div>
      </div>
    </section>"""

# 6. Build new #bathroom-showers content (only shower cards)
shower_grid = '\n\n          '.join(shower_card_htmls)

new_bs_section = f"""<!-- ========================================================================
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
          
          {shower_grid}

        </div>
      </div>
    </section>"""

# 7. Apply replacements — replace BOTH sections in the HTML
# Need to find the actual section tags (not just id= attribute)
def find_full_section(html, section_id):
    """Return (start_of_section_tag, end_of_closing_tag) in html"""
    # Find the opening section tag that contains this id
    pattern = r'<section[^>]*id="' + re.escape(section_id) + r'"[^>]*>'
    m = re.search(pattern, html)
    if not m:
        raise ValueError(f"Section #{section_id} not found")
    sec_open_start = m.start()
    # Walk back to find any comment before it
    # find from last newline
    scan = html.rfind('\n<!-- ', 0, sec_open_start)
    if scan != -1 and scan > sec_open_start - 300:
        sec_open_start = scan + 1  # keep the newline before comment
    # find </section>
    sec_close = html.find('</section>', m.end()) + len('</section>')
    return sec_open_start, sec_close

# Replace shower-partitions section
sp_start, sp_end = find_full_section(html, 'shower-partitions')
print(f"\nshower-partitions: [{sp_start}:{sp_end}]")

# Replace bathroom-showers section
bs_start, bs_end = find_full_section(html, 'bathroom-showers')
print(f"bathroom-showers: [{bs_start}:{bs_end}]")

# Since bathroom-showers comes before shower-partitions in the DOM,
# we need to replace from last to first to preserve positions

# First confirm order
assert bs_start < sp_start, "Expected bathroom-showers before shower-partitions"

# Replace shower-partitions (later in file) first
html = html[:sp_start] + '    ' + new_sp_section + html[sp_end:]
print("Replaced shower-partitions section")

# Recalculate bs position after the above replacement
bs_start, bs_end = find_full_section(html, 'bathroom-showers')

# Replace bathroom-showers
html = html[:bs_start] + '    ' + new_bs_section + '\n\n    ' + html[bs_end:]
print("Replaced bathroom-showers section")

# 8. Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nSaved index.html!")

# Quick verify
idx_bs2 = html.find('id="bathroom-showers"')
idx_bs2_end = html.find('</section>', idx_bs2)
bs_section2 = html[idx_bs2:idx_bs2_end]
bs_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', bs_section2)
print(f"\n=== BATHROOM SHOWERS section now has {len(bs_titles)} products ===")
for t in bs_titles:
    print(f"  - {t}")

idx_sp2 = html.find('id="shower-partitions"')
idx_sp2_end = html.find('</section>', idx_sp2)
sp_section2 = html[idx_sp2:idx_sp2_end]
sp_titles = re.findall(r'<h3 class="gallery-product-title">([^<]+)</h3>', sp_section2)
print(f"\n=== GLASS PARTITIONS section now has {len(sp_titles)} products ===")
for t in sp_titles:
    print(f"  - {t}")
