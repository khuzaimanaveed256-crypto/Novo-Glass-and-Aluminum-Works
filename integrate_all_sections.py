import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update navigation links in header & drawer to include Doors & Windows
nav_header_old = """      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#shower-partitions" class="nav-item">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="nav-item">Glass Railings</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>"""

nav_header_new = """      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#shower-partitions" class="nav-item">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="nav-item">Glass Railings</a>
        <a href="#doors-windows" class="nav-item">Doors &amp; Windows</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>"""

assert nav_header_old in html, "nav_header_old not found"
html = html.replace(nav_header_old, nav_header_new, 1)

nav_drawer_old = """      <nav class="drawer-nav">
        <a href="#hero" class="drawer-link">Home</a>
        <a href="#services" class="drawer-link">Our Services</a>
        <a href="#mirrors" class="drawer-link">LED Mirrors</a>
        <a href="#shower-partitions" class="drawer-link">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="drawer-link">Glass Railings</a>
        <a href="#collection-preview" class="drawer-link">Craftsmanship</a>
        <a href="#contact" class="drawer-link">Contact &amp; Location</a>
        <a href="#customModal" class="drawer-link open-modal-trigger">Request Custom Quote</a>
      </nav>"""

nav_drawer_new = """      <nav class="drawer-nav">
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

assert nav_drawer_old in html, "nav_drawer_old not found"
html = html.replace(nav_drawer_old, nav_drawer_new, 1)

# 2. Add card 5 to #shower-partitions right after Partition 02
partition_02_marker = """          <!-- Partition 02 -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/partition-02-acoustic-commercial.jpg" alt="NOVO GLASS - Commercial Acoustic Glass Wall & Door System" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">COMMERCIAL PARTITION</span>
                <span class="gallery-spec-badge">Sound-Damping Acoustic</span>
              </div>
              <h3 class="gallery-product-title">Commercial Acoustic Glass Wall &amp; Door</h3>
              <p class="gallery-product-desc">
                Sound-dampening architectural tinted glass partition wall with heavy-duty black framed glass doors, providing superior noise isolation and sleek aesthetics.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Sizing</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Commercial Acoustic Glass Wall & Door" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

partition_03_card = """          <!-- Partition 03 (Sliding Barn Glass Door) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/partition-03-sliding-frosted.jpg" alt="NOVO GLASS - Barn-Style Sliding Frosted Glass Door" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">SLIDING GLASS DOOR</span>
                <span class="gallery-spec-badge">Frosted Safety Glass</span>
              </div>
              <h3 class="gallery-product-title">Barn-Style Sliding Frosted Glass Door</h3>
              <p class="gallery-product-desc">
                Modern top-hung stainless steel roller track with frosted privacy tempered glass pane and brushed ergonomic pull handle for luxury bathrooms and suites.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Sizing</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Barn-Style Sliding Frosted Glass Door" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

assert partition_02_marker in html, "partition_02_marker not found"
html = html.replace(partition_02_marker, partition_02_marker + "\n\n" + partition_03_card, 1)

# 3. Add card 6 to #railings-staircases right after Railing 03
railing_03_marker = """          <!-- Railing 03 (Post & Clamp System) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/novo-railing-balcony.jpg" alt="NOVO GLASS - Modern Minimalist Structural Glass Railing" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">STAIRCASE &amp; BALCONY</span>
                <span class="gallery-spec-badge">Stainless Steel 316</span>
              </div>
              <h3 class="gallery-product-title">Modern Minimalist Structural Glass Railing</h3>
              <p class="gallery-product-desc">
                Architectural post-and-clamp glass balustrade system engineered for staircase runs and landing areas with brushed stainless steel cap handrails.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Modern Minimalist Structural Glass Railing" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

