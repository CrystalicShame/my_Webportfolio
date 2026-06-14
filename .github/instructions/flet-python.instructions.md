---
name: flet-python-guidelines
description: Use when working with Flet Python files. Ensures proper state management, responsive design, and cross-platform compatibility.
applyTo: "**/*.py"
---

# Flet Python Development Guidelines

## Before Making Changes
1. **Understand the current component tree** — trace the parent-child relationships
2. **Check responsive behavior** — will this change work on mobile, tablet, and desktop?
3. **Review design tokens** — use the colors and styles defined in the design system, not hardcoded values
4. **Test state updates** — does the UI update correctly when state changes?

## Code Style
- Use `snake_case` for function and variable names
- Use `UPPER_CASE` for constants (design tokens, config values)
- Add docstrings to complex functions
- Keep functions focused on a single responsibility
- Use type hints where helpful (e.g., `def build_card(title: str) -> ft.Container:`)

## Component Best Practices
- **Separate presentation from logic**: Functions that build UI should not contain complex business logic
- **Reuse components**: Create widget functions for repeated patterns (cards, buttons, headers)
- **Use control naming**: Assign `name` to interactive controls for easy state tracking
- **Handle events properly**: Use lambda or bound methods for `on_click` handlers
- **Manage scroll position**: Use `ScrollView` with `auto_scroll=True` for dynamic content

## State Management
- Keep state at the page or app level for shared data
- Use control properties directly when possible (e.g., `textfield.value`)
- Update the UI by calling `page.update()` after state changes
- Avoid circular dependencies between components

## Responsive Layout
```python
# Use ResponsiveRow for fluid, mobile-first layouts
ft.ResponsiveRow([
    ft.Container(
        content=...,
        col={"sm": 12, "md": 6, "lg": 4},  # Full width on mobile, half on tablet, third on desktop
    ),
], spacing=10, run_spacing=10)
```

## Common Issues to Avoid
- ❌ Hardcoding colors instead of using design tokens
- ❌ Forgetting to call `page.update()` after state changes
- ❌ Using fixed widths/heights instead of responsive layouts
- ❌ Not testing on mobile screen sizes
- ❌ Deeply nested component hierarchies (simplify with helper functions)

## Testing Checklist Before Commit
- [ ] Runs without errors: `uv run flet run`
- [ ] Responsive on mobile (375px width)
- [ ] Responsive on tablet (768px width)
- [ ] Responsive on desktop (1200px+ width)
- [ ] All colors use design tokens from `main.py`
- [ ] No hardcoded values for spacing/sizing (use consistent units)
- [ ] Links and navigation work correctly
- [ ] Web version builds: `flet build web -v` (if applicable)
