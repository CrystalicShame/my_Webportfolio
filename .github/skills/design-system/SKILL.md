---
name: design-system
description: "Use when: updating colors, fonts, spacing, or other design tokens in the portfolio. Ensures consistency across all components."
tags: ["design", "styling", "theming"]
---

# Portfolio Design System Management

## What This Skill Does
This workflow helps you:
- **Update design tokens** (colors, fonts, spacing) in one place
- **Test changes** across all components
- **Ensure consistency** throughout the portfolio
- **Document design decisions** for future updates

## Current Design System

### Color Palette (from `main.py`)
```python
BG          = "#0A0E1A"        # near-black navy (page background)
SURFACE     = "#111827"        # dark card surface
SURFACE2    = "#1C2537"        # slightly lighter card
ACCENT      = "#00D4FF"        # electric cyan (primary accent)
ACCENT2     = "#7C3AED"        # deep violet (secondary accent)
GOLD        = "#F59E0B"        # amber/gold highlight
TEXT_PRIMARY   = "#F1F5F9"     # white text
TEXT_SECONDARY = "#94A3B8"     # gray text
BORDER      = "#1E3A5F"        # border color
```

### Typography
- **Headings**: Courier New, 28px, Bold
- **Body text**: System default, 14-16px
- **Captions**: System default, 12px, TEXT_SECONDARY

### Spacing
- **Component padding**: 20px
- **Section spacing**: 30px
- **Row/column spacing**: 10px
- **Card radius**: 12px

## Updating the Design System

### Step 1: Modify Design Tokens
Edit the constants at the top of `main.py`:
```python
BG          = "#NEW_COLOR"     # description
SURFACE     = "#NEW_COLOR"
```

### Step 2: Verify Impact
Update these sections and test:
1. **Card components** — `section_title()`, reusable card widgets
2. **Navigation bar** — color scheme
3. **Accent elements** — buttons, highlights, borders
4. **Text hierarchy** — headings, body, captions

### Step 3: Test All Pages
Run the app and visit each section:
- Home
- Timeline
- MATLAB
- Blog
- GitHub
- Marks

### Step 4: Cross-Platform Testing
- [ ] Desktop (dark background, readable text?)
- [ ] Mobile (colors visible at small size?)
- [ ] Web (colors render consistently?)

## Common Updates

### Changing the Primary Accent
```python
# Old
ACCENT      = "#00D4FF"        # cyan

# New
ACCENT      = "#FF00FF"        # magenta
```
Then search for `ACCENT` in all components and ensure it looks good.

### Adding a New Color Token
```python
# Add to constants
HIGHLIGHT   = "#FFD700"        # gold highlight

# Use in components
ft.Text(..., color=HIGHLIGHT)
```

### Adjusting Spacing
Replace hardcoded spacing values with named constants:
```python
# Before
padding=20

# After
padding=COMPONENT_PADDING  # where COMPONENT_PADDING = 20
```

## Testing Checklist
- [ ] All pages render without errors
- [ ] Text contrast is sufficient (pass WCAG AA)
- [ ] Colors are used consistently
- [ ] No hardcoded colors remain (all use tokens)
- [ ] Responsive design still works on mobile/tablet/desktop
- [ ] Web build completes: `flet build web -v`

## Design File Structure
```
my_Webportfolio/
├── main.py                          # Design tokens at top of file
├── .github/
│   ├── instructions/
│   │   └── flet-python.instructions.md
│   ├── prompts/
│   │   ├── add-portfolio-section.prompt.md
│   │   └── test-responsive-design.prompt.md
│   └── skills/
│       └── design-system/
│           └── SKILL.md (this file)
├── src/
│   └── assets/                      # Images, icons
└── README.md
```

---

**Pro Tip**: Keep design tokens at the module level, not buried in functions. This makes global updates easy!