railing_04_card = """          <!-- Railing 04 (Spigot-Mounted Exterior Balcony) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/railing-02-spigot-balcony.jpg" alt="NOVO GLASS - Spigot-Mounted Villa Balcony Glass Balustrade" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">EXTERIOR BALUSTRADE</span>
                <span class="gallery-spec-badge">Duplex 2205 Spigots</span>
              </div>
              <h3 class="gallery-product-title">Spigot-Mounted Villa Balcony Balustrade</h3>
              <p class="gallery-product-desc">
                Frameless architectural glass balcony railing engineered with marine-grade stainless steel base spigots for multi-tier contemporary residences.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Spigot-Mounted Villa Balcony Balustrade" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

assert railing_03_marker in html, "railing_03_marker not found"
html = html.replace(railing_03_marker, railing_03_marker + "\n\n" + railing_04_card, 1)

# 4. Insert Section 5: ALUMINUM DOORS & WINDOWS right after Section 4: STAIRCASE GLASS & RAILINGS
idx_railings = html.find('id="railings-staircases"')
idx_railings_end = html.find('</section>', idx_railings) + len('</section>')

doors_windows_section = """

    <!-- ========================================================================
         SECTION 5: ALUMINUM DOORS & WINDOWS
         ======================================================================== -->
    <section class="section-gallery section-doors-windows" id="doors-windows" aria-label="Aluminum Doors & Windows">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">ARCHITECTURAL ALUMINUM SYSTEMS</span>
          <h2 class="gallery-title">ALUMINUM DOORS &amp; WINDOWS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Precision-engineered architectural aluminum doors, panoramic sliding systems, and high-performance insulated window frames. Crafted for seamless indoor-outdoor transitions and luxury modern living.
          </p>
        </div>

        <div class="gallery-products-grid gallery-products-grid-3">
          
          <!-- Door 01 (Bi-Fold Folding Doors) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/door-01-aluminum-bifold.jpg" alt="NOVO GLASS - Luxury Aluminum Bi-Fold Glass Doors" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">BI-FOLD DOOR SYSTEM</span>
                <span class="gallery-spec-badge">Concertina Multi-Leaf</span>
              </div>
              <h3 class="gallery-product-title">Luxury Aluminum Bi-Fold Glass Doors</h3>
              <p class="gallery-product-desc">
                Smooth-gliding concertina multi-panel folding doors with slim aluminum profiles and thermal break insulation for panoramic openings.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Fabrication</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Luxury Aluminum Bi-Fold Glass Doors" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Door 02 (Slimline Black French Door) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/door-02-slimline-black.jpg" alt="NOVO GLASS - Slimline Black Aluminum Glass French Door" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">INTERIOR &amp; PATIO DOOR</span>
                <span class="gallery-spec-badge">Slim Matte Black</span>
              </div>
              <h3 class="gallery-product-title">Slimline Black Aluminum Glass French Door</h3>
              <p class="gallery-product-desc">
                Minimalist matte black aluminum frame with full-height tempered clear glass, architectural lockset, and high thermal performance.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Fabrication</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Slimline Black Aluminum Glass French Door" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Door 03 (Triple Sliding Patio Doors) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/door-03-triple-sliding.jpg" alt="NOVO GLASS - Triple-Track Aluminum Sliding Patio Doors" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">SLIDING PATIO SYSTEM</span>
                <span class="gallery-spec-badge">Triple Track Rolling</span>
              </div>
              <h3 class="gallery-product-title">Triple-Track Aluminum Sliding Patio Doors</h3>
              <p class="gallery-product-desc">
                Floor-to-ceiling heavy-duty sliding glass doors with ultra-smooth concealed rollers for seamless kitchen, garden, and patio integration.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Fabrication</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Triple-Track Aluminum Sliding Patio Doors" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Door 04 (Frosted Sliding Terrace Doors) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/door-04-patio-slider.jpg" alt="NOVO GLASS - Architectural Sliding Glass Terrace Doors" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">TERRACE SLIDING DOOR</span>
                <span class="gallery-spec-badge">Satin Privacy Glass</span>
              </div>
              <h3 class="gallery-product-title">Architectural Sliding Glass Terrace Doors</h3>
              <p class="gallery-product-desc">
                Wide-span aluminum sliding system with translucent frosted safety glass providing privacy and diffuse natural ambient illumination.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Fabrication</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Architectural Sliding Glass Terrace Doors" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Window 01 (Bronze Reflective Aluminum Window) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/window-01-bronze-aluminum.jpg" alt="NOVO GLASS - Champagne Bronze Aluminum Window System" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">ARCHITECTURAL WINDOW</span>
                <span class="gallery-spec-badge">Bronze Reflective Glass</span>
              </div>
              <h3 class="gallery-product-title">Champagne Bronze Aluminum Window System</h3>
              <p class="gallery-product-desc">
                Heavy aluminum architectural window framework with bronze solar-reflective safety glass, precision casement vents, and decorative exterior molding.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Fabrication</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Champagne Bronze Aluminum Window System" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

        </div>
      </div>
    </section>"""

html = html[:idx_railings_end] + doors_windows_section + html[idx_railings_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with all galleries successfully!")
