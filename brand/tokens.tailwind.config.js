// ============================================================================
// RJ Business Solutions — Tailwind v4 Theme Extension
// Maps brand design tokens from brand.css into Tailwind's theme system.
// Import this into your Tailwind v4 CSS-based config via @config.
//
// Usage in tailwind v4 (CSS-first):
//   @import "./brand/tokens.tailwind.config.js" layer(base);
//   Or reference in @theme block inside your main CSS file.
// ============================================================================

/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
      // ── Font Families ────────────────────────────────────────────────────
      fontFamily: {
        head: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
        body: ['"Inter"', 'system-ui', 'sans-serif'],
        mono: ['"Space Grotesk"', 'ui-monospace', 'monospace'],
      },

      // ── Colors ────────────────────────────────────────────────────────────
      colors: {
        rj: {
          blue:    '#2563eb',   // Primary CTA, links, focus rings
          sky:     '#0ea5e9',   // Accents, gradient stops
          deep:    '#1e3a8a',   // Section dividers, dark headers
          navy:    '#0f172a',   // Body text, hero backgrounds
          white:   '#ffffff',
          soft:    '#f8fafc',   // Page background
          light:   '#eff6ff',   // Section wash, hover
          border:  '#bfdbfe',
          muted:   '#dbeafe',   // Chips, badges
          line:    '#e2e8f0',   // Borders, dividers
          success: '#10b981',
          warning: '#f59e0b',
          danger:  '#ef4444',
          text:    '#0f172a',
          'muted-text': '#475569',
        },
      },

      // ── Font Sizes ────────────────────────────────────────────────────────
      fontSize: {
        h1:    ['72px', { lineHeight: '1',     letterSpacing: '-0.02em', fontWeight: '600' }],
        h2:    ['48px', { lineHeight: '1.1',   letterSpacing: '-0.02em', fontWeight: '600' }],
        h3:    ['28px', { lineHeight: '1.2',   letterSpacing: '-0.01em', fontWeight: '600' }],
        h4:    ['20px', { lineHeight: '1.3',   fontWeight: '600' }],
        body:  ['16px', { lineHeight: '1.6',   fontWeight: '400' }],
        small: ['14px', { lineHeight: '1.5',   fontWeight: '400' }],
        mono:  ['12px', { lineHeight: '1.4',   letterSpacing: '0.14em', fontWeight: '600' }],
      },

      // ── Spacing ───────────────────────────────────────────────────────────
      spacing: {
        // Maps to brand.css spacing scale:
        // 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 40, 48, 56, 64, 80, 100, 120
        1:   '4px',
        1.5: '6px',
        2:   '8px',
        2.5: '10px',
        3:   '12px',
        3.5: '14px',
        4:   '16px',
        5:   '20px',
        6:   '24px',
        7:   '28px',
        8:   '32px',
        10:  '40px',
        12:  '48px',
        14:  '56px',
        16:  '64px',
        20:  '80px',
        24:  '100px',
        28:  '120px',
      },

      // ── Border Radius ─────────────────────────────────────────────────────
      borderRadius: {
        tight: '4px',
        sm:    '6px',
        btn:   '8px',
        input: '10px',
        card:  '14px',
        lg:    '20px',
        xl:    '24px',
        pill:  '999px',
      },

      // ── Box Shadows ───────────────────────────────────────────────────────
      boxShadow: {
        'card':        '0 20px 40px rgba(15, 23, 42, 0.08)',
        'card-hover':  '0 20px 40px rgba(15, 23, 42, 0.15)',
        'featured':    '0 30px 60px rgba(15, 23, 42, 0.15)',
        'deep':        '0 30px 60px rgba(15, 23, 42, 0.25)',
        'cta':         '0 4px 14px rgba(37, 99, 235, 0.35)',
        'cta-hover':   '0 8px 20px rgba(37, 99, 235, 0.4)',
      },

      // ── Background Images (Gradients) ─────────────────────────────────────
      backgroundImage: {
        'grad-primary': 'linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%)',
        'grad-dark':    'linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #2563eb 100%)',
        'grad-light':   'linear-gradient(180deg, #ffffff 0%, #eff6ff 100%)',
      },

      // ── Backdrop Blur ─────────────────────────────────────────────────────
      backdropBlur: {
        nav: '20px',
      },

      // ── Transition Duration ───────────────────────────────────────────────
      transitionDuration: {
        DEFAULT: '150ms',
        spring: '500ms',
      },

      // ── Max Width ─────────────────────────────────────────────────────────
      maxWidth: {
        container: '1280px',
      },

      // ── Screens (Breakpoints) ─────────────────────────────────────────────
      screens: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        '2xl': '1440px',
      },
    },
  },

  // ── Custom Utilities (via plugin) ────────────────────────────────────────
  plugins: [
    function ({ addUtilities }) {
      addUtilities({
        // Radial glow effect for dark surfaces
        '.glow-radial': {
          position: 'relative',
          overflow: 'hidden',
          '&::after': {
            content: '""',
            position: 'absolute',
            right: '-150px',
            top: '-150px',
            width: '600px',
            height: '600px',
            background: 'radial-gradient(circle, rgba(14,165,233,0.4) 0%, transparent 60%)',
            filter: 'blur(60px)',
            pointerEvents: 'none',
          },
        },

        // Gradient text (clips gradient to text fill)
        '.text-gradient': {
          background: 'linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%)',
          '-webkit-background-clip': 'text',
          '-webkit-text-fill-color': 'transparent',
          'background-clip': 'text',
        },

        // Sticky nav with blur
        '.nav-sticky': {
          position: 'sticky',
          top: '0',
          zIndex: '50',
          backdropFilter: 'blur(20px)',
          WebkitBackdropFilter: 'blur(20px)',
          background: 'rgba(255,255,255,0.85)',
          borderBottom: '1px solid #e2e8f0',
        },
      });
    },
  ],
};
