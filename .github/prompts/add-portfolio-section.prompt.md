---
name: add-portfolio-section
description: "Use when: adding a new portfolio section (project, skill, or timeline entry). Creates a reusable component with consistent styling."
---

# Add a New Portfolio Section

I'll help you add a new section to your web portfolio. Follow these steps:

## What You'll Do
1. **Design the component** — sketch out the layout (cards, grid, timeline, etc.)
2. **Create a reusable widget function** — add it near other component functions in `main.py`
3. **Apply design tokens** — use colors, fonts, and spacing from the design system
4. **Add navigation** — ensure it's accessible from the navigation bar
5. **Test responsively** — verify it works on mobile, tablet, and desktop

## Component Template
```python
def section_name(title: str, items: list) -> ft.Column:
    """Build the [Section Name] section with consistent styling."""
    return ft.Column([
        section_title("Section Title", "Optional subtitle"),
        ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Text(item["title"], size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(item["description"], size=14, color=TEXT_SECONDARY),
                ]),
                bgcolor=SURFACE,
                padding=20,
                border_radius=12,
                border=ft.border.all(1, BORDER),
                col={"sm": 12, "md": 6, "lg": 4},
            )
            for item in items
        ], spacing=10, run_spacing=10),
    ], spacing=30)
```

## Navigation Integration
Add to `NAV_LABELS` and `NAV_ICONS`, then handle the route in your page navigation logic.

## Testing Checklist
- [ ] Component displays correctly on desktop
- [ ] Component is responsive on mobile (stacks vertically)
- [ ] All text uses design tokens (TEXT_PRIMARY, TEXT_SECONDARY)
- [ ] Cards use SURFACE or SURFACE2 for background
- [ ] Spacing is consistent with other sections
- [ ] Navigation link works correctly
- [ ] Works in both desktop and web builds

## Common Patterns
- **Grid of cards** → Use `ResponsiveRow` with `col` breakpoints
- **Vertical timeline** → Use `Column` with alternating left/right cards
- **Image gallery** → Use `GridView` or `ResponsiveRow` with `Image` controls
- **Link list** → Use `ListView` with `ListTile` controls

---

**Tip**: Keep your component functions pure (no side effects) and parameterized for reusability!
