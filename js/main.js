/**
 * NOVO GLASS — Cinematic Experience Engine
 * Luxury LED Mirrors & Decorative Glass
 */

(function () {
  'use strict';

  // -------------------------------------------------------------------------
  // 1. Core State & Element Selectors
  // -------------------------------------------------------------------------
  const DOM = {
    body: document.body,
    intro: document.getElementById('cinematicIntro'),
    progressBar: document.getElementById('introProgressBar'),
    skipBtn: document.getElementById('skipIntroBtn'),
    header: document.getElementById('siteHeader'),
    heroMirrorImg: document.getElementById('heroMirrorImg'),
    ledHalo: document.getElementById('ledHalo'),
    mirrorCanvasLayer: document.getElementById('mirrorCanvasLayer'),
    specularGlare: document.getElementById('specularGlare'),
    heroEyebrow: document.getElementById('heroEyebrow'),
    heroHeadline: document.getElementById('heroHeadline'),
    heroDesc: document.getElementById('heroDesc'),
    heroActions: document.getElementById('heroActions'),
    heroPillars: document.getElementById('heroPillars'),
    customModal: document.getElementById('customModal'),
    openModalBtns: [
      document.getElementById('openCustomDesignBtn'),
      document.getElementById('btnCustomDesign'),
      document.getElementById('drawerCustomBtn')
    ].filter(Boolean),
    closeModalBtn: document.getElementById('closeModalBtn'),
    mobileMenuBtn: document.getElementById('mobileMenuBtn'),
    mobileDrawer: document.getElementById('mobileDrawer'),
    customCursor: document.getElementById('customCursor')
  };

  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // -------------------------------------------------------------------------
  // 2. Cinematic Intro Sequence
  // -------------------------------------------------------------------------
  let introTimeline = null;
  let introFinished = false;

  function runCinematicIntro() {
    if (DOM.body) DOM.body.classList.remove('is-loading');
    if (DOM.intro) DOM.intro.style.display = 'none';
    revealHeroExperience(true);
    return;
    if (isReducedMotion || typeof gsap === 'undefined') {
      skipIntroInstantly();
      return;
    }

    introTimeline = gsap.timeline({
      onComplete: finishIntro
    });

    // Intro Film Sequence
    introTimeline
      .set(DOM.intro, { opacity: 1, pointerEvents: 'auto' })
      .to(DOM.progressBar, {
        width: '100%',
        duration: 2.2,
        ease: 'power2.inOut'
      })
      .to('.intro-brand-light-streak', {
        left: '120%',
        duration: 1.6,
        ease: 'power3.inOut'
      }, '-=1.8')
      .to(DOM.intro, {
        opacity: 0,
        scale: 1.05,
        duration: 1.2,
        ease: 'power3.inOut',
        onStart: () => {
          DOM.body.classList.remove('is-loading');
          revealHeroExperience();
        }
      })
      .set(DOM.intro, { display: 'none' });
  }

  function finishIntro() {
    if (introFinished) return;
    introFinished = true;
    DOM.body.classList.remove('is-loading');
    if (DOM.intro) DOM.intro.style.display = 'none';
  }

  function skipIntroInstantly() {
    if (introFinished) return;
    introFinished = true;
    if (introTimeline) introTimeline.kill();
    DOM.body.classList.remove('is-loading');
    if (DOM.intro) DOM.intro.style.display = 'none';
    revealHeroExperience(true);
  }

  // -------------------------------------------------------------------------
  // 3. Hero Visual Reveal Timeline
  // -------------------------------------------------------------------------
  function revealHeroExperience(instant = true) {
    if (DOM.heroDesc) { DOM.heroDesc.style.opacity = '1'; DOM.heroDesc.style.transform = 'none'; }
    if (DOM.heroPillars) { DOM.heroPillars.style.opacity = '1'; DOM.heroPillars.style.transform = 'none'; }
    if (DOM.heroMirrorImg) { DOM.heroMirrorImg.style.transform = 'scale(1)'; }
  }

  // -------------------------------------------------------------------------
  // 4. Interactive LED Lighting Atmosphere Engine
  // -------------------------------------------------------------------------
  const LIGHT_MODES = {
    warm: {
      color: '#f7cca0',
      glow: 'rgba(245, 186, 95, 0.45)',
      lumens: '3,850 LUMENS',
      temp: '3000K WARM GOLD'
    },
    neutral: {
      color: '#ffffff',
      glow: 'rgba(220, 235, 255, 0.38)',
      lumens: '4,100 LUMENS',
      temp: '4000K NATURAL STUDIO'
    },
    dim: {
      color: '#ff9944',
      glow: 'rgba(255, 130, 40, 0.52)',
      lumens: '1,950 LUMENS',
      temp: '2400K CANDLELIGHT'
    }
  };

  function setLightingMode(mode) {
    const data = LIGHT_MODES[mode] || LIGHT_MODES.warm;
    
    // Apply body attribute for CSS custom properties
    DOM.body.setAttribute('data-light', mode);

    // Synchronize All Buttons (if any exist)
    document.querySelectorAll('[data-temp]').forEach(btn => {
      if (btn.getAttribute('data-temp') === mode) {
        btn.classList.add('is-active');
      } else {
        btn.classList.remove('is-active');
      }
    });

    // Subtle flash shimmer on mirror to celebrate lighting shift
    if (DOM.specularGlare && !isReducedMotion) {
      gsap.fromTo(DOM.specularGlare, 
        { opacity: 0.7 },
        { opacity: 0.35, duration: 0.8, ease: 'power2.out' }
      );
    }
  }


  // -------------------------------------------------------------------------
  // 5. Specular Glare & Subtle 3D Camera Tilt On Mousemove
  // -------------------------------------------------------------------------
  let mouseX = 0.5;
  let mouseY = 0.5;
  let targetTiltX = 0;
  let targetTiltY = 0;

  function initCameraParallax() {
    if (isReducedMotion) return;

    window.addEventListener('pointermove', (e) => {
      const { innerWidth, innerHeight } = window;
      const xPercent = (e.clientX / innerWidth) * 100;
      const yPercent = (e.clientY / innerHeight) * 100;

      // Update Specular Glare Coordinates
      document.documentElement.style.setProperty('--mouse-x', `${xPercent}%`);
      document.documentElement.style.setProperty('--mouse-y', `${yPercent}%`);

      // Calculate subtle camera angle tilt
      const normalizedX = (e.clientX / innerWidth) - 0.5;
      const normalizedY = (e.clientY / innerHeight) - 0.5;
      
      targetTiltY = normalizedX * 3.5; // deg
      targetTiltX = -normalizedY * 2.5; // deg

      if (DOM.mirrorCanvasLayer) {
        gsap.to(DOM.mirrorCanvasLayer, {
          rotationY: targetTiltY,
          rotationX: targetTiltX,
          duration: 1.4,
          ease: 'power2.out',
          overwrite: 'auto'
        });
      }
    });
  }

  // -------------------------------------------------------------------------
  // 6. Luxury Custom Cursor
  // -------------------------------------------------------------------------
  function initCustomCursor() {
    if (!DOM.customCursor || window.matchMedia('(pointer: coarse)').matches) return;

    let cursorX = window.innerWidth / 2;
    let cursorY = window.innerHeight / 2;
    let currentX = cursorX;
    let currentY = cursorY;

    window.addEventListener('pointermove', (e) => {
      cursorX = e.clientX;
      cursorY = e.clientY;
    });

    function renderCursor() {
      currentX += (cursorX - currentX) * 0.18;
      currentY += (cursorY - currentY) * 0.18;
      DOM.customCursor.style.transform = `translate(${currentX}px, ${currentY}px)`;
      requestAnimationFrame(renderCursor);
    }
    renderCursor();

    // Hover state for interactive targets
    const interactiveElements = document.querySelectorAll('a, button, input, textarea, .glance-card, .mirror-product-card');
    interactiveElements.forEach(el => {
      el.addEventListener('mouseenter', () => DOM.customCursor.classList.add('is-hovering'));
      el.addEventListener('mouseleave', () => DOM.customCursor.classList.remove('is-hovering'));
    });
  }

  // -------------------------------------------------------------------------
  // 7. Scroll Behavior & GSAP ScrollTrigger
  // -------------------------------------------------------------------------
  function initScrollEffects() {
    // Header Glass Blur on Scroll
    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        DOM.header.classList.add('is-scrolled');
      } else {
        DOM.header.classList.remove('is-scrolled');
      }
    }, { passive: true });

    if (window.ScrollTrigger && !isReducedMotion) {
      gsap.registerPlugin(ScrollTrigger);

      // Parallax on hero mirror as user scrolls into atelier glance
      gsap.to(DOM.heroMirrorImg, {
        yPercent: 12,
        scale: 1.12,
        ease: 'none',
        scrollTrigger: {
          trigger: '#hero',
          start: 'top top',
          end: 'bottom top',
          scrub: 1
        }
      });

      // Mirror collection cards render cleanly with CSS transitions

      // Glance cards render cleanly with CSS transitions
    }
  }

  // -------------------------------------------------------------------------
  // 8. Custom Design Commission Modal (Upgraded 5-Step Atelier Experience)
  // -------------------------------------------------------------------------
  function setupModal() {
    const modal = DOM.customModal;
    const dialog = document.getElementById('customModalDialog');
    const formView = document.getElementById('modalFormView');
    const successView = document.getElementById('modalSuccessView');
    const form = document.getElementById('bespokeForm');
    const presetBanner = document.getElementById('modalPresetBanner');
    const presetName = document.getElementById('modalPresetName');
    const btnClearPreset = document.getElementById('btnClearPreset');
    const btnWhatsAppDirect = document.getElementById('btnWhatsAppDirect');
    const btnSuccessClose = document.getElementById('btnSuccessClose');
    const btnSubmitAnother = document.getElementById('btnSubmitAnother');

    let currentPresetPiece = '';

    function openModal(presetPiece = '') {
      if (!modal) return;

      currentPresetPiece = presetPiece ? presetPiece.trim() : '';

      // Reset to form view
      if (formView) formView.style.display = 'block';
      if (successView) successView.style.display = 'none';

      // Ensure all input fields are completely EMPTY when form loads/opens
      if (form) {
        form.reset();
        const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="tel"], input[type="number"], textarea');
        inputs.forEach(input => { input.value = ''; });
      }
      document.querySelectorAll('.form-field-group.has-error').forEach(g => g.classList.remove('has-error'));

      // Show or hide preset mirror banner
      if (currentPresetPiece) {
        if (presetBanner) presetBanner.style.display = 'inline-flex';
        if (presetName) presetName.textContent = currentPresetPiece;
      } else {
        if (presetBanner) presetBanner.style.display = 'none';
      }

      modal.classList.add('is-active');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';

      if (dialog) dialog.scrollTop = 0;
    }

    function closeModal() {
      if (!modal) return;
      modal.classList.remove('is-active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    // Clear preset button
    if (btnClearPreset) {
      btnClearPreset.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        currentPresetPiece = '';
        if (presetBanner) presetBanner.style.display = 'none';
      });
    }

    // Step 2: Interactive Lighting Cards
    document.querySelectorAll('.lighting-card').forEach(card => {
      card.addEventListener('click', function () {
        document.querySelectorAll('.lighting-card').forEach(c => c.classList.remove('is-selected'));
        this.classList.add('is-selected');
        const radio = this.querySelector('input[type="radio"]');
        if (radio) radio.checked = true;
      });
    });

    // Real-time error removal on input
    const inputsToValidate = [
      { id: 'clientName', group: 'groupClientName' },
      { id: 'clientEmail', group: 'groupClientEmail' },
      { id: 'clientPhone', group: 'groupClientPhone' },
      { id: 'dimWidth', group: 'groupDimWidth' },
      { id: 'dimHeight', group: 'groupDimHeight' }
    ];

    inputsToValidate.forEach(item => {
      const inputEl = document.getElementById(item.id);
      const groupEl = document.getElementById(item.group);
      if (inputEl && groupEl) {
        inputEl.addEventListener('input', () => {
          groupEl.classList.remove('has-error');
        });
      }
    });

    // Validation & Submission Handling
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();

        const nameInput = document.getElementById('clientName');
        const emailInput = document.getElementById('clientEmail');
        const phoneInput = document.getElementById('clientPhone');
        const widthInput = document.getElementById('dimWidth');
        const heightInput = document.getElementById('dimHeight');
        const depthInput = document.getElementById('dimDepth');
        const notesInput = document.getElementById('projectNotes');

        const groupName = document.getElementById('groupClientName');
        const groupEmail = document.getElementById('groupClientEmail');
        const groupPhone = document.getElementById('groupClientPhone');
        const groupWidth = document.getElementById('groupDimWidth');
        const groupHeight = document.getElementById('groupDimHeight');

        let isValid = true;
        let firstInvalidField = null;

        // Reset errors
        [groupName, groupEmail, groupPhone, groupWidth, groupHeight].forEach(g => {
          if (g) g.classList.remove('has-error');
        });

        // Validate Full Name
        const nameVal = nameInput ? nameInput.value.trim() : '';
        if (!nameVal || nameVal.length < 2) {
          if (groupName) groupName.classList.add('has-error');
          if (!firstInvalidField) firstInvalidField = nameInput;
          isValid = false;
        }

        // Validate Email
        const emailVal = emailInput ? emailInput.value.trim() : '';
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailVal || !emailRegex.test(emailVal)) {
          if (groupEmail) groupEmail.classList.add('has-error');
          if (!firstInvalidField) firstInvalidField = emailInput;
          isValid = false;
        }

        // Validate Phone
        const phoneVal = phoneInput ? phoneInput.value.trim() : '';
        if (!phoneVal || phoneVal.replace(/[^0-9]/g, '').length < 6) {
          if (groupPhone) groupPhone.classList.add('has-error');
          if (!firstInvalidField) firstInvalidField = phoneInput;
          isValid = false;
        }

        // Validate Width
        const widthVal = widthInput ? parseFloat(widthInput.value) : 0;
        if (!widthVal || isNaN(widthVal) || widthVal < 5) {
          if (groupWidth) groupWidth.classList.add('has-error');
          if (!firstInvalidField) firstInvalidField = widthInput;
          isValid = false;
        }

        // Validate Height
        const heightVal = heightInput ? parseFloat(heightInput.value) : 0;
        if (!heightVal || isNaN(heightVal) || heightVal < 5) {
          if (groupHeight) groupHeight.classList.add('has-error');
          if (!firstInvalidField) firstInvalidField = heightInput;
          isValid = false;
        }

        if (!isValid) {
          if (firstInvalidField) {
            firstInvalidField.focus();
            firstInvalidField.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
          return;
        }

        // Collect Form Data
        const selectedLighting = document.querySelector('input[name="ledLighting"]:checked')?.value || '3000K – Warm Gold';
        const depthVal = depthInput && depthInput.value.trim() ? depthInput.value.trim() : '2.5';
        const notesVal = notesInput ? notesInput.value.trim() : '';
        const inquiryId = `NV-${Math.floor(10000 + Math.random() * 90000)}`;

        const inquiryRecord = {
          id: inquiryId,
          timestamp: new Date().toISOString(),
          name: nameVal,
          email: emailVal,
          phone: phoneVal,
          lighting: selectedLighting,
          width: widthVal,
          height: heightVal,
          depth: depthVal,
          notes: notesVal,
          referencedMirror: currentPresetPiece
        };

        // Persist inquiry in localStorage so business never loses inquiries
        try {
          const stored = JSON.parse(localStorage.getItem('novoglass_inquiries') || '[]');
          stored.unshift(inquiryRecord);
          localStorage.setItem('novoglass_inquiries', JSON.stringify(stored));
        } catch (storageErr) {
          console.warn('[NOVO GLASS] Inquiry storage notice:', storageErr);
        }

        console.log('[NOVO GLASS Atelier] Bespoke Commission Inquiry Registered:', inquiryRecord);

        // Populate Success Screen
        const successClient = document.getElementById('successClientName');
        const summaryId = document.getElementById('summaryInquiryId');
        const summaryLighting = document.getElementById('summaryLighting');
        const summaryDimensions = document.getElementById('summaryDimensions');
        const summaryEmail = document.getElementById('summaryEmail');
        const summaryPhone = document.getElementById('summaryPhone');

        if (successClient) successClient.textContent = nameVal;
        if (summaryId) summaryId.textContent = `#${inquiryId}`;
        if (summaryLighting) summaryLighting.textContent = selectedLighting;
        if (summaryDimensions) summaryDimensions.textContent = `${widthVal} × ${heightVal} in. (Depth: ${depthVal} in.)`;
        if (summaryEmail) summaryEmail.textContent = emailVal;
        if (summaryPhone) summaryPhone.textContent = phoneVal;

        // Configure WhatsApp Instant Fast-Track Link
        if (btnWhatsAppDirect) {
          const waMessage = encodeURIComponent(
            `Hello NOVO GLASS Atelier,\n\nI would like to request a quotation for a bespoke mirror commission.\n\n` +
            `• Client Name: ${nameVal}\n` +
            `• Email: ${emailVal}\n` +
            `• Phone/WhatsApp: ${phoneVal}\n` +
            `• LED Lighting: ${selectedLighting}\n` +
            `• Dimensions: ${widthVal} × ${heightVal} × ${depthVal} inches\n` +
            (currentPresetPiece ? `• Reference Piece: ${currentPresetPiece}\n` : '') +
            (notesVal ? `• Project Details: ${notesVal}\n` : '') +
            `\nCommission Ref: #${inquiryId}`
          );
          btnWhatsAppDirect.href = `https://wa.me/?text=${waMessage}`;
        }

        // Show Success Screen
        if (formView) formView.style.display = 'none';
        if (successView) successView.style.display = 'block';

        if (dialog) {
          dialog.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    // Success Screen Handlers
    if (btnSuccessClose) {
      btnSuccessClose.addEventListener('click', closeModal);
    }

    if (btnSubmitAnother) {
      btnSubmitAnother.addEventListener('click', () => {
        if (form) {
          form.reset();
          const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="tel"], input[type="number"], textarea');
          inputs.forEach(input => { input.value = ''; });
        }
        document.querySelectorAll('.form-field-group.has-error').forEach(g => g.classList.remove('has-error'));
        const lightWarm = document.getElementById('lightWarm');
        if (lightWarm) lightWarm.click();
        currentPresetPiece = '';
        if (presetBanner) presetBanner.style.display = 'none';

        if (formView) formView.style.display = 'block';
        if (successView) successView.style.display = 'none';

        if (dialog) dialog.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // Trigger button listeners
    DOM.openModalBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openModal();
      });
    });

    document.querySelectorAll('.open-modal-trigger').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const piece = btn.getAttribute('data-piece') || '';
        openModal(piece);
      });
    });

    if (DOM.closeModalBtn) {
      DOM.closeModalBtn.addEventListener('click', closeModal);
    }

    if (DOM.customModal) {
      DOM.customModal.addEventListener('click', (e) => {
        if (e.target === DOM.customModal) closeModal();
      });
    }
  }

  // -------------------------------------------------------------------------
  // 9. Mobile Menu Drawer
  // -------------------------------------------------------------------------
  function setupMobileMenu() {
    if (!DOM.mobileMenuBtn || !DOM.mobileDrawer) return;

    DOM.mobileMenuBtn.addEventListener('click', () => {
      const isOpen = DOM.mobileDrawer.classList.toggle('is-open');
      DOM.mobileMenuBtn.setAttribute('aria-expanded', isOpen);
    });

    document.querySelectorAll('.drawer-link').forEach(link => {
      link.addEventListener('click', () => {
        DOM.mobileDrawer.classList.remove('is-open');
      });
    });
  }

  // -------------------------------------------------------------------------
  // 10. Event Listener Attachments & Boot
  // -------------------------------------------------------------------------
  function initEventListeners() {
    // Skip Intro
    if (DOM.skipBtn) {
      DOM.skipBtn.addEventListener('click', skipIntroInstantly);
    }
    if (DOM.intro) {
      DOM.intro.addEventListener('click', skipIntroInstantly);
    }

    // LED Mode buttons
    document.querySelectorAll('[data-temp]').forEach(btn => {
      btn.addEventListener('click', () => {
        const temp = btn.getAttribute('data-temp');
        setLightingMode(temp);
      });
    });


    // Escape Key to close modal
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && DOM.customModal && DOM.customModal.classList.contains('is-active')) {
        DOM.customModal.classList.remove('is-active');
        document.body.style.overflow = '';
      }
    });
  }

  // -------------------------------------------------------------------------
  // 11. Golden Light Sweep Animation (Page Load Specular Reflection)
  // -------------------------------------------------------------------------
  function initGoldenLightSweep() {
    const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (isReduced) return;

    const brandingRow = document.getElementById('heroBrandingRow');
    if (!brandingRow) return;

    // Trigger after initial page paint
    setTimeout(() => {
      brandingRow.classList.add('play-golden-sweep');
    }, 320);

    // Clean up animation class after 2.8s
    setTimeout(() => {
      brandingRow.classList.remove('play-golden-sweep');
      brandingRow.classList.add('sweep-completed');
    }, 2850);
  }

  // Boot Application
  document.addEventListener('DOMContentLoaded', () => {
    initEventListeners();
    setupModal();
    setupMobileMenu();
    initCustomCursor();
    initCameraParallax();
    initScrollEffects();
    runCinematicIntro();
    initGoldenLightSweep();
  });

})();
