css_enhancements = """
/* ==========================================================================
   GLOBAL COMPLETE PRODUCT IMAGE DISPLAY — ZERO CROPPING (object-fit: contain)
   ========================================================================== */

/* 1. LED Mirrors: Every mirror displays complete height, width and halo */
.mirror-product-media {
  position: relative !important;
  aspect-ratio: 4 / 4.6 !important;
  height: 380px !important;
  width: 100% !important;
  background: radial-gradient(circle at center, #1a1a24 0%, #070709 100%) !important;
  overflow: hidden !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 14px 10px !important;
  border-bottom: 1px solid rgba(198, 164, 91, 0.12) !important;
}

.mirror-product-media img {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain !important;
  object-position: center !important;
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  filter: drop-shadow(0 8px 22px rgba(0, 0, 0, 0.75)) !important;
  transition: transform 0.65s var(--ease-cinematic), filter 0.65s ease !important;
}

.mirror-product-card:hover .mirror-product-media img {
  transform: scale(1.03) !important;
  filter: drop-shadow(0 12px 28px rgba(198, 164, 91, 0.25)) brightness(1.05) !important;
}

/* 2. Global Gallery Product Media: contain by default so no product is cropped */
.gallery-product-media {
  position: relative;
  aspect-ratio: 4 / 4.4;
  height: 440px;
  width: 100%;
  overflow: hidden;
  background: radial-gradient(circle at center, #191922 0%, #08080a 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 12px 10px;
  border-bottom: 1px solid rgba(198, 164, 91, 0.15);
}

.gallery-product-media img {
  width: 100%;
  height: 100%;
  object-fit: contain !important;
  object-position: center;
  display: block;
  filter: drop-shadow(0 10px 24px rgba(0, 0, 0, 0.75));
  transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1), filter 0.65s ease;
}

.gallery-product-card:hover .gallery-product-media img {
  transform: scale(1.025);
  filter: drop-shadow(0 15px 32px rgba(198, 164, 91, 0.25)) brightness(1.04);
}

/* 3. Bathroom Showers: Full-height enclosures */
.section-bathroom-showers .gallery-products-grid.shower-cabins-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.2rem;
  width: 100%;
}

.section-bathroom-showers .gallery-product-media {
  aspect-ratio: 3 / 4;
  height: 500px;
  max-height: 520px;
}

/* 4. Glass Partitions: Clean 2-column centered layout */
.section-shower-partitions .gallery-products-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  max-width: 980px;
  margin: 0 auto;
  gap: 2.4rem;
  width: 100%;
}

.section-shower-partitions .gallery-product-media {
  aspect-ratio: 4 / 3.4;
  height: 380px;
}

/* 5. Staircase Glass: Tall architectural stairs */
.section-staircase-glass {
  background: #0a0a0c;
  background: radial-gradient(circle at 50% 0%, rgba(198, 164, 91, 0.035) 0%, rgba(10, 10, 12, 0.99) 70%);
  border-top: 1px solid rgba(198, 164, 91, 0.12);
}

.section-staircase-glass .gallery-products-grid.staircase-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.2rem;
  width: 100%;
}

.section-staircase-glass .gallery-product-media {
  aspect-ratio: 3 / 4;
  height: 480px;
}

/* 6. Terrace & Balcony Glass: Clean 2-column centered layout */
.section-balcony-glass {
  background: #0c0c0e;
  background: radial-gradient(circle at 50% 0%, rgba(198, 164, 91, 0.04) 0%, rgba(12, 12, 14, 0.98) 70%);
  border-top: 1px solid rgba(198, 164, 91, 0.12);
}

.section-balcony-glass .gallery-products-grid.balcony-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  max-width: 980px;
  margin: 0 auto;
  gap: 2.4rem;
  width: 100%;
}

.section-balcony-glass .gallery-product-media {
  aspect-ratio: 3 / 4;
  height: 480px;
}

/* 7. Sliding Doors & Windows: Balanced 3-column grid */
.section-doors-windows .gallery-products-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.2rem;
  width: 100%;
}

.section-doors-windows .gallery-product-media {
  aspect-ratio: 4 / 4.4;
  height: 450px;
}

/* 8. Craftsmanship / Atelier Signature Mirror */
.card-media {
  position: relative !important;
  aspect-ratio: 16 / 10 !important;
  min-height: 380px !important;
  overflow: hidden !important;
  background: radial-gradient(circle at center, #181822 0%, #08080a 100%) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 14px !important;
}

.card-media img {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain !important;
  object-position: center !important;
  display: block !important;
  filter: drop-shadow(0 10px 24px rgba(0, 0, 0, 0.75)) !important;
  transition: transform 0.65s var(--ease-cinematic) !important;
}

/* Responsive adjustments */
@media (max-width: 1200px) {
  .section-staircase-glass .gallery-products-grid.staircase-grid,
  .section-doors-windows .gallery-products-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.8rem;
  }
  .mirror-product-media {
    height: 340px !important;
  }
}

@media (max-width: 768px) {
  .mirror-product-media {
    height: 320px !important;
  }
  .section-staircase-glass .gallery-products-grid.staircase-grid,
  .section-balcony-glass .gallery-products-grid.balcony-grid,
  .section-shower-partitions .gallery-products-grid,
  .section-doors-windows .gallery-products-grid {
    grid-template-columns: 1fr;
    gap: 1.6rem;
  }
  .gallery-product-media {
    height: 380px;
  }
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace earlier full-height shower section if present or append cleanly
marker = '/* ==========================================================================\n   BATHROOM SHOWERS — FULL HEIGHT PRODUCT IMAGES'
if marker in css:
    idx = css.find(marker)
    css = css[:idx]

css = css.rstrip() + "\n\n" + css_enhancements

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("css/style.css updated with global complete product image display rules!")
