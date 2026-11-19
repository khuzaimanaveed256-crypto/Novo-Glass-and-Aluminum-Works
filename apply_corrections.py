import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# STEP 1: Extract the Barn-Style Sliding Door card from #bathroom-showers
# =========================================================================
idx_bs = html.find('id="bathroom-showers"')
idx_bs_end = html.find('</section>', idx_bs)
bs_section = html[idx_bs:idx_bs_end]

# Find the 4th card (Barn-Style Sliding Frosted Glass Door)
barn_pattern = re.compile(
    r'(<!--[^\n]*?-->\s*)?<article class="gallery-product-card">.*?Barn-Style Sliding Frosted Glass Door.*?</article>',
    re.DOTALL
)
barn_match = barn_pattern.search(bs_section)
assert barn_match is not None, "Could not find Barn-Style Sliding Frosted Glass Door in #bathroom-showers"

barn_card_html = barn_match.group(0).strip()
print("Found Barn Door card:")
print(barn_card_html[:150] + "...")

# Remove this card from bs_section
bs_section_cleaned = bs_section[:barn_match.start()].rstrip() + "\n\n" + bs_section[barn_match.end():].lstrip()

# Update the lead paragraph in #bathroom-showers to reflect shower enclosures & cabins
bs_section_cleaned = bs_section_cleaned.replace(
    'Bespoke frameless shower enclosures, tinted glass cabins, walk-in suites, and sliding bathroom doors. Handcrafted with heavy tempered architectural safety glass and precision hardware fittings.',
    'Bespoke frameless shower enclosures, tinted glass shower cabins, and luxury walk-in suites. Handcrafted with heavy tempered architectural safety glass, precision hardware fittings, and waterproof base profiles.'
)

# Replace in html
html = html[:idx_bs] + bs_section_cleaned + html[idx_bs_end:]
print("Removed Barn Door card from #bathroom-showers and updated lead text")

# =========================================================================
# STEP 2: Add Barn-Style Sliding Door card to #doors-windows (Sliding Doors)
# =========================================================================
idx_dw = html.find('id="doors-windows"')
idx_dw_end = html.find('</section>', idx_dw)
dw_section = html[idx_dw:idx_dw_end]

# Update the heading and lead of #doors-windows to feature Sliding Doors clearly
dw_section_updated = dw_section.replace(
    '<span class="gold-eyebrow">ARCHITECTURAL ALUMINUM SYSTEMS</span>\n          <h2 class="gallery-title">ALUMINUM DOORS &amp; WINDOWS</h2>',
    '<span class="gold-eyebrow">ARCHITECTURAL SLIDING &amp; ENTRANCE SYSTEMS</span>\n          <h2 class="gallery-title">SLIDING DOORS &amp; ALUMINUM SYSTEMS</h2>'
)
dw_section_updated = dw_section_updated.replace(
    '<span class="gold-eyebrow">ARCHITECTURAL ALUMINUM SYSTEMS</span>\r\n          <h2 class="gallery-title">ALUMINUM DOORS &amp; WINDOWS</h2>',
    '<span class="gold-eyebrow">ARCHITECTURAL SLIDING &amp; ENTRANCE SYSTEMS</span>\r\n          <h2 class="gallery-title">SLIDING DOORS &amp; ALUMINUM SYSTEMS</h2>'
)

dw_section_updated = dw_section_updated.replace(
    'Precision-engineered architectural aluminum doors, panoramic sliding systems, and high-performance insulated window frames. Crafted for seamless indoor-outdoor transitions and luxury modern living.',
    'Precision-engineered architectural sliding glass doors, barn-style interior sliding doors, bi-fold patio systems, and high-performance insulated window frames. Crafted for seamless indoor-outdoor transitions and luxury modern living.'
)

# Insert the Barn Door card right after the Bi-Fold Doors card (or as card 2)
bifold_end_marker = '</article>'
# Find first </article> in dw_section
first_art_end = dw_section_updated.find('</article>') + len('</article>')

card_to_insert = "\n\n          " + barn_card_html

dw_section_updated = dw_section_updated[:first_art_end] + card_to_insert + dw_section_updated[first_art_end:]

# Replace in html
html = html[:idx_dw] + dw_section_updated + html[idx_dw_end:]
print("Added Barn Door card into #doors-windows (Sliding Doors)")

# =========================================================================
# STEP 3: Update navigation to reflect Sliding Doors & Windows
# =========================================================================
html = html.replace(
    '<a href="#doors-windows" class="nav-item">Doors &amp; Windows</a>',
    '<a href="#doors-windows" class="nav-item">Sliding Doors &amp; Windows</a>'
)
html = html.replace(
    '<a href="#doors-windows" class="drawer-link">Doors &amp; Windows</a>',
    '<a href="#doors-windows" class="drawer-link">Sliding Doors &amp; Windows</a>'
)

# Save index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved index.html successfully!")
