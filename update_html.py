with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update header navigation
header_nav_target = """      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">Mirror Collection</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>"""

header_nav_replacement = """      <nav class="nav-links" aria-label="Main Navigation">
        <a href="#hero" class="nav-item is-active">Home</a>
        <a href="#services" class="nav-item">Our Services</a>
        <a href="#mirrors" class="nav-item">LED Mirrors</a>
        <a href="#shower-partitions" class="nav-item">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="nav-item">Glass Railings</a>
        <a href="#collection-preview" class="nav-item">Craftsmanship</a>
        <a href="#contact" class="nav-item">Contact &amp; Location</a>
      </nav>"""

assert header_nav_target in content, "header_nav_target not found"
content = content.replace(header_nav_target, header_nav_replacement, 1)

# 2. Update mobile drawer navigation
drawer_nav_target = """      <nav class="drawer-nav">
        <a href="#hero" class="drawer-link">Home</a>
        <a href="#services" class="drawer-link">Our Services</a>
        <a href="#mirrors" class="drawer-link">Mirror Collection</a>
        <a href="#collection-preview" class="drawer-link">Craftsmanship</a>
        <a href="#contact" class="drawer-link">Contact &amp; Location</a>
        <a href="#customModal" class="drawer-link open-modal-trigger">Request Custom Quote</a>
      </nav>"""

drawer_nav_replacement = """      <nav class="drawer-nav">
        <a href="#hero" class="drawer-link">Home</a>
        <a href="#services" class="drawer-link">Our Services</a>
        <a href="#mirrors" class="drawer-link">LED Mirrors</a>
        <a href="#shower-partitions" class="drawer-link">Shower &amp; Partitions</a>
        <a href="#railings-staircases" class="drawer-link">Glass Railings</a>
        <a href="#collection-preview" class="drawer-link">Craftsmanship</a>
        <a href="#contact" class="drawer-link">Contact &amp; Location</a>
        <a href="#customModal" class="drawer-link open-modal-trigger">Request Custom Quote</a>
      </nav>"""

assert drawer_nav_target in content, "drawer_nav_target not found"
content = content.replace(drawer_nav_target, drawer_nav_replacement, 1)

# 3. Add Mirror 28, 29, 30, 31 right after Mirror 27
extra_mirrors = """
          <!-- Mirror 28 -->
          <article class="mirror-product-card">
            <div class="mirror-product-media">
              <img src="assets/images/mirror-calligraphy.jpg" alt="NOVO GLASS - Calligraphy LED Mirror" loading="lazy">
            </div>
            <div class="mirror-product-details">
              <span class="mirror-product-tag">LED MIRROR</span>
              <h3 class="mirror-product-title">Mirror 28</h3>
              <div class="mirror-product-footer">
                <span class="card-price">Bespoke Order</span>
                <button class="mirror-inquire-btn open-modal-trigger" data-piece="Mirror 28 - Calligraphy LED Mirror" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Mirror 29 -->
          <article class="mirror-product-card">
            <div class="mirror-product-media">
              <img src="assets/images/mirror-floral-custom.jpg" alt="NOVO GLASS - Floral Custom LED Mirror" loading="lazy">
            </div>
            <div class="mirror-product-details">
              <span class="mirror-product-tag">LED MIRROR</span>
              <h3 class="mirror-product-title">Mirror 29</h3>
              <div class="mirror-product-footer">
                <span class="card-price">Bespoke Order</span>
                <button class="mirror-inquire-btn open-modal-trigger" data-piece="Mirror 29 - Floral Custom LED Mirror" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Mirror 30 -->
          <article class="mirror-product-card">
            <div class="mirror-product-media">
              <img src="assets/images/mirror-geometric-pattern.jpg" alt="NOVO GLASS - Geometric Architectural Mirror" loading="lazy">
            </div>
            <div class="mirror-product-details">
              <span class="mirror-product-tag">LED MIRROR</span>
              <h3 class="mirror-product-title">Mirror 30</h3>
              <div class="mirror-product-footer">
                <span class="card-price">Bespoke Order</span>
                <button class="mirror-inquire-btn open-modal-trigger" data-piece="Mirror 30 - Geometric Architectural Mirror" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Mirror 31 -->
          <article class="mirror-product-card">
            <div class="mirror-product-media">
              <img src="assets/images/mirror-round-halo.jpg" alt="NOVO GLASS - Round Halo Ambient Mirror" loading="lazy">
            </div>
            <div class="mirror-product-details">
              <span class="mirror-product-tag">LED MIRROR</span>
              <h3 class="mirror-product-title">Mirror 31</h3>
              <div class="mirror-product-footer">
                <span class="card-price">Bespoke Order</span>
                <button class="mirror-inquire-btn open-modal-trigger" data-piece="Mirror 31 - Round Halo Ambient Mirror" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

m27_marker = """<!-- Mirror 27 -->
          <article class="mirror-product-card">
            <div class="mirror-product-media">
              <img src="assets/images/mirror-27.jpg" alt="NOVO GLASS - Mirror 27" loading="eager">
            </div>
            <div class="mirror-product-details">
              <span class="mirror-product-tag">ARCHITECTURAL MIRROR</span>
              <h3 class="mirror-product-title">Mirror 27</h3>
              <div class="mirror-product-footer">
                <span class="card-price">Bespoke Order</span>
                <button class="mirror-inquire-btn open-modal-trigger" data-piece="Mirror 27" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

