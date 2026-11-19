shower_css = """
/* ==========================================================================
   BATHROOM SHOWERS — FULL HEIGHT PRODUCT IMAGES (No Cropping)
   ========================================================================== */

.section-bathroom-showers .gallery-products-grid.shower-cabins-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.2rem;
  width: 100%;
}

.section-bathroom-showers .gallery-product-card {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.section-bathroom-showers .gallery-product-media {
  position: relative;
  aspect-ratio: 3 / 4;
  height: 500px;
  max-height: 520px;
  width: 100%;
  background: radial-gradient(circle at center, #191922 0%, #08080a 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 12px 10px;
  overflow: hidden;
  border-bottom: 1px solid rgba(198, 164, 91, 0.15);
}

.section-bathroom-showers .gallery-product-media img {
  width: 100%;
  height: 100%;
  object-fit: contain !important;
  object-position: center;
  display: block;
  filter: drop-shadow(0 12px 28px rgba(0, 0, 0, 0.75));
  transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1), filter 0.65s ease;
}

.section-bathroom-showers .gallery-product-card:hover .gallery-product-media img {
  transform: scale(1.025);
  filter: drop-shadow(0 16px 36px rgba(198, 164, 91, 0.25)) brightness(1.04);
}

@media (max-width: 1200px) {
  .section-bathroom-showers .gallery-products-grid.shower-cabins-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.8rem;
  }
  .section-bathroom-showers .gallery-product-media {
    height: 460px;
  }
}

@media (max-width: 768px) {
  .section-bathroom-showers .gallery-products-grid.shower-cabins-grid {
    grid-template-columns: 1fr;
    gap: 1.6rem;
  }
  .section-bathroom-showers .gallery-product-media {
    height: 420px;
    aspect-ratio: 3 / 4;
  }
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check if already added
if 'BATHROOM SHOWERS — FULL HEIGHT PRODUCT IMAGES' not in css:
    with open('css/style.css', 'a', encoding='utf-8') as f:
        f.write("\n" + shower_css)
    print("Added full-height shower styling to style.css")
else:
    print("Shower styling already exists in style.css")
