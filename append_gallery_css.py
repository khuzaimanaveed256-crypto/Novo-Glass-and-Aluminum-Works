css_rules = """
/* ==========================================================================
   ARCHITECTURAL PRODUCT GALLERIES (Shower Glass, Partitions & Railings)
   ========================================================================== */

.section-gallery {
  position: relative;
  padding: 6.5rem 2rem 5.5rem;
  background: #0c0c0e;
  background: radial-gradient(circle at 50% 0%, rgba(198, 164, 91, 0.04) 0%, rgba(12, 12, 14, 0.98) 70%);
  border-top: 1px solid rgba(198, 164, 91, 0.12);
  width: 100%;
  overflow: hidden;
}

.section-railings-staircases {
  background: #0a0a0c;
  background: radial-gradient(circle at 50% 0%, rgba(198, 164, 91, 0.035) 0%, rgba(10, 10, 12, 0.99) 70%);
}

.gallery-container {
  max-width: 1360px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.gallery-heading-block {
  text-align: center;
  margin-bottom: 3.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.gallery-title {
  font-family: 'Cinzel', serif;
  font-size: clamp(1.9rem, 3.8vw, 2.75rem);
  font-weight: 700;
  letter-spacing: 0.12em;
  color: #F8F5EE;
  margin: 0.6rem 0 1rem;
  text-transform: uppercase;
  background: linear-gradient(135deg, #FFFFFF 0%, #E9D5A1 50%, #C6A45B 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gallery-gold-divider {
  width: 72px;
  height: 2px;
  background: linear-gradient(90deg, transparent, #C6A45B, transparent);
  margin-bottom: 1.25rem;
}

.gallery-lead {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 1rem;
  line-height: 1.7;
  color: #B3B3B3;
  max-width: 780px;
  margin: 0 auto;
  font-weight: 300;
}

/* Grids */
.gallery-products-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  width: 100%;
}

.gallery-products-grid-3 {
  grid-template-columns: repeat(3, 1fr);
  gap: 2.2rem;
}

/* Product Card */
.gallery-product-card {
  position: relative;
  background: #141416;
  border: 1px solid rgba(198, 164, 91, 0.2);
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease, box-shadow 0.45s ease;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.gallery-product-card:hover {
  transform: translateY(-8px);
  border-color: rgba(229, 197, 131, 0.65);
  box-shadow: 0 22px 50px rgba(0, 0, 0, 0.75), 0 0 35px rgba(198, 164, 91, 0.18);
}

/* Card Media */
.gallery-product-media {
  position: relative;
  aspect-ratio: 4 / 3.4;
  width: 100%;
  overflow: hidden;
  background: #08080a;
}

.gallery-product-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform 0.85s cubic-bezier(0.16, 1, 0.3, 1), filter 0.85s ease;
}

.gallery-product-card:hover .gallery-product-media img {
  transform: scale(1.05);
  filter: brightness(1.06) contrast(1.02);
}

.gallery-zoom-badge {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 32px;
  height: 32px;
  background: rgba(10, 10, 12, 0.75);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(198, 164, 91, 0.35);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #E5C583;
  opacity: 0;
  transform: scale(0.85);
  transition: opacity 0.35s ease, transform 0.35s ease, background 0.35s ease;
  pointer-events: none;
}

.gallery-product-card:hover .gallery-zoom-badge {
  opacity: 1;
  transform: scale(1);
}

/* Card Details */
.gallery-product-details {
  padding: 1.5rem 1.4rem 1.4rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  background: linear-gradient(180deg, #141416 0%, #101012 100%);
  border-top: 1px solid rgba(198, 164, 91, 0.12);
}

.gallery-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  margin-bottom: 0.65rem;
  flex-wrap: wrap;
}

.gallery-product-tag {
  font-family: 'Cinzel', serif;
  font-size: 0.68rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #C6A45B;
  font-weight: 600;
}

.gallery-spec-badge {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.66rem;
  letter-spacing: 0.04em;
  color: #D4AF37;
  background: rgba(198, 164, 91, 0.1);
  padding: 0.2rem 0.55rem;
  border-radius: 20px;
  border: 1px solid rgba(198, 164, 91, 0.22);
}

.gallery-product-title {
  font-family: 'Cinzel', serif;
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: #FAF8F5;
  margin-bottom: 0.6rem;
  line-height: 1.35;
  transition: color 0.35s ease;
}

.gallery-product-card:hover .gallery-product-title {
  color: #E5C583;
}

.gallery-product-desc {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.84rem;
  line-height: 1.55;
  color: #A3A3A8;
  font-weight: 300;
  margin-bottom: 1.3rem;
  flex-grow: 1;
}

/* Card Footer */
.gallery-product-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.8rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.07);
  margin-top: auto;
}

.gallery-price-block {
  display: flex;
  flex-direction: column;
}

.gallery-price-label {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #88888D;
}

.gallery-price-value {
  font-family: 'Cinzel', serif;
  font-size: 0.92rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: #E5C583;
}

.gallery-inquire-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.52rem 0.95rem;
  background: transparent;
  color: #F8F5EE;
  font-family: 'Cinzel', serif;
  font-size: 0.76rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 600;
  border: 1px solid rgba(198, 164, 91, 0.4);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.gallery-inquire-btn:hover {
  background: linear-gradient(135deg, #D4AF37 0%, #AA8028 100%);
  color: #050505;
  border-color: #D4AF37;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.35);
}

.gallery-inquire-btn svg {
  transition: transform 0.35s ease;
}

.gallery-inquire-btn:hover svg {
  transform: translateX(3px);
  stroke: #050505;
}

/* Responsive Breakpoints */
@media (max-width: 1200px) {
  .gallery-products-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.8rem;
  }
  .gallery-products-grid-3 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .section-gallery {
    padding: 4.5rem 1.25rem 3.5rem;
  }
  .gallery-products-grid,
  .gallery-products-grid-3 {
    grid-template-columns: 1fr;
    gap: 1.6rem;
  }
  .gallery-product-media {
    aspect-ratio: 4 / 3;
  }
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    orig = f.read()

if 'ARCHITECTURAL PRODUCT GALLERIES' not in orig:
    with open('css/style.css', 'a', encoding='utf-8') as f:
        f.write("\n" + css_rules)
    print("Appended gallery CSS to style.css successfully!")
else:
    print("Gallery CSS already exists in style.css.")
