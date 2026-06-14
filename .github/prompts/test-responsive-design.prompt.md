---
name: test-responsive-design
description: "Use when: testing the portfolio's responsiveness across devices. Ensures the layout works on mobile, tablet, and desktop."
---

# Test Responsive Design

## Quick Test Commands
```bash
# Start the app in desktop mode
uv run flet run

# Start the app in web mode (can test multiple window sizes)
uv run flet run --web
```

## Desktop Testing
1. Open the app with `uv run flet run`
2. Resize the window to test breakpoints:
   - **Mobile (375px)**: `Col(sm=12)` — stack vertically
   - **Tablet (768px)**: `Col(md=6)` — half-width columns
   - **Desktop (1200px+)**: `Col(lg=4)` — third-width columns

## Web Browser Testing
1. Run: `uv run flet run --web`
2. Open DevTools (F12) and enable Device Emulation
3. Test these viewport sizes:
   - iPhone 12 (390 × 844)
   - iPad Air (820 × 1180)
   - Desktop (1920 × 1080)

## What to Check
- [ ] **Navigation** — can you access all sections on mobile?
- [ ] **Cards/content** — do they stack properly on mobile?
- [ ] **Images** — are they scaled correctly?
- [ ] **Text readability** — is font size appropriate for all devices?
- [ ] **Spacing** — is padding/margin consistent?
- [ ] **Touch targets** — are buttons/links easy to tap on mobile?
- [ ] **Overflow** — no horizontal scrolling on mobile?
- [ ] **Colors** — all design tokens applied correctly?

## Common Responsive Issues
| Problem | Solution |
|---------|----------|
| Content overflows on mobile | Use `ResponsiveRow` with `col` breakpoints |
| Text is too small on mobile | Use `size` parameter with smaller values, e.g., `size=12` for mobile content |
| Images stretch/distort | Use `Image(fit=ft.ImageFit.CONTAIN)` instead of `FILL` |
| Navigation buttons are too small | Ensure padding is ≥ 44px × 44px (mobile touch minimum) |
| Fixed widths break layout | Replace with `ResponsiveRow` or percentage-based widths |

## Building for Deployment
Once responsive testing is complete:
```bash
# Build for web
flet build web -v

# This creates a production build in build/web/
```

---

**Pro Tip**: Keep browser DevTools open while editing — hot reload lets you test changes instantly!
