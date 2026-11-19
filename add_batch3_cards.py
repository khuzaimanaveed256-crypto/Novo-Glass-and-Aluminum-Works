with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Shower 03 card after the Barn-Style Sliding Frosted Glass Door card in #shower-partitions
partition_03_end = """          <!-- Partition 03 (Sliding Barn Glass Door) -->
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

shower_04_card = """
          <!-- Shower 03 (Tinted Sliding Glass Shower Cabin) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/shower-03-tinted-sliding-cabin.jpg" alt="NOVO GLASS - Tinted Sliding Glass Shower Cabin" loading="lazy">
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
                <span class="gallery-spec-badge">Tinted Safety Glass</span>
              </div>
              <h3 class="gallery-product-title">Tinted Sliding Glass Shower Cabin</h3>
              <p class="gallery-product-desc">
                Fully enclosed tinted tempered glass shower cabin with heavy-duty stainless steel sliding door hardware, pin clips, and seamless low-profile tray.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Sizing</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Tinted Sliding Glass Shower Cabin" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

assert partition_03_end in html, "partition_03_end marker NOT FOUND"
html = html.replace(partition_03_end, partition_03_end + shower_04_card, 1)
print("Added Shower 03 card to #shower-partitions")

# 2. Add 3 new Staircase cards after Railing 04 (Spigot-Mounted Villa Balcony) card
railing_04_end = """          <!-- Railing 04 (Spigot-Mounted Exterior Balcony) -->
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

new_staircase_cards = """
          <!-- Staircase 03 (Smoked Glass Pin-Mounted with Under-Stair Storage) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/staircase-03-smoked-pinmount.jpg" alt="NOVO GLASS - Smoked Glass Staircase Railing with Under-Stair Storage" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">INTERIOR STAIRCASE</span>
                <span class="gallery-spec-badge">Smoked Tempered Glass</span>
              </div>
              <h3 class="gallery-product-title">Smoked Glass Staircase with Pin Mounts</h3>
              <p class="gallery-product-desc">
                Full-height smoked architectural glass panels secured with polished stainless steel pin-mount standoffs along a floating staircase with integrated under-stair storage.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Smoked Glass Staircase with Pin Mounts" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Staircase 04 (Marble Staircase with Black Post Balustrade) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/staircase-04-marble-black-post.jpg" alt="NOVO GLASS - Marble Staircase with Black Post Glass Balustrade" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">MARBLE STAIRCASE</span>
                <span class="gallery-spec-badge">Black Post &amp; Clamp</span>
              </div>
              <h3 class="gallery-product-title">Marble Staircase Black Post Glass Balustrade</h3>
              <p class="gallery-product-desc">
                Luxury marble staircase with architectural clear glass panels mounted on matte black vertical posts, creating an elegant and open-riser ambiance.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Marble Staircase Black Post Glass Balustrade" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Staircase 05 (Clear Glass Black Handrail System) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/staircase-05-black-rail-clear.jpg" alt="NOVO GLASS - Clear Glass Staircase with Black Aluminum Handrail" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">RESIDENTIAL STAIRCASE</span>
                <span class="gallery-spec-badge">Clear Glass + Black Rail</span>
              </div>
              <h3 class="gallery-product-title">Clear Glass Staircase &amp; Black Aluminum Rail</h3>
              <p class="gallery-product-desc">
                Structural clear safety glass balustrade with matte black extruded aluminum handrail profile and bottom-fixed base clamps for interior residential staircases.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Clear Glass Staircase & Black Aluminum Rail" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

assert railing_04_end in html, "railing_04_end marker NOT FOUND"
html = html.replace(railing_04_end, railing_04_end + new_staircase_cards, 1)
print("Added Staircase 03, 04, 05 cards to #railings-staircases")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html saved successfully!")