assert m27_marker in content, "Mirror 27 marker not found in content"
content = content.replace(m27_marker, m27_marker + "\n" + extra_mirrors, 1)

# 4. Insert Section 3 (Bathroom Shower Glass & Partitions) and Section 4 (Staircase Glass & Railings)
idx_mirrors = content.find('id="mirrors"')
idx_sec_end = content.find('</section>', idx_mirrors)
idx_after_sec = idx_sec_end + len('</section>')

new_sections = """

    <!-- ========================================================================
         SECTION 3: BATHROOM SHOWER GLASS & PARTITIONS
         ======================================================================== -->
    <section class="section-gallery section-shower-partitions" id="shower-partitions" aria-label="Bathroom Shower Glass & Partitions">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">ARCHITECTURAL GLASS SOLUTIONS</span>
          <h2 class="gallery-title">BATHROOM SHOWER GLASS &amp; PARTITIONS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Bespoke frameless shower enclosures, minimalist glass cabins, and commercial acoustic partitions. Engineered with high-strength tempered safety glass and precision black &amp; champagne fittings.
          </p>
        </div>

        <div class="gallery-products-grid">
          
          <!-- Shower 01 -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/shower-01-matte-black.jpg" alt="NOVO GLASS - Matte Black Framed Shower Cabin" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">SHOWER ENCLOSURE</span>
                <span class="gallery-spec-badge">Tempered Safety Glass</span>
              </div>
              <h3 class="gallery-product-title">Matte Black Framed Shower Cabin</h3>
              <p class="gallery-product-desc">
                Architectural matte black aluminum framing with tempered clear safety glass, magnetic water seals, and ergonomic designer handle.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Sizing</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Matte Black Framed Shower Cabin" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Shower 02 -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/shower-02-luxury-frameless.jpg" alt="NOVO GLASS - Luxury Frameless Walk-In Double Shower Suite" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">WALK-IN SHOWER</span>
                <span class="gallery-spec-badge">Ultra-Clear Low-Iron</span>
              </div>
              <h3 class="gallery-product-title">Frameless Double Walk-In Shower Suite</h3>
              <p class="gallery-product-desc">
                Full-height frameless glass enclosure for master bathrooms and luxury suites, featuring dual pivot doors and minimal hardware footprint.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Sizing</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Frameless Double Walk-In Shower Suite" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Partition 01 -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/partition-01-aluminum-office.jpg" alt="NOVO GLASS - Architectural Aluminum Office Partition" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">OFFICE PARTITION</span>
                <span class="gallery-spec-badge">Frosted Acoustic Glass</span>
              </div>
              <h3 class="gallery-product-title">Aluminum Grid Office Glass Partition</h3>
              <p class="gallery-product-desc">
                Modular aluminum glass partition system with frosted manifestation bands for privacy, meeting rooms, and modern corporate interiors.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Sizing</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Aluminum Grid Office Glass Partition" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Partition 02 -->
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
          </article>

        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 4: STAIRCASE GLASS & RAILINGS
         ======================================================================== -->
    <section class="section-gallery section-railings-staircases" id="railings-staircases" aria-label="Staircase Glass & Railings">
      <div class="gallery-container">
        
        <div class="gallery-heading-block">
          <span class="gold-eyebrow">STRUCTURAL BALUSTRADES &amp; FACADES</span>
          <h2 class="gallery-title">STAIRCASE GLASS &amp; RAILINGS</h2>
          <div class="gallery-gold-divider"></div>
          <p class="gallery-lead">
            Engineered structural glass balustrades, staircase glass barriers, and cantilever terrace railings. Designed to deliver uncompromised safety, pristine transparency, and architectural distinction.
          </p>
        </div>

        <div class="gallery-products-grid gallery-products-grid-3">
          
          <!-- Railing 01 -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/railing-01-architectural-balcony.jpg" alt="NOVO GLASS - Cantilever Balcony Glass Railing with LED Illumination" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">BALCONY BALUSTRADE</span>
                <span class="gallery-spec-badge">Integrated LED Profile</span>
              </div>
              <h3 class="gallery-product-title">Cantilever Balcony Glass Railing with LED</h3>
              <p class="gallery-product-desc">
                Multi-tier exterior cantilever balustrade with laminated toughened safety glass and built-in architectural LED perimeter illumination for modern luxury villas.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Cantilever Balcony Glass Railing with LED" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Railing 02 -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/novo-glass-balcony.jpg" alt="NOVO GLASS - Panoramic Frameless Terrace Glass Balustrade System" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">TERRACE BALUSTRADE</span>
                <span class="gallery-spec-badge">Heavy Laminated Safety Glass</span>
              </div>
              <h3 class="gallery-product-title">Panoramic Frameless Terrace Balustrade</h3>
              <p class="gallery-product-desc">
                Unobstructed terrace glass railing utilizing heavy-duty recessed base channels and marine-grade stainless hardware for pristine panoramic views.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Panoramic Frameless Terrace Balustrade" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Railing 03 -->
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
          </article>

        </div>
      </div>
    </section>"""

content = content[:idx_after_sec] + new_sections + content[idx_after_sec:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")
