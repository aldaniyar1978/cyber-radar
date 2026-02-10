// Theme Switcher & Accessibility Features
// © 2026 Cyber Radar

(function() {
  'use strict';

  // Load saved preferences
  const loadPreferences = () => {
    const theme = localStorage.getItem('theme') || 'dark';
    const fontSize = localStorage.getItem('fontSize') || 'normal';
    const contrast = localStorage.getItem('contrast') || 'normal';
    
    document.documentElement.setAttribute('data-theme', theme);
    document.documentElement.setAttribute('data-font-size', fontSize);
    document.documentElement.setAttribute('data-contrast', contrast);
  };

  // Initialize on page load
  loadPreferences();

  // Create accessibility panel
  const createAccessibilityPanel = () => {
    const panel = document.createElement('div');
    panel.id = 'accessibility-panel';
    panel.innerHTML = `
      <button id="a11y-toggle" aria-label="Toggle accessibility panel" title="Accessibility Settings">
        <svg width="20" height="20" viewBox="0="0 0 24 24" fill="none" stroke="currentColor">
          <circle cx="12" cy="12" r="10"/>
          <path d="M12 6v6l4 2"/>
        </svg>
      </button>
      <div id="a11y-menu" class="hidden">
        <h3>Настройки доступности</h3>
        
        <div class="a11y-section">
          <label>Тема:</label>
          <div class="button-group">
            <button data-theme="light">🌞 Светлая</button>
            <button data-theme="dark">🌙 Темная</button>
          </div>
        </div>
        
        <div class="a11y-section">
          <label>Размер шрифта:</label>
          <div class="button-group">
            <button data-font="small">A</button>
            <button data-font="normal">A</button>
            <button data-font="large">A</button>
          </div>
        </div>
        
        <div class="a11y-section">
          <label>Контраст:</label>
          <div class="button-group">
            <button data-contrast="normal">Обычный</button>
            <button data-contrast="high">Высокий</button>
          </div>
        </div>
        
        <button id="reset-settings">Сбросить</button>
      </div>
    `;
    document.body.appendChild(panel);

    // Toggle menu
    const toggle = document.getElementById('a11y-toggle');
    const menu = document.getElementById('a11y-menu');
    toggle.addEventListener('click', () => {
      menu.classList.toggle('hidden');
    });

    // Theme switcher
    document.querySelectorAll('[data-theme]').forEach(btn => {
      btn.addEventListener('click', () => {
        const theme = btn.dataset.theme;
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        updateActiveButtons();
      });
    });

    // Font size
    document.querySelectorAll('[data-font]').forEach(btn => {
      btn.addEventListener('click', () => {
        const size = btn.dataset.font;
        document.documentElement.setAttribute('data-font-size', size);
        localStorage.setItem('fontSize', size);
        updateActiveButtons();
      });
    });

    // Contrast
    document.querySelectorAll('[data-contrast]').forEach(btn => {
      btn.addEventListener('click', () => {
        const contrast = btn.dataset.contrast;
        document.documentElement.setAttribute('data-contrast', contrast);
        localStorage.setItem('contrast', contrast);
        updateActiveButtons();
      });
    });

    // Reset
    document.getElementById('reset-settings').addEventListener('click', () => {
      localStorage.removeItem('theme');
      localStorage.removeItem('fontSize');
      localStorage.removeItem('contrast');
      loadPreferences();
      updateActiveButtons();
    });

    updateActiveButtons();
  };

  // Update active button states
  const updateActiveButtons = () => {
    const theme = document.documentElement.getAttribute('data-theme');
    const fontSize = document.documentElement.getAttribute('data-font-size');
    const contrast = document.documentElement.getAttribute('data-contrast');

    document.querySelectorAll('[data-theme]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.theme === theme);
    });
    document.querySelectorAll('[data-font]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.font === fontSize);
    });
    document.querySelectorAll('[data-contrast]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.contrast === contrast);
    });
  };

  // Wait for DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createAccessibilityPanel);
  } else {
    createAccessibilityPanel();
  }
})();
