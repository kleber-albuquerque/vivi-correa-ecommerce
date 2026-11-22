// Script do menu admin responsivo
(function() {
  function initMenu() {
    const burger = document.getElementById('admin-burger');
    const aside = document.querySelector('aside');
    const scrim = document.getElementById('admin-scrim');
    if (!burger || !aside) return;

    function toggleMenu() {
      const aberto = aside.classList.toggle('aberto');
      if (scrim) scrim.classList.toggle('visivel', aberto);
      document.body.classList.toggle('menu-aberto', aberto);
      burger.setAttribute('aria-expanded', String(aberto));
    }

    function fecharMenu() {
      aside.classList.remove('aberto');
      if (scrim) scrim.classList.remove('visivel');
      document.body.classList.remove('menu-aberto');
      burger.setAttribute('aria-expanded', 'false');
    }

    burger.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      toggleMenu();
    });

    if (scrim) {
      scrim.addEventListener('click', function(e) {
        e.preventDefault();
        fecharMenu();
      });
    }

    aside.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        if (window.innerWidth < 900) {
          fecharMenu();
        }
      });
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && aside.classList.contains('aberto')) {
        fecharMenu();
      }
    });

    window.addEventListener('resize', function() {
      if (window.innerWidth >= 900 && aside.classList.contains('aberto')) {
        fecharMenu();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMenu);
  } else {
    initMenu();
  }
})();
