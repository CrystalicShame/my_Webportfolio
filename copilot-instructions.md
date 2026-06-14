# Copilot Instructions for My Web Portfolio

## Project Overview
This is a **Flet-based web portfolio** built with Python. The app is a cross-platform portfolio showcasing projects, timeline, MATLAB work, blog, and GitHub links.

- **Framework**: Flet 0.85.2 (cross-platform UI)
- **Language**: Python 3.10+
- **Build Targets**: Desktop (Windows/Mac/Linux), Web, Mobile (iOS/Android)
- **Design System**: Dark theme with neon accents (cyan, violet, gold)

## Core Principles

### 1. Flet Development
- Use Flet's responsive container system (`ResponsiveRow`, `Column`, `Row`)
- Leverage `ft.Icons` for UI elements
- Manage state at the page/app level
- Keep components reusable via functions (e.g., `section_title()`, `card_widget()`)
- Ensure cross-platform compatibility (mobile, web, desktop)

### 2. Design Consistency
- Adhere to the design token system defined in `main.py`:
  - Background: `#0A0E1A` (near-black navy)
  - Surface: `#111827`, `#1C2537` (card backgrounds)
  - Accent colors: `#00D4FF` (cyan), `#7C3AED` (violet), `#F59E0B` (gold)
  - Text: `#F1F5F9` (primary), `#94A3B8` (secondary)
- Use consistent spacing, padding, and margins
- Apply the same font families across similar elements

### 3. Code Organization
- Keep reusable widgets in separate functions at the top of the file
- Use comment blocks (`# ─────`) to separate sections
- Maintain a clear structure: imports → design tokens → components → pages → main app
- Place state management near the component that uses it

### 4. Responsive Design
- Test on multiple screen sizes (mobile 375px, tablet 768px, desktop 1200px+)
- Use `ResponsiveRow` for adaptive layouts
- Ensure navigation and content are accessible on all devices

## Common Patterns

### Creating a Card
```python
def card_widget(title: str, content: str, icon=None) -> ft.Container:
    return ft.Container(
        content=ft.Column([
            ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
            ft.Text(content, size=14, color=TEXT_SECONDARY),
        ]),
        bgcolor=SURFACE,
        padding=20,
        border_radius=12,
        border=ft.border.all(1, BORDER),
    )
```

### Navigation Bar
- Located at the bottom of the page (mobile-friendly)
- Use `NavigationBar` with `destinations` for routing
- Icons and labels from `NAV_LABELS` and `NAV_ICONS`

## Testing & Building
- Run locally: `uv run flet run` (desktop) or `uv run flet run --web` (web)
- Build for deployment: `flet build web -v`
- Always test responsive behavior before deployment

## Files to Know
- `main.py` — Main app entry point, design tokens, reusable components
- `src/assets/` — Images, icons, and static assets
- `pyproject.toml` — Project metadata and dependencies
- `README.md` — Build and deployment instructions

## When Refactoring
- Preserve the design token system
- Keep component functions pure (no side effects)
- Test on multiple platforms after changes
- Update `IMPROVEMENTS.md` with significant changes

---

**Last Updated**: 2026-05-31
