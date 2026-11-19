import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Staircase 06 to #staircase-glass
stair_card_06 = """
          <!-- Staircase 06 (Minimalist Floating Staircase Glass Balustrade) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/staircase-06-floating-white-spigot.jpg" alt="NOVO GLASS - Minimalist Floating Staircase Glass Balustrade" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">FLOATING STAIRCASE</span>
                <span class="gallery-spec-badge">Tempered Glass + Spigots</span>
              </div>
              <h3 class="gallery-product-title">Minimalist Floating Staircase Glass Balustrade</h3>
              <p class="gallery-product-desc">
                Modern architectural open-riser staircase with cantilevered clear safety glass panels secured with polished stainless steel base spigots.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Engineering</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Minimalist Floating Staircase Glass Balustrade" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

# Find the end of the last article in #staircase-glass
idx_sg = html.find('id="staircase-glass"')
idx_sg_end = html.find('</section>', idx_sg)
last_art_end_sg = html.rfind('</article>', idx_sg, idx_sg_end) + len('</article>')

html = html[:last_art_end_sg] + stair_card_06 + html[last_art_end_sg:]
print("Added Staircase 06 card to #staircase-glass")

# 2. Add Partitions 03 and 04 to #shower-partitions
partition_card_03 = """
          <!-- Partition 03 (Frameless Commercial Corridor Glass Partition) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/partition-04-office-frosted-band.jpg" alt="NOVO GLASS - Frameless Commercial Corridor Glass Partition" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">CORRIDOR PARTITION</span>
                <span class="gallery-spec-badge">Frameless Acoustic Glass</span>
              </div>
              <h3 class="gallery-product-title">Frameless Commercial Corridor Glass Partition</h3>
              <p class="gallery-product-desc">
                Floor-to-ceiling acoustic glass wall partition system with frosted manifestation privacy bands and heavy-duty pivot entrance doors.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Sizing</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Frameless Commercial Corridor Glass Partition" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Partition 04 (Slimline Black Frame Privacy Glass Partition) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/partition-05-black-frame-privacy.jpg" alt="NOVO GLASS - Slimline Black Frame Privacy Glass Partition" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">EXECUTIVE PARTITION</span>
                <span class="gallery-spec-badge">Slim Black Frame + Satin</span>
              </div>
              <h3 class="gallery-product-title">Slimline Black Frame Privacy Glass Partition</h3>
              <p class="gallery-product-desc">
                Contemporary slimline matte black aluminum partition framework featuring wide satin privacy glass and matching acoustic hinged door.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Sizing</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Slimline Black Frame Privacy Glass Partition" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

idx_sp = html.find('id="shower-partitions"')
idx_sp_end = html.find('</section>', idx_sp)
last_art_end_sp = html.rfind('</article>', idx_sp, idx_sp_end) + len('</article>')

html = html[:last_art_end_sp] + partition_card_03 + html[last_art_end_sp:]
print("Added Partition 03 & 04 cards to #shower-partitions")

# 3. Add Windows 02 and 03 to #doors-windows
window_cards_02_03 = """
          <!-- Window 02 (Architectural Aluminum Sliding Window System) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/window-02-aluminum-sliding-track.jpg" alt="NOVO GLASS - Architectural Aluminum Sliding Window System" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">SLIDING WINDOW SYSTEM</span>
                <span class="gallery-spec-badge">Heavy-Duty Track</span>
              </div>
              <h3 class="gallery-product-title">Architectural Aluminum Sliding Window System</h3>
              <p class="gallery-product-desc">
                Multi-track smooth-gliding aluminum window framework with solar reflective glass and integrated exterior safety bars.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Fabrication</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Architectural Aluminum Sliding Window System" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>

          <!-- Window 03 (Bronze Anodized Casement Glass Window System) -->
          <article class="gallery-product-card">
            <div class="gallery-product-media">
              <img src="assets/images/window-03-bronze-casement-open.jpg" alt="NOVO GLASS - Bronze Anodized Casement Glass Window System" loading="lazy">
              <span class="gallery-zoom-badge">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </span>
            </div>
            <div class="gallery-product-details">
              <div class="gallery-meta-row">
                <span class="gallery-product-tag">CASEMENT WINDOW</span>
                <span class="gallery-spec-badge">Bronze Anodized Frame</span>
              </div>
              <h3 class="gallery-product-title">Bronze Anodized Casement Glass Window System</h3>
              <p class="gallery-product-desc">
                Dual-swing out-opening bronze aluminum casement window with fixed upper transom panel and architectural exterior trim.
              </p>
              <div class="gallery-product-footer">
                <div class="gallery-price-block">
                  <span class="gallery-price-label">Custom Fabrication</span>
                  <span class="gallery-price-value">Bespoke Order</span>
                </div>
                <button class="gallery-inquire-btn open-modal-trigger" data-piece="Bronze Anodized Casement Glass Window System" type="button">
                  <span>Inquire</span>
                  <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8">
                    <path d="M5 12h14M13 6l6 6-6 6"/>
                  </svg>
                </button>
              </div>
            </div>
          </article>"""

idx_dw = html.find('id="doors-windows"')
idx_dw_end = html.find('</section>', idx_dw)
last_art_end_dw = html.rfind('</article>', idx_dw, idx_dw_end) + len('</article>')

html = html[:last_art_end_dw] + window_cards_02_03 + html[last_art_end_dw:]
print("Added Window 02 & 03 cards to #doors-windows")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html saved successfully with all 5 new products!")
