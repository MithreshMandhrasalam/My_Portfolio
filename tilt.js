/**
 * Cursor-tracking 3D tilt effect
 * Works on any elements matching the given selectors.
 */
function initTilt(selector, options = {}) {
  const {
    maxTilt   = 14,   // max degrees of rotation
    glare     = true, // subtle shine that follows cursor
    scale     = 1.04, // tiny scale-up on hover
    speed     = 60,   // ms for live tracking (lower = snappier)
    resetSpeed = 500, // ms to snap back on leave
  } = options;

  const cards = document.querySelectorAll(selector);

  cards.forEach(card => {
    // Inject a glare overlay element
    if (glare) {
      const shine = document.createElement('div');
      shine.className = '__tilt-shine';
      shine.style.cssText = `
        position:absolute; inset:0; border-radius:inherit;
        pointer-events:none; opacity:0;
        background: radial-gradient(circle at 50% 50%, rgba(34,211,238,0.18) 0%, transparent 65%);
        transition: opacity 0.3s;
      `;
      card.style.position = card.style.position || 'relative';
      card.style.overflow  = 'hidden';
      card.appendChild(shine);
    }

    card.addEventListener('mousemove', e => {
      const rect    = card.getBoundingClientRect();
      const cx      = rect.left + rect.width  / 2;
      const cy      = rect.top  + rect.height / 2;
      const dx      = (e.clientX - cx) / (rect.width  / 2);  // -1 → 1
      const dy      = (e.clientY - cy) / (rect.height / 2);  // -1 → 1

      const rotX = -dy * maxTilt;
      const rotY =  dx * maxTilt;

      card.style.transition = `transform ${speed}ms ease-out`;
      card.style.transform  = `perspective(900px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale(${scale})`;

      // Move the glare highlight to follow the cursor
      if (glare) {
        const shine = card.querySelector('.__tilt-shine');
        if (shine) {
          const px = ((e.clientX - rect.left) / rect.width)  * 100;
          const py = ((e.clientY - rect.top)  / rect.height) * 100;
          shine.style.background = `radial-gradient(circle at ${px}% ${py}%, rgba(34,211,238,0.2) 0%, transparent 65%)`;
          shine.style.opacity = '1';
        }
      }
    });

    card.addEventListener('mouseleave', () => {
      card.style.transition = `transform ${resetSpeed}ms ease-out`;
      card.style.transform  = 'perspective(900px) rotateX(0deg) rotateY(0deg) scale(1)';
      if (glare) {
        const shine = card.querySelector('.__tilt-shine');
        if (shine) shine.style.opacity = '0';
      }
    });
  });
}

// Init on page load for whichever cards exist on the current page
document.addEventListener('DOMContentLoaded', () => {
  initTilt('.proj-card',  { maxTilt: 12, scale: 1.04 });
  initTilt('.cert-card',  { maxTilt: 14, scale: 1.03 });
});
