with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx_start = content.find('<!-- ========================================================================\n         SECTION 4: STAIRCASE GLASS & RAILINGS')
if idx_start == -1:
    idx_start = content.find('id="railings-staircases"')
    # find comment preceding it
    idx_start = content.rfind('<!--', 0, idx_start)

idx_end = content.find('</section>', idx_start) + len('</section>')

new_staircase_section = """<!-- ========================================================================
         SECTION 4: STAIRCASE GLASS & RAILINGS
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
          
          <!-- Staircase 01 (Curved Glass Balustrade) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/staircase-01-curved-glass.jpg" alt="NOVO GLASS - Grand Curved Staircase Glass Balustrade" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">CURVED STAIRCASE</span>
                <span class="gallery-spec-badge">Point-Supported Pins</span>
              </div>
              <h3 class="gallery-product-title">Grand Curved Staircase Glass Balustrade</h3>
              <p class="gallery-product-desc">
                Architectural curved tempered glass panels mounted with heavy-duty stainless steel standoff pins and precision-formed continuous ergonomic top rail.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Grand Curved Staircase Glass Balustrade" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Staircase 02 (Cantilever Smoked Glass) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/staircase-02-cantilever-smoke.jpg" alt="NOVO GLASS - Cantilever Staircase Smoked Glass Railing" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">CANTILEVER STAIRCASE</span>
                <span class="gallery-spec-badge">Tinted Safety Glass</span>
              </div>
              <h3 class="gallery-product-title">Cantilever Staircase Smoked Glass Railing</h3>
              <p class="gallery-product-desc">
                Modern floating stone staircase featuring tinted architectural glass balustrades with continuous mezzanine landing protection and minimalist anchors.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Cantilever Staircase Smoked Glass Railing" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Railing 01 (Balcony LED) -->
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

          <!-- Railing 02 (Terrace Balustrade) -->
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

          <!-- Railing 03 (Post & Clamp System) -->
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

content = content[:idx_start] + new_staircase_section + content[idx_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Staircase Glass & Railings section successfully!")
