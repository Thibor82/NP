
(() => {
    const CONSENT_NAME = '_ga_consent';
    const ONE_YEAR     = 60 * 60 * 24 * 365;   // en segundos
    const FOUR_DAYS    = 60 * 60 * 24 * 4;
    // Utilidades =========================
    function getCookie(name) {
      const m = document.cookie.match(
        new RegExp('(?:^|; )' + name.replace(/[$()*+./?[\\\]^{|}-]/g, '\\$&') + '=([^;]*)')
      );
      return m ? decodeURIComponent(m[1]) : null;
    }
  
    function setCookie(name, value, maxAge) {
      document.cookie = `${name}=${value}; max-age=${maxAge}; path=/; samesite=Lax`;
    }
  
    function loadGA() {
      if (window.GA_INITIALIZED) return;
      window.GA_INITIALIZED = true;
  
      const s = document.createElement('script');
      s.src = 'https://www.googletagmanager.com/gtag/js?id=G-XXXXX';   // <-- tu ID
      s.async = true;
      document.head.appendChild(s);
  
      window.dataLayer = window.dataLayer || [];
      function gtag(){ dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', 'G-XXXXX', { anonymize_ip: true });
    }
  
    // Lógica principal ====================
    const consent = getCookie(CONSENT_NAME);

    // 1. Ya aceptó → carga GA y termina
    if (consent === 'true') {            // ✔ aceptó
        loadGA();
        return;
    }
    // 2. Ya rechazó → NO mostramos el banner, NO cargamos GA
    if (consent === 'false') {           // ✖ rechazó
        return;                            // no hace nada más
    }
  
      const banner   = document.getElementById('cookie-banner');
      const btnOk    = document.getElementById('btn-accept');
      const btnKo    = document.getElementById('btn-reject');
  
      banner.style.display = 'block';
  
      btnOk.addEventListener('click', () => {
        setCookie(CONSENT_NAME, 'true', ONE_YEAR);
        loadGA();
        banner.remove();
      });
  
      btnKo.addEventListener('click', () => {
        setCookie(CONSENT_NAME, 'false', FOUR_DAYS);
        banner.remove();
      });
  })();
  