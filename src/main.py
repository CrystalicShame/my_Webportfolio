"""

Andre Cavota Web_Portfolio        Computer Programming I (Semester 1, 2026)
Built with Flet 0.85.2

"""

import pathlib
import urllib.parse
import flet as ft

try:
    import flet_video as fv
except ImportError:
    fv = None

APP_DIR = pathlib.Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"

# ─────────────────────────────────────────────
# DESIGN TOKENS
# ─────────────────────────────────────────────
BG          = "#0A0E1A"        # near-black navy
SURFACE     = "#111827"        # dark card surface
SURFACE2    = "#1C2537"        # slightly lighter card
ACCENT      = "#178BFF"        # bright portfolio blue
ACCENT2     = "#7C3AED"        # deep violet
GOLD        = "#F59E0B"        # amber/gold highlight
TEXT_PRIMARY   = "#F1F5F9"
TEXT_SECONDARY = "#94A3B8"
BORDER      = "#1E3A5F"
RED         = "#EF4444"
TEAL        = "#10B981"
ORANGE      = "#F97316"
DEFAULT_VIEWPORT_WIDTH = 1280
MOBILE_BREAKPOINT = 720
NARROW_BREAKPOINT = 960

NAV_LABELS  = ["Home", "Timeline", "MATLAB", "Blog", "GitHub"]
NAV_ICONS   = [
    ft.Icons.HOME_ROUNDED,
    ft.Icons.TIMELINE_ROUNDED,
    ft.Icons.CALCULATE_ROUNDED,
    ft.Icons.ARTICLE_ROUNDED,
    ft.Icons.CODE_ROUNDED,
    ft.Icons.GRADE_ROUNDED,
]
MATLAB_CERTIFICATE_URLS = {
    # Paste online certificate URLs here when they are ready.
    # Empty values keep the "View Certificate" buttons inactive for now.
    "core_matlab_skills": "https://matlabacademy.mathworks.com/progress/share/learningpath/certificate.html?id=75bcd81d-afb2-4f64-b287-a4006584a80d",
    "visualization_in_matlab": "https://matlabacademy.mathworks.com/progress/share/learningpath/certificate.html?id=2fb8214a-85e8-4111-a6dd-e8b776210cfa",
    "matlab_onramp": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=58fcafac-8132-4604-9feb-fe6946c6c28c",
    "calculations_with_vectors_and_matrices": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=5a4f52d0-e2dd-42f4-8c9e-c20ad89d8132",
    "the_why_and_how_of_functions": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=c239b0ec-899c-4195-8f20-953f1ad043cd",
    "simulink_onramp": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=cb0cf204-9316-49e0-901b-1b62dcda970b",
    "circuit_simulation_onramp": "",
}
TYPING_CERTIFICATE_URL = "https://www.typing.com/apiv1/student/tests/408036084/166558181/certificate?language=en"
# Paste the MATLAB project link here when it is ready.
MATLAB_PROJECT_URL = "https://drive.google.com/file/d/19TaatuDSXP5pxEKU1XURPxRdiYIVOy3i/view?usp=sharing"
MINESHIELD_APP_URL = "https://drive.google.com/file/d/1loRTJW1Q7iFPdWvqulKkPhQlBwEKK4Hz/view?usp=sharing"
BLOG_VIDEO_FILE = "Video_Contribution.mp4"
BLOG_VIDEO_RESOURCE = urllib.parse.quote(BLOG_VIDEO_FILE)
CONTACT_EMAIL = "cavotaanderson@gmail.com"
CONTACT_EMAIL_URL = f"https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=cm&to={CONTACT_EMAIL}"
CORE_MATLAB_SKILLS_CERTIFICATE_KEY = "core_matlab_skills"
VISUALIZATION_IN_MATLAB_CERTIFICATE_KEY = "visualization_in_matlab"
MATLAB_ONRAMP_CERTIFICATE_KEY = "matlab_onramp"
CALCULATIONS_WITH_VECTORS_AND_MATRICES_CERTIFICATE_KEY = "calculations_with_vectors_and_matrices"
THE_WHY_AND_HOW_OF_FUNCTIONS_CERTIFICATE_KEY = "the_why_and_how_of_functions"
SIMULINK_ONRAMP_CERTIFICATE_KEY = "simulink_onramp"


def no_action(e: ft.ControlEvent) -> None:
    pass


def certificate_url(certificate_key: str) -> str | None:
    certificate_url = MATLAB_CERTIFICATE_URLS.get(certificate_key, "").strip()
    if certificate_url.startswith(("https://", "http://")):
        return certificate_url
    return None


def open_certificate(certificate_key: str):
    def handle_click(e: ft.ControlEvent) -> None:
        url = certificate_url(certificate_key)
        if url:
            e.page.launch_url(url, web_popup_window_name=ft.UrlTarget.BLANK)

    return handle_click


# ─────────────────────────────────────────────
# REUSABLE WIDGETS
# ─────────────────────────────────────────────

def section_title(text: str, subtitle: str = "") -> ft.Column:
    items = [
        ft.Text(
            text,
            size=28,
            weight=ft.FontWeight.BOLD,
            color=TEXT_PRIMARY,
            font_family="Courier New",
        ),
        ft.Container(
            width=60,
            height=3,
            bgcolor=ACCENT,
            border_radius=2,
            margin=ft.Margin(0, 4, 0, 0),
        ),
    ]
    if subtitle:
        items.append(
            ft.Text(subtitle, size=14, color=TEXT_SECONDARY, italic=True)
        )
    return ft.Column(controls=items, spacing=4)


def card(content: ft.Control, padding: int = 20) -> ft.Container:
    return ft.Container(
        content=content,
        bgcolor=SURFACE,
        border_radius=12,
        padding=padding,
        border=ft.Border(
            left=ft.BorderSide(1, BORDER),
            top=ft.BorderSide(1, BORDER),
            right=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
        ),
    )


def badge(label: str, color: str = ACCENT) -> ft.Container:
    return ft.Container(
        content=ft.Text(label, size=11, color=color, weight=ft.FontWeight.W_600),
        bgcolor=ft.Colors.with_opacity(0.12, color),
        border_radius=20,
        padding=ft.Padding(10, 4, 10, 4),
        border=ft.Border(
            left=ft.BorderSide(1, ft.Colors.with_opacity(0.4, color)),
            top=ft.BorderSide(1, ft.Colors.with_opacity(0.4, color)),
            right=ft.BorderSide(1, ft.Colors.with_opacity(0.4, color)),
            bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.4, color)),
        ),
    )


# ─────────────────────────────────────────────
# PAGE BUILDERS
# ─────────────────────────────────────────────

def hidden_scroll() -> ft.ScrollMode:
    return ft.ScrollMode.HIDDEN


def portfolio_scrollbar_theme() -> ft.ScrollbarTheme:
    return ft.ScrollbarTheme(
        thumb_visibility=False,
        track_visibility=False,
        thickness=0,
        radius=6,
        thumb_color=ft.Colors.TRANSPARENT,
        track_color=ft.Colors.TRANSPARENT,
        track_border_color=ft.Colors.TRANSPARENT,
        min_thumb_length=68,
        interactive=False,
    )


def current_view_width(viewport_width: float | int | None) -> float:
    try:
        width = float(viewport_width or DEFAULT_VIEWPORT_WIDTH)
    except (TypeError, ValueError):
        width = DEFAULT_VIEWPORT_WIDTH
    return max(320, width)


def available_width(
    viewport_width: float | int | None,
    max_width: int,
    side_padding: int = 24,
    min_width: int = 280,
) -> float:
    return max(min_width, min(max_width, current_view_width(viewport_width) - side_padding))


def build_home_legacy() -> ft.Column:
    hero = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src="profile_picture.jpg",
                                fit="cover",
                                width=80,
                                height=80,
                            ),
                            width=80,
                            height=80,
                            border_radius=40,
                            clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "Andre Cavota",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=TEXT_PRIMARY,
                                    font_family="Courier New",
                                ),
                                ft.Text(
                                    "Computer Programming I  ·  Semester 1, 2026",
                                    size=13,
                                    color=TEXT_SECONDARY,
                                ),
                            ],
                            spacing=2,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Divider(color=BORDER, height=24),
                ft.Text(
                    "An engineering degree does not make the engineer,\n"
                    "its the ability to see a challenge as an exercise.",
                    size=15,
                    color=TEXT_SECONDARY,
                ),
                ft.Row(
                    controls=[
                        badge("Python"),
                        badge("Firebase&ReactNative",RED),
                        badge("MATLAB", GOLD),
                        badge("GitHub", ACCENT2),
                        badge("Projects", "#10B981"),
                    ],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
            ],
            spacing=18,
        ),
        bgcolor=SURFACE,
        border_radius=16,
        padding=30,
        border=ft.Border(
            left=ft.BorderSide(2, ACCENT),
            top=ft.BorderSide(1, BORDER),
            right=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
        ),
    )

    stats_row = ft.Row(
        controls=[
            card(
                ft.Column(
                    controls=[
                        ft.Text("15%", size=32, weight=ft.FontWeight.BOLD, color=ACCENT),
                        ft.Text("CA Weighting", size=12, color=TEXT_SECONDARY),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                ),
                padding=24,
            ),
            card(
                ft.Column(
                    controls=[
                        ft.Text("7", size=32, weight=ft.FontWeight.BOLD, color=GOLD),
                        ft.Text("MATLAB Courses", size=12, color=TEXT_SECONDARY),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                ),
                padding=24,
            ),
            card(
                ft.Column(
                    controls=[
                        ft.Text("20", size=32, weight=ft.FontWeight.BOLD, color=ACCENT2),
                        ft.Text("Team Members", size=12, color=TEXT_SECONDARY),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                ),
                padding=24,
            ),
        ],
        spacing=12,
        wrap=True,
    )

    rubric_rows = [
        ("Flet Implementation", "30", "Code structure and deployment", ACCENT),
        ("GitHub Evidence", "25", "Documentation of your commits", ACCENT2),
        ("Blog & Video", "25", "Clarity of core programming concepts", GOLD),
        ("MATLAB Courses", "20", "Verification of 7 MathWorks certificates", "#10B981"),
    ]

    rubric_table = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text("Category", size=12, weight=ft.FontWeight.BOLD,
                            color=TEXT_SECONDARY, expand=3),
                    ft.Text("Marks", size=12, weight=ft.FontWeight.BOLD,
                            color=TEXT_SECONDARY, expand=1),
                    ft.Text("Details", size=12, weight=ft.FontWeight.BOLD,
                            color=TEXT_SECONDARY, expand=4),
                ],
            ),
            ft.Divider(color=BORDER, height=8),
            *[
                ft.Row(
                    controls=[
                        ft.Text(cat, size=13, color=TEXT_PRIMARY,
                                weight=ft.FontWeight.W_600, expand=3),
                        ft.Container(
                            content=ft.Text(
                                marks, size=13, color=col,
                                weight=ft.FontWeight.BOLD
                            ),
                            expand=1,
                        ),
                        ft.Text(detail, size=12, color=TEXT_SECONDARY, expand=4),
                    ],
                    spacing=8,
                )
                for cat, marks, detail, col in rubric_rows
            ],
        ],
        spacing=10,
    )

    return ft.Column(
        controls=[
            hero,
            ft.Container(height=8),
            stats_row,
            ft.Container(height=8),
            card(
                ft.Column(
                    controls=[
                        section_title("Assessment Breakdown", "CA Weighting — 15% of total"),
                        ft.Container(height=12),
                        rubric_table,
                    ],
                    spacing=4,
                ),
            ),
        ],
        spacing=12,
        scroll=hidden_scroll(),
        expand=True,
    )


def build_timeline_legacy() -> ft.Column:
    weeks = [
        ("Week 1", "Project kickoff, repo setup, assigned metallurgical module.",
         ["Repo", "Setup"]),
        ("Week 2", "Scaffolded Flet app structure, defined routing with ft.run().",
         ["Flet", "Routing"]),
        ("Week 3", "Implemented data-input forms for material cost calculations.",
         ["Forms", "UI"]),
        ("Week 4", "Integrated cost formula: Σ(Qᵢ × Pᵢ) + Overheads into backend.",
         ["Math", "Backend"]),
        ("Week 5", "Code review on two PRs; fixed ft.Colors deprecation warnings.",
         ["Review", "Bug Fix"]),
        ("Week 6", "Added results dashboard with ft.DataTable and bar charts.",
         ["Charts", "Data"]),
        ("Week 7", "Unit tests, deployment to Flet web, final documentation.",
         ["Testing", "Deploy"]),
    ]

    timeline_items = []
    for i, (week, desc, tags) in enumerate(weeks):
        is_last = i == len(weeks) - 1
        timeline_items.append(
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Container(
                                width=14,
                                height=14,
                                bgcolor=ACCENT,
                                border_radius=7,
                                border=ft.Border(
                                    left=ft.BorderSide(2, BG),
                                    top=ft.BorderSide(2, BG),
                                    right=ft.BorderSide(2, BG),
                                    bottom=ft.BorderSide(2, BG),
                                ),
                            ),
                            ft.Container(
                                width=2,
                                height=60 if not is_last else 0,
                                bgcolor=BORDER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            week,
                                            size=14,
                                            weight=ft.FontWeight.BOLD,
                                            color=ACCENT,
                                        ),
                                        *[badge(t) for t in tags],
                                    ],
                                    spacing=8,
                                    wrap=True,
                                ),
                                ft.Text(desc, size=13, color=TEXT_SECONDARY),
                            ],
                            spacing=6,
                        ),
                        expand=True,
                        padding=ft.Padding(0, 0, 0, 12),
                    ),
                ],
                spacing=16,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
        )

    return ft.Column(
        controls=[
            section_title(
                "Project Timeline",
                "Weekly log of individual contributions to the group project",
            ),
            ft.Container(height=16),
            card(
                ft.Column(controls=timeline_items, spacing=0),
            ),
        ],
        spacing=4,
        scroll=hidden_scroll(),
        expand=True,
    )


def build_matlab_legacy() -> ft.Column:
    courses = [
        ("Simulink Onramp", "Completed", True, SIMULINK_ONRAMP_CERTIFICATE_KEY),
        ("MATLAB Onramp", "Completed", True, MATLAB_ONRAMP_CERTIFICATE_KEY),
        (
            "Core MATLAB Skills",
            "Completed",
            True,
            CORE_MATLAB_SKILLS_CERTIFICATE_KEY,
        ),
        (
            "Calculations with Vectors and Matrices",
            "Completed",
            True,
            CALCULATIONS_WITH_VECTORS_AND_MATRICES_CERTIFICATE_KEY,
        ),
        (
            "Visualization in MATLAB",
            "Completed",
            True,
            VISUALIZATION_IN_MATLAB_CERTIFICATE_KEY,
        ),
        (
            "The Why and How of Functions",
            "Completed",
            True,
            THE_WHY_AND_HOW_OF_FUNCTIONS_CERTIFICATE_KEY,
        ),
        (
            "Circuit Simulation Onramp",
            "Completed",
            True,
            "circuit_simulation_onramp",
        ),
    ]

    certificate_gallery = ft.Container(visible=False)
    view_button_label = ft.Text(
        "View Certificates",
        color=TEXT_PRIMARY,
        size=13,
        weight=ft.FontWeight.BOLD,
    )

    def toggle_certificates(e: ft.ControlEvent) -> None:
        certificate_gallery.visible = not certificate_gallery.visible
        view_button_label.value = (
            "Hide Certificates" if certificate_gallery.visible else "View Certificates"
        )
        e.page.update()

    view_certificates_button = ft.Container(
        width=184,
        height=40,
        border_radius=6,
        bgcolor=ACCENT,
        padding=ft.Padding(12, 0, 12, 0),
        on_click=toggle_certificates,
        tooltip="Show MATLAB certificates",
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.LINK_ROUNDED, color=TEXT_PRIMARY, size=18),
                view_button_label,
            ],
            spacing=8,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    certificate_gallery.content = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.LINK_ROUNDED,
                                color=GOLD,
                                size=22,
                            ),
                            ft.Text(
                                "MathWorks Certificates",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=TEXT_PRIMARY,
                            ),
                        ],
                        spacing=10,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE_ROUNDED,
                        icon_color=TEXT_SECONDARY,
                        tooltip="Hide certificates",
                        on_click=toggle_certificates,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        width=344,
                        height=180,
                        border_radius=8,
                        padding=ft.Padding(12, 12, 12, 10),
                        bgcolor=SURFACE2,
                        ink=certificate_url(link_file) is not None,
                        on_click=(
                            open_certificate(link_file)
                            if certificate_url(link_file)
                            else no_action
                        ),
                        tooltip=f"{name} certificate link pending",
                        border=ft.Border(
                            left=ft.BorderSide(1, BORDER),
                            top=ft.BorderSide(1, BORDER),
                            right=ft.BorderSide(1, BORDER),
                            bottom=ft.BorderSide(1, BORDER),
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    height=82,
                                    border_radius=6,
                                    bgcolor=BG,
                                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                    content=ft.Icon(
                                        ft.Icons.LINK_ROUNDED,
                                        size=30,
                                        color=ACCENT,
                                    ),
                                    alignment=ft.Alignment(0, 0),
                                ),
                                ft.Text(
                                    name,
                                    size=12,
                                    color=TEXT_PRIMARY,
                                    weight=ft.FontWeight.W_600,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                                ft.Text(
                                    "View Certificate",
                                    size=12,
                                    color=ACCENT,
                                    weight=ft.FontWeight.BOLD,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                            ],
                            spacing=8,
                        ),
                    )
                    for name, status, done, link_file in courses
                ],
                spacing=12,
                run_spacing=12,
                wrap=True,
            ),
        ],
        spacing=14,
    )
    certificate_gallery.bgcolor = SURFACE
    certificate_gallery.border_radius = 10
    certificate_gallery.padding = ft.Padding(16, 14, 16, 16)
    certificate_gallery.border = ft.Border(
        left=ft.BorderSide(1, BORDER),
        top=ft.BorderSide(1, BORDER),
        right=ft.BorderSide(1, BORDER),
        bottom=ft.BorderSide(1, BORDER),
    )

    course_cards = []
    for idx, (name, status, done, link_file) in enumerate(courses):
        col = "#10B981" if done else TEXT_SECONDARY
        icon = ft.Icons.CHECK_CIRCLE_ROUNDED if done else ft.Icons.RADIO_BUTTON_UNCHECKED
        cert_url = certificate_url(link_file)
        cert_action = ft.IconButton(
            icon=ft.Icons.OPEN_IN_NEW_ROUNDED,
            icon_color=ACCENT if cert_url else TEXT_SECONDARY,
            icon_size=19,
            width=34,
            height=34,
            padding=4,
            tooltip=f"View {name} certificate" if cert_url else f"{name} certificate link pending",
            url=cert_url,
            disabled=cert_url is None,
        )
        course_cards.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                str(idx + 1),
                                size=13,
                                weight=ft.FontWeight.BOLD,
                                color=BG,
                            ),
                            width=28,
                            height=28,
                            bgcolor=GOLD,
                            border_radius=14,
                            alignment=ft.Alignment(0, 0),
                        ),
                        ft.Text(name, size=14, color=TEXT_PRIMARY, expand=True),
                        ft.Icon(icon, color=col, size=20),
                        ft.Text(status, size=12, color=col),
                        cert_action,
                    ],
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=SURFACE2,
                border_radius=10,
                padding=ft.Padding(16, 12, 16, 12),
                border=ft.Border(
                    left=ft.BorderSide(2, GOLD if done else BORDER),
                    top=ft.BorderSide(1, BORDER),
                    right=ft.BorderSide(1, BORDER),
                    bottom=ft.BorderSide(1, BORDER),
                ),
            )
        )

    progress = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text("7 / 7 Courses Completed", size=13,
                            color=TEXT_SECONDARY),
                    ft.Text("100%", size=13, color="#10B981",
                            weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.ProgressBar(value=1.0, bgcolor=SURFACE2, color="#10B981"),
        ],
        spacing=6,
    )

    progress_actions = ft.Column(
        controls=[
            progress,
            ft.Row(
                controls=[view_certificates_button],
                alignment=ft.MainAxisAlignment.END,
            ),
        ],
        spacing=12,
    )

    return ft.Column(
        controls=[
            section_title(
                "MATLAB Achievement Hub",
                "Proof of completion — 7 MathWorks Learning Center courses",
            ),
            ft.Container(height=16),
            card(progress_actions, padding=16),
            certificate_gallery,
            ft.Container(height=8),
            *course_cards,
        ],
        spacing=8,
        scroll=hidden_scroll(),
        expand=True,
    )
def build_matlab(viewport_width: float | int | None = None) -> ft.Column:
    view_width = current_view_width(viewport_width)
    is_mobile = view_width < MOBILE_BREAKPOINT
    content_width = available_width(view_width, 1280, 28 if is_mobile else 72)
    path_card_width = min(628, content_width)
    course_card_width = min(410, content_width)
    metric_width = 180 if content_width >= 780 else max(132, (content_width - 18) / 2)

    def line_border(color: str = BORDER, opacity: float = 0.74) -> ft.Border:
        side = ft.BorderSide(1, ft.Colors.with_opacity(opacity, color))
        return ft.Border(left=side, top=side, right=side, bottom=side)

    def grid_background(width: int = 2000, height: int = 1360) -> list[ft.Container]:
        verticals = [
            ft.Container(
                left=x,
                top=0,
                width=1,
                height=height,
                bgcolor=ft.Colors.with_opacity(0.22, BORDER),
            )
            for x in range(0, width + 1, 100)
        ]
        horizontals = [
            ft.Container(
                left=0,
                top=y,
                width=width,
                height=1,
                bgcolor=ft.Colors.with_opacity(0.18, BORDER),
            )
            for y in range(0, height + 1, 64)
        ]
        return verticals + horizontals

    def certificate_button(certificate_key: str) -> ft.TextButton:
        cert_url = certificate_url(certificate_key)
        is_ready = cert_url is not None
        text_color = "#4BA3FF" if is_ready else TEXT_SECONDARY
        border_opacity = 0.62 if is_ready else 0.48
        return ft.TextButton(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        ft.Icons.OPEN_IN_NEW_ROUNDED,
                        size=14,
                        color=text_color,
                    ),
                    ft.Text(
                        "View Certificate",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color=text_color,
                    ),
                ],
                spacing=7,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            url=cert_url,
            height=34,
            disabled=not is_ready,
            tooltip="View certificate" if is_ready else "Certificate link pending",
            style=ft.ButtonStyle(
                color=text_color,
                bgcolor="#0E2743" if is_ready else "#0B1C31",
                padding=ft.Padding(0, 0, 0, 0),
                side=ft.BorderSide(1, ft.Colors.with_opacity(border_opacity, ACCENT)),
                shape=ft.RoundedRectangleBorder(radius=7),
                overlay_color=ft.Colors.with_opacity(0.12, ACCENT),
                mouse_cursor=ft.MouseCursor.CLICK if is_ready else ft.MouseCursor.BASIC,
            ),
        )

    def metric_card(value: str, label: str, sublabel: str, width: int) -> ft.Container:
        return ft.Container(
            width=min(width, metric_width),
            height=62,
            border_radius=10,
            bgcolor="#10223B",
            border=line_border(ACCENT, 0.44),
            padding=ft.Padding(14 if is_mobile else 20, 0, 12 if is_mobile else 18, 0),
            content=ft.Row(
                controls=[
                    ft.Text(
                        value,
                        size=24 if is_mobile else 28,
                        color="#4BA3FF",
                        weight=ft.FontWeight.BOLD,
                        font_family="Courier New",
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                label,
                                size=12,
                                color=TEXT_PRIMARY,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(sublabel, size=12, color=TEXT_SECONDARY),
                        ],
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def section_label(label: str) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Container(width=4, height=24, border_radius=2, bgcolor="#4BA3FF"),
                ft.Text(
                    label.upper(),
                    size=12,
                    color=TEXT_SECONDARY,
                    weight=ft.FontWeight.BOLD,
                    font_family="Courier New",
                ),
            ],
            spacing=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def provider_line() -> ft.Row:
        return ft.Row(
            controls=[
                ft.Icon(ft.Icons.CHANGE_HISTORY_ROUNDED, color=ORANGE, size=12),
                ft.Text("MathWorks Training Services", size=12, color=TEXT_SECONDARY),
            ],
            spacing=6,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def date_status(date_text: str, compact: bool = False) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.CALENDAR_MONTH_ROUNDED, color="#A78BFA", size=13),
                        ft.Text(date_text, size=12, color=TEXT_SECONDARY),
                    ],
                    spacing=7,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            width=7,
                            height=7,
                            border_radius=4,
                            bgcolor=TEAL,
                            shadow=ft.BoxShadow(
                                blur_radius=8,
                                color=ft.Colors.with_opacity(0.55, TEAL),
                            ),
                        ),
                        ft.Text(
                            "100% complete" if not compact else "100%",
                            size=12,
                            color="#5EF5A4",
                            weight=ft.FontWeight.BOLD,
                            font_family="Courier New",
                        ),
                    ],
                    spacing=6,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def path_card(
        title: str,
        subtitle: str,
        bullets: list[str],
        date_text: str,
        certificate_key: str,
        icon: str | None,
    ) -> ft.Container:
        return ft.Container(
            width=path_card_width,
            height=430 if is_mobile else 386,
            border_radius=14,
            bgcolor="#0F172A",
            border=line_border(ACCENT, 0.62),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        right=-36,
                        top=-36,
                        width=118,
                        height=118,
                        border_radius=60,
                        bgcolor=ft.Colors.with_opacity(0.07, "#4BA3FF"),
                    ),
                    ft.Container(
                        left=0,
                        right=0,
                        top=0,
                        bottom=0,
                        padding=ft.Padding(28, 28, 28, 28),
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            width=44,
                                            height=44,
                                            border_radius=11,
                                            bgcolor="#163256",
                                            content=ft.Icon(icon, color="#4BA3FF", size=23),
                                            alignment=ft.Alignment(0, 0),
                                        ),
                                        ft.Container(expand=True),
                                        ft.Container(
                                            height=24,
                                            border_radius=12,
                                            padding=ft.Padding(10, 0, 10, 0),
                                            bgcolor="#102D4B",
                                            border=line_border(ACCENT, 0.55),
                                            content=ft.Text(
                                                "LEARNING PATH",
                                                size=10,
                                                color="#4BA3FF",
                                                weight=ft.FontWeight.BOLD,
                                                font_family="Courier New",
                                            ),
                                            alignment=ft.Alignment(0, 0),
                                        ),
                                    ],
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                ft.Container(height=8),
                                provider_line(),
                                ft.Text(
                                    title,
                                    size=18,
                                    color=TEXT_PRIMARY,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(subtitle, size=13, color=TEXT_SECONDARY),
                                ft.Container(
                                    height=3,
                                    border_radius=2,
                                    gradient=ft.LinearGradient(
                                        begin=ft.Alignment(-1, 0),
                                        end=ft.Alignment(1, 0),
                                        colors=["#4BA3FF", "#46E6A8"],
                                    ),
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    width=5,
                                                    height=5,
                                                    border_radius=3,
                                                    bgcolor="#4BA3FF",
                                                ),
                                                ft.Text(item, size=12, color=TEXT_SECONDARY, expand=True),
                                            ],
                                            spacing=8,
                                            vertical_alignment=ft.CrossAxisAlignment.START,
                                        )
                                        for item in bullets
                                    ],
                                    spacing=6,
                                ),
                                ft.Container(expand=True),
                                ft.Container(height=1, bgcolor=ft.Colors.with_opacity(0.75, BORDER)),
                                date_status(date_text),
                                certificate_button(certificate_key),
                            ],
                            spacing=8,
                            expand=True,
                        ),
                    ),
                ],
            ),
        )

    def course_card(
        title: str,
        date_text: str,
        certificate_key: str,
        icon: str,
        accent: str,
        tag: str = "COURSE",
    ) -> ft.Container:
        return ft.Container(
            width=course_card_width,
            height=292,
            border_radius=14,
            bgcolor="#0F172A",
            border=line_border(ACCENT, 0.46),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        right=-38,
                        top=-38,
                        width=118,
                        height=118,
                        border_radius=60,
                        bgcolor=ft.Colors.with_opacity(0.06, accent),
                    ),
                    ft.Container(
                        left=0,
                        right=0,
                        top=0,
                        bottom=0,
                        padding=ft.Padding(24, 22, 24, 22),
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            width=44,
                                            height=44,
                                            border_radius=11,
                                            bgcolor=ft.Colors.with_opacity(0.16, accent),
                                            content=ft.Icon(icon, color=accent, size=23),
                                            alignment=ft.Alignment(0, 0),
                                        ),
                                        ft.Container(expand=True),
                                        ft.Container(
                                            height=23,
                                            border_radius=12,
                                            padding=ft.Padding(10, 0, 10, 0),
                                            bgcolor=ft.Colors.with_opacity(0.13, accent),
                                            border=line_border(accent, 0.45),
                                            content=ft.Text(
                                                tag,
                                                size=10,
                                                color=accent,
                                                weight=ft.FontWeight.BOLD,
                                                font_family="Courier New",
                                            ),
                                            alignment=ft.Alignment(0, 0),
                                        ),
                                    ],
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                ft.Container(height=8),
                                provider_line(),
                                ft.Text(
                                    title,
                                    size=15,
                                    color=TEXT_PRIMARY,
                                    weight=ft.FontWeight.BOLD,
                                    max_lines=2,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                                ft.Container(
                                    height=3,
                                    border_radius=2,
                                    gradient=ft.LinearGradient(
                                        begin=ft.Alignment(-1, 0),
                                        end=ft.Alignment(1, 0),
                                        colors=["#4BA3FF", "#46E6A8"],
                                    ),
                                ),
                                ft.Container(expand=True),
                                ft.Container(height=1, bgcolor=ft.Colors.with_opacity(0.75, BORDER)),
                                date_status(date_text, compact=True),
                                certificate_button(certificate_key),
                            ],
                            spacing=10,
                            expand=True,
                        ),
                    ),
                ],
            ),
        )

    hero = ft.Column(
        controls=[
            ft.Container(
                height=28,
                border_radius=14,
                padding=ft.Padding(12, 0, 12, 0),
                bgcolor="#10223B",
                border=line_border(ACCENT, 0.55),
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.DIAMOND_ROUNDED, size=11, color="#4BA3FF"),
                        ft.Text(
                            "MathWorks Training Services",
                            size=12,
                            color="#4BA3FF",
                            font_family="Courier New",
                        ),
                    ],
                    spacing=7,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            ft.Row(
                controls=[
                    ft.Text(
                        "MATLAB",
                        size=38 if is_mobile else 50,
                        color=TEXT_PRIMARY,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Certifications",
                        size=38 if is_mobile else 50,
                        color="#4BA3FF",
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                wrap=True,
            ),
            ft.Text(
                (
                    "A verified record of completed MathWorks training - covering core programming, data visualization, matrix operations, and Simulink simulation."
                    if is_mobile
                    else "A verified record of completed MathWorks training - covering core\n"
                    "programming, data visualization, matrix operations, and Simulink\n"
                    "simulation."
                ),
                size=15,
                color=TEXT_SECONDARY,
                height=1.55,
                width=content_width if is_mobile else None,
            ),
            ft.Container(height=16),
            ft.Row(
                controls=[
                    metric_card("7", "Certificates", "total earned", 180),
                    metric_card("2", "Learning Paths", "completed", 180),
                    metric_card("100%", "Completion", "all courses", 180),
                    metric_card("2026", "Year", "all certified", 180),
                ],
                spacing=24,
                wrap=True,
                alignment=ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START,
            ),
        ],
        spacing=14,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    content = ft.Container(
        width=content_width,
        content=ft.Column(
            controls=[
                hero,
                ft.Container(height=72),
                section_label("Learning Paths"),
                ft.Row(
                    controls=[
                        path_card(
                            "Core MATLAB Skills",
                            "Comprehensive learning path - 4 courses",
                            [
                                "MATLAB Desktop Tools and Troubleshooting Scripts",
                                "Explore Data with MATLAB Plots",
                                "Make and Manipulate Matrices",
                                "Calculations with Vectors and Matrices",
                            ],
                            "25 April 2026",
                            CORE_MATLAB_SKILLS_CERTIFICATE_KEY,
                            ft.Icons.SCHOOL_ROUNDED,
                        ),
                        path_card(
                            "Visualization in MATLAB",
                            "Comprehensive learning path - 3 courses",
                            [
                                "Explore Data with MATLAB Plots",
                                "Plot Beyond the Second Dimension",
                                "How MATLAB Graphics Work",
                            ],
                            "26 April 2026",
                            VISUALIZATION_IN_MATLAB_CERTIFICATE_KEY,
                            ft.Icons.BAR_CHART_ROUNDED,
                        ),
                    ],
                    spacing=24,
                    run_spacing=24,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START,
                ),
                ft.Container(height=34),
                section_label("Individual Courses"),
                ft.Row(
                    controls=[
                        course_card(
                            "MATLAB Onramp",
                            "21 Feb 2026",
                            MATLAB_ONRAMP_CERTIFICATE_KEY,
                            ft.Icons.BOLT_ROUNDED,
                            ORANGE,
                        ),
                        course_card(
                            "Calculations with Vectors and Matrices",
                            "25 Apr 2026",
                            CALCULATIONS_WITH_VECTORS_AND_MATRICES_CERTIFICATE_KEY,
                            ft.Icons.CALCULATE_ROUNDED,
                            "#60A5FA",
                        ),
                        course_card(
                            "The Why and How of Functions",
                            "30 Apr 2026",
                            THE_WHY_AND_HOW_OF_FUNCTIONS_CERTIFICATE_KEY,
                            ft.Icons.SETTINGS_ROUNDED,
                            "#A78BFA",
                        ),
                        course_card(
                            "Simulink Onramp",
                            "30 Apr 2026",
                            SIMULINK_ONRAMP_CERTIFICATE_KEY,
                            ft.Icons.CACHED_ROUNDED,
                            TEAL,
                            "SIMULINK",
                        ),
                        course_card(
                            "Circuit Simulation Onramp",
                            "30 Apr 2026",
                            "circuit_simulation_onramp",
                            ft.Icons.ELECTRICAL_SERVICES_ROUNDED,
                            GOLD,
                            "SIMULINK",
                        ),
                    ],
                    spacing=24,
                    run_spacing=24,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START,
                ),
            ],
            spacing=28,
        ),
    )

    return ft.Column(
        expand=True,
        scroll=hidden_scroll(),
        controls=[
            ft.Container(
                bgcolor=BG,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=["#080D19", "#0A1325", "#08101E"],
                ),
                content=ft.Stack(
                    controls=[
                        *grid_background(width=int(content_width + 80), height=2200),
                        ft.Container(
                            padding=ft.Padding(0, 34 if is_mobile else 72, 0, 44 if is_mobile else 60),
                            content=ft.Row(
                                controls=[content],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.START,
                            ),
                        ),
                    ],
                ),
            ),
        ],
        spacing=0,
    )


def build_blog_legacy() -> ft.Column:
    posts = [
        {
            "title": "Understanding Big-O Notation",
            "tag": "Algorithms",
            "tag_color": ACCENT,
            "body": (
                "When analysing algorithms, Big-O notation gives us a language to "
                "express how runtime grows relative to input size. O(1) is constant, "
                "O(n) is linear, and O(n²) describes nested-loop behaviour common "
                "in naive sorting algorithms."
            ),
            "formula": "T(n) = O(n²)  →  each element compared n times",
        },
        {
            "title": "Material Cost Formula in Engineering Apps",
            "tag": "Mathematics",
            "tag_color": GOLD,
            "body": (
                "Our metallurgical module uses a summation formula to compute "
                "total material costs across n line items, each with quantity Qᵢ "
                "and unit price Pᵢ, plus a fixed overhead value."
            ),
            "formula": "Total Cost = Σ(Qᵢ × Pᵢ) + Overheads   [i = 1 … n]",
        },
        {
            "title": "Version Control with Git",
            "tag": "DevOps",
            "tag_color": ACCENT2,
            "body": (
                "Effective Git workflow in a 20-member team requires branch "
                "strategies, protected main branches, and mandatory code review "
                "before merge. Squash merges keep history clean and auditable."
            ),
            "formula": "feat/branch → PR → review → squash-merge → main",
        },
    ]

    post_widgets = []
    for post in posts:
        post_widgets.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                badge(post["tag"], post["tag_color"]),
                            ],
                        ),
                        ft.Text(
                            post["title"],
                            size=17,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT_PRIMARY,
                        ),
                        ft.Text(post["body"], size=13, color=TEXT_SECONDARY),
                        ft.Container(
                            content=ft.Text(
                                post["formula"],
                                size=12,
                                color=ACCENT,
                                font_family="Courier New",
                            ),
                            bgcolor=ft.Colors.with_opacity(0.08, ACCENT),
                            border_radius=6,
                            padding=ft.Padding(12, 8, 12, 8),
                            border=ft.Border(
                                left=ft.BorderSide(3, ACCENT),
                                top=ft.BorderSide(0, ACCENT),
                                right=ft.BorderSide(0, ACCENT),
                                bottom=ft.BorderSide(0, ACCENT),
                            ),
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.PLAY_CIRCLE_OUTLINE_ROUNDED,
                                        color=ACCENT2, size=16),
                                ft.Text("Embed video coming soon",
                                        size=12, color=TEXT_SECONDARY),
                            ],
                            spacing=6,
                        ),
                    ],
                    spacing=10,
                ),
                bgcolor=SURFACE,
                border_radius=12,
                padding=20,
                border=ft.Border(
                    left=ft.BorderSide(1, BORDER),
                    top=ft.BorderSide(1, BORDER),
                    right=ft.BorderSide(1, BORDER),
                    bottom=ft.BorderSide(1, BORDER),
                ),
            )
        )

    return ft.Column(
        controls=[
            section_title(
                "Technical Blog",
                "Confidence in Concepts — written explanations with notation",
            ),
            ft.Container(height=16),
            *post_widgets,
        ],
        spacing=12,
        scroll=hidden_scroll(),
        expand=True,
    )


def build_blog(viewport_width: float | int | None = None) -> ft.Column:
    view_width = current_view_width(viewport_width)
    is_mobile = view_width < MOBILE_BREAKPOINT
    content_width = available_width(view_width, 860, 24 if is_mobile else 72)
    horizontal_pad = 14 if is_mobile else 32
    post_pad = 16 if is_mobile else 36
    blog_bg = "#0A0F2E"
    blog_mid = "#0D1A4A"
    blog_gold = "#C9A84C"
    blog_gold_light = "#E8C87A"
    blog_white = "#F0F4FF"
    blog_muted = "#8892B0"
    blog_line = ft.Colors.with_opacity(0.25, blog_gold)

    posts = [
        {
            "category": "Algorithm",
            "category_color": "#A5B4FC",
            "category_bg": "#262A78",
            "title": "Fall Detection Algorithm - FR-007",
            "description": (
                "MineShield detects falls by analysing a rolling window of "
                "accelerometer readings. A fall is confirmed when three conditions "
                "are met simultaneously: high impact, significant change in "
                "magnitude, and sudden stillness after the impact."
            ),
            "chips": [
                "magnitude = sqrt(x^2 + y^2 + z^2)",
                "maxMagnitude > 2.5g",
                "deltaMagnitude > 2.0",
                "currentMagnitude < 1.2g",
            ],
            "details": [
                ("heading", "Core Equation - Acceleration Magnitude"),
                (
                    "text",
                    "The accelerometer returns three axis values (x, y, z) at each "
                    "reading. To detect motion regardless of device orientation, "
                    "these are combined into a single scalar magnitude.",
                ),
                ("math", "|a| = sqrt(x^2 + y^2 + z^2)"),
                (
                    "text",
                    "This is the Euclidean norm of the acceleration vector. A "
                    "device at rest with no movement reads approximately 1.0g "
                    "because of gravity. A sudden violent motion spikes this value "
                    "significantly above 1.0g.",
                ),
                ("heading", "Rolling Window"),
                (
                    "text",
                    "MineShield samples the accelerometer every 200 ms and keeps "
                    "the last 10 readings in a rolling array. From this window, "
                    "the algorithm extracts the maximum and minimum magnitudes.",
                ),
                (
                    "math",
                    "maxMagnitude = max(|a1|, |a2|, ... , |a10|)\n"
                    "minMagnitude = min(|a1|, |a2|, ... , |a10|)",
                ),
                ("heading", "Three Fall Detection Conditions"),
                (
                    "cards",
                    [
                        (
                            "Condition 1 - High Impact",
                            "maxMagnitude > 2.5g",
                            "Peak acceleration exceeds 2.5 times gravity, "
                            "indicating a sudden physical impact.",
                        ),
                        (
                            "Condition 2 - Significant Change",
                            "(max - min) > 2.0g",
                            "The spread between peak and trough rules out vibration "
                            "or normal walking.",
                        ),
                        (
                            "Condition 3 - Post-Fall Stillness",
                            "currentMagnitude < 1.2g",
                            "Immediately after impact, the device becomes stationary, "
                            "consistent with a person on the ground.",
                        ),
                        (
                            "Combined Logic",
                            "C1 AND C2 AND C3",
                            "All three must be true. Any single spike without "
                            "stillness is ignored.",
                        ),
                    ],
                ),
                ("heading", "Implementation (sensorService.js)"),
                (
                    "code",
                    """const detectFall = (currentMagnitude, timestamp) => {
  lastMagnitudes.push(currentMagnitude);
  if (lastMagnitudes.length > 10) lastMagnitudes.shift();
  if (lastMagnitudes.length < 10) return false;

  const maxMagnitude = Math.max(...lastMagnitudes);
  const minMagnitude = Math.min(...lastMagnitudes);

  const hasHighImpact = maxMagnitude > 2.5;
  const hasSignificantChange = (maxMagnitude - minMagnitude) > 2.0;
  const isStationaryAfterImpact = currentMagnitude < 1.2;

  return hasHighImpact && hasSignificantChange && isStationaryAfterImpact;
};""",
                ),
                ("heading", "10-Second SOS Escalation"),
                (
                    "text",
                    "When a fall is detected, a confirmation modal appears. If the "
                    "worker does not respond within 10 seconds, triggerSOS() sends "
                    "the worker's last known GPS location to all supervisors via "
                    "Firebase Cloud Messaging.",
                ),
                ("math", "t_escalation = t_detection + 10 000 ms"),
                (
                    "text",
                    "Tested accuracy: 92% across 50 simulated falls on physical "
                    "devices running Android 11, 12, and 13.",
                ),
            ],
        },
        {
            "category": "Sensor",
            "category_color": blog_gold_light,
            "category_bg": "#3A3218",
            "title": "Accelerometer Sensor - How It Works in MineShield",
            "description": (
                "The accelerometer is a built-in smartphone sensor that measures "
                "the rate of change of velocity along three axes. MineShield uses "
                "Expo Sensors to subscribe to this data stream and feed it into "
                "the fall detection algorithm at 5 readings per second."
            ),
            "chips": [
                "expo-sensors",
                "Accelerometer.setUpdateInterval(200)",
                "x, y, z axes",
                "FR-007",
            ],
            "details": [
                ("heading", "What an Accelerometer Measures"),
                (
                    "text",
                    "An accelerometer measures proper acceleration - the "
                    "acceleration relative to free fall - along three perpendicular "
                    "axes.",
                ),
                (
                    "bullets",
                    [
                        "x - lateral movement, left and right",
                        "y - longitudinal movement, forward and backward",
                        "z - vertical movement, up and down",
                    ],
                ),
                (
                    "text",
                    "At rest on a flat surface, a device reads approximately "
                    "(x=0, y=0, z=1.0) because gravity acts upward relative to "
                    "the sensor.",
                ),
                ("heading", "Units and Scale"),
                (
                    "math",
                    "Acceleration units: g (1g = 9.81 m/s^2)\n"
                    "Rest state: |a| ~= 1.0g\n"
                    "Normal walking: |a| ~= 1.0 - 1.5g\n"
                    "Violent fall impact: |a| > 2.5g",
                ),
                ("heading", "Sensor Subscription in MineShield"),
                (
                    "text",
                    "The sensor is started when the worker opens the app and "
                    "stopped when they leave. The update interval is set to 200 ms, "
                    "giving 5 samples per second.",
                ),
                (
                    "code",
                    """import { Accelerometer } from 'expo-sensors';

export const startFallDetection = () => {
  Accelerometer.setUpdateInterval(200); // 5 readings/sec

  subscription = Accelerometer.addListener(({ x, y, z }) => {
    const magnitude = Math.sqrt(x*x + y*y + z*z);
    const timestamp = Date.now();

    if (!fallDetected && detectFall(magnitude, timestamp)) {
      fallDetected = true;
      showFallConfirmation(); // 10-second modal
      storeSensorLog({ type: 'FALL_DETECTED', magnitude, timestamp });
    }
  });
};""",
                ),
                ("heading", "Battery Consideration"),
                (
                    "text",
                    "Per the SRS non-functional requirements, the accelerometer "
                    "runs only while the app is in the foreground. Combined with "
                    "location updates every 30 seconds, the system supports about "
                    "6-8 hours of continuous use on a standard device battery.",
                ),
            ],
        },
        {
            "category": "Sound Monitoring",
            "category_color": "#6EE7B7",
            "category_bg": "#12392E",
            "title": "Noise Level Monitoring - FR-008",
            "description": (
                "MineShield monitors ambient noise levels using the device "
                "microphone via Expo Audio. When sound exceeds the 85 dB threshold "
                "defined in the SRS, an alert is triggered and the reading is "
                "logged to the Firestore sensorLogs collection."
            ),
            "chips": [
                "threshold = 85 dB",
                "L = 20 x log10(p / p0)",
                "FR-008 - Medium priority",
                "Firestore sensorLogs",
            ],
            "details": [
                ("heading", "The Decibel Scale"),
                (
                    "text",
                    "Sound pressure level is measured in decibels, a logarithmic "
                    "scale representing the ratio of measured pressure to a "
                    "reference pressure.",
                ),
                ("math", "L = 20 x log10(p / p0)"),
                (
                    "text",
                    "Where L is the sound level in dB, p is the measured sound "
                    "pressure in Pa, and p0 is the reference pressure of 20 uPa, "
                    "the threshold of human hearing.",
                ),
                ("heading", "Why 85 dB?"),
                (
                    "text",
                    "The 85 dB threshold is based on occupational health standards. "
                    "Prolonged exposure above this level causes irreversible "
                    "hearing damage. In underground mining environments, machinery, "
                    "blasting, and ventilation fans routinely exceed this threshold.",
                ),
                (
                    "cards",
                    [
                        ("Normal conversation", "~60 dB", "Safe for unlimited exposure."),
                        (
                            "MineShield alert threshold",
                            "85 dB",
                            "SRS FR-008: alert triggered above this level.",
                        ),
                        (
                            "Mine machinery",
                            "90 - 110 dB",
                            "Common in underground operations.",
                        ),
                        ("Blasting", "> 140 dB", "Instant hearing damage risk."),
                    ],
                ),
                ("heading", "Logarithmic Nature of dB"),
                (
                    "text",
                    "Because the scale is logarithmic, every +10 dB increase "
                    "represents a 10x increase in sound intensity.",
                ),
                (
                    "math",
                    "deltaL = 10 dB -> intensity x 10\n"
                    "deltaL = 20 dB -> intensity x 100\n"
                    "deltaL = 30 dB -> intensity x 1000",
                ),
                ("heading", "SRS Requirement"),
                (
                    "text",
                    "FR-008 is classified as Medium priority and uses Firestore for "
                    "log storage. Each reading above threshold is stored in the "
                    "sensorLogs collection with the noise level, timestamp, and "
                    "user ID so supervisors can identify dangerous zones over time.",
                ),
                (
                    "code",
                    """// Noise alert log structure (Firestore: sensorLogs)
{
  logId: "auto-generated",
  userId: "worker-uid",
  type: "NOISE_THRESHOLD_EXCEEDED",
  noiseLevel: 91.4,
  timestamp: "2026-05-29T08:23:11Z",
  zoneId: "zone-B3"
}""",
                ),
            ],
        },
    ]

    def category_chip(text: str, text_color: str, bg_color: str) -> ft.Container:
        return ft.Container(
            content=ft.Text(
                text.upper(),
                size=10,
                color=text_color,
                weight=ft.FontWeight.BOLD,
            ),
            bgcolor=ft.Colors.with_opacity(0.62, bg_color),
            border_radius=4,
            padding=ft.Padding(12, 5, 12, 5),
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.with_opacity(0.36, text_color)),
                top=ft.BorderSide(1, ft.Colors.with_opacity(0.36, text_color)),
                right=ft.BorderSide(1, ft.Colors.with_opacity(0.36, text_color)),
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.36, text_color)),
            ),
        )

    def blog_chip(text: str) -> ft.Container:
        return ft.Container(
            content=ft.Text(
                text,
                size=11,
                color=blog_gold_light,
                font_family="Courier New",
            ),
            bgcolor=ft.Colors.with_opacity(0.08, blog_gold),
            border_radius=4,
            padding=ft.Padding(10, 4, 10, 4),
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.with_opacity(0.20, blog_gold)),
                top=ft.BorderSide(1, ft.Colors.with_opacity(0.20, blog_gold)),
                right=ft.BorderSide(1, ft.Colors.with_opacity(0.20, blog_gold)),
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.20, blog_gold)),
            ),
        )

    def body_heading(text: str) -> ft.Text:
        return ft.Text(
            text,
            size=16,
            color=blog_white,
            weight=ft.FontWeight.BOLD,
            font_family="Georgia",
        )

    def body_text(text: str) -> ft.Text:
        return ft.Text(text, size=13, color=blog_muted, height=1.75)

    def bullet_item(text: str) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Text(">", size=13, color=blog_gold, weight=ft.FontWeight.BOLD),
                ft.Text(text, size=13, color=blog_muted, expand=True, height=1.55),
            ],
            spacing=8,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    def math_block(text: str) -> ft.Container:
        return ft.Container(
            content=ft.Text(
                text,
                size=14,
                color=blog_gold_light,
                font_family="Courier New",
                height=1.65,
            ),
            bgcolor=ft.Colors.with_opacity(0.06, blog_gold),
            border_radius=8,
            padding=ft.Padding(18, 12, 18, 12),
            border=ft.Border(left=ft.BorderSide(3, blog_gold)),
        )

    def code_block(text: str) -> ft.Container:
        return ft.Container(
            content=ft.Text(
                text,
                size=10 if is_mobile else 12,
                color=blog_gold_light,
                font_family="Courier New",
                selectable=True,
            ),
            bgcolor=ft.Colors.with_opacity(0.40, "#000000"),
            border_radius=8,
            padding=ft.Padding(18, 14, 18, 14),
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.with_opacity(0.12, blog_gold)),
                top=ft.BorderSide(1, ft.Colors.with_opacity(0.12, blog_gold)),
                right=ft.BorderSide(1, ft.Colors.with_opacity(0.12, blog_gold)),
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.12, blog_gold)),
            ),
        )

    def condition_card(label: str, value: str, description: str) -> ft.Container:
        return ft.Container(
            width=min(354, content_width - (post_pad * 2)),
            content=ft.Column(
                controls=[
                    ft.Text(
                        label.upper(),
                        size=10,
                        color=blog_gold,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        value,
                        size=13,
                        color=blog_white,
                        font_family="Courier New",
                    ),
                    ft.Text(description, size=12, color=blog_muted, height=1.45),
                ],
                spacing=5,
            ),
            bgcolor=ft.Colors.with_opacity(0.30, "#000000"),
            border_radius=8,
            padding=ft.Padding(15, 13, 15, 13),
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.with_opacity(0.15, blog_gold)),
                top=ft.BorderSide(1, ft.Colors.with_opacity(0.15, blog_gold)),
                right=ft.BorderSide(1, ft.Colors.with_opacity(0.15, blog_gold)),
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.15, blog_gold)),
            ),
        )

    def video_section() -> ft.Container:
        video_ready = fv is not None
        if video_ready:
            async def start_video(e: ft.ControlEvent) -> None:
                await video_player.play()
                play_overlay.visible = False
                e.page.update()

            def show_play_overlay(e: ft.ControlEvent) -> None:
                play_overlay.visible = True
                e.page.update()

            video_player = fv.Video(
                playlist=[fv.VideoMedia(BLOG_VIDEO_RESOURCE)],
                title="Video Contribution",
                fit=ft.BoxFit.CONTAIN,
                fill_color="#050817",
                autoplay=False,
                muted=False,
                volume=85,
                controls=fv.MaterialVideoControls(
                    visible_on_mount=True,
                    display_seek_bar=True,
                    button_bar_button_color=blog_white,
                    seek_bar_color=ft.Colors.with_opacity(0.40, blog_gold),
                    seek_bar_position_color=blog_gold,
                    seek_bar_thumb_color=blog_gold,
                    backdrop_color=ft.Colors.with_opacity(0.40, "#000000"),
                ),
                on_complete=show_play_overlay,
                expand=True,
            )
            play_overlay = ft.Container(
                left=0,
                top=0,
                right=0,
                bottom=0,
                ink=True,
                on_click=start_video,
                alignment=ft.Alignment(0, 0),
                bgcolor=ft.Colors.with_opacity(0.30, "#000000"),
                content=ft.Column(
                    controls=[
                        ft.Container(
                            width=72,
                            height=72,
                            border_radius=36,
                            alignment=ft.Alignment(0, 0),
                            bgcolor=ft.Colors.with_opacity(0.90, blog_gold),
                            content=ft.Icon(
                                ft.Icons.PLAY_ARROW_ROUNDED,
                                size=44,
                                color="#050817",
                            ),
                        ),
                        ft.Text(
                            "Click to play",
                            size=13,
                            color=blog_white,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                    spacing=12,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            )
            video_content = ft.Stack(
                controls=[video_player, play_overlay],
                fit=ft.StackFit.EXPAND,
                expand=True,
            )
        else:
            video_content = ft.Column(
                controls=[
                    ft.Container(
                        width=58,
                        height=58,
                        border_radius=29,
                        alignment=ft.Alignment(0, 0),
                        bgcolor=ft.Colors.with_opacity(0.14, blog_gold),
                        border=ft.Border(
                            left=ft.BorderSide(1, blog_line),
                            top=ft.BorderSide(1, blog_line),
                            right=ft.BorderSide(1, blog_line),
                            bottom=ft.BorderSide(1, blog_line),
                        ),
                        content=ft.Icon(
                            ft.Icons.PLAY_ARROW_ROUNDED,
                            size=32,
                            color=blog_gold,
                        ),
                    ),
                    ft.Text(
                        "Video player ready",
                        size=17,
                        color=blog_white,
                        weight=ft.FontWeight.BOLD,
                        font_family="Georgia",
                    ),
                    ft.Text(
                        "Install project dependencies and keep the MP4 in the "
                        "portfolio folder as a served asset to load the embedded "
                        "recording.",
                        size=12,
                        color=blog_muted,
                        text_align=ft.TextAlign.CENTER,
                        width=420,
                        height=1.55,
                    ),
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )

        return ft.Container(
            padding=ft.Padding(0, 24 if is_mobile else 34, 0, 30 if is_mobile else 38),
            border=ft.Border(bottom=ft.BorderSide(1, blog_line)),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            category_chip("Video", blog_gold_light, "#3A3218"),
                            blog_chip("Video Contribution"),
                        ],
                        spacing=8,
                        wrap=True,
                    ),
                    ft.Text(
                        "Video Contribution",
                        size=24 if is_mobile else 26,
                        weight=ft.FontWeight.BOLD,
                        color=blog_white,
                        font_family="Georgia",
                    ),
                    ft.Text(
                        "The recorded contribution is embedded with the blog notes so "
                        "the written concepts and video walkthrough stay together.",
                        size=13,
                        color=blog_muted,
                        height=1.6,
                    ),
                    ft.Container(
                        height=220 if is_mobile else 420,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        border_radius=12,
                        bgcolor="#050817",
                        border=ft.Border(
                            left=ft.BorderSide(1, ft.Colors.with_opacity(0.30, blog_gold)),
                            top=ft.BorderSide(1, ft.Colors.with_opacity(0.30, blog_gold)),
                            right=ft.BorderSide(1, ft.Colors.with_opacity(0.30, blog_gold)),
                            bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.30, blog_gold)),
                        ),
                        shadow=ft.BoxShadow(
                            blur_radius=28,
                            color=ft.Colors.with_opacity(0.24, "#000000"),
                        ),
                        content=video_content,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(
                                "Embedded MP4",
                                size=11,
                                color=blog_muted,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Container(width=5, height=5, border_radius=3, bgcolor=blog_line),
                            ft.Text(
                                BLOG_VIDEO_FILE,
                                size=11,
                                color=blog_gold_light,
                                font_family="Courier New",
                            ),
                        ],
                        spacing=8,
                        wrap=True,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                spacing=14,
            ),
        )

    def expanded_body(details: list[tuple[str, object]]) -> ft.Container:
        controls: list[ft.Control] = []
        for kind, value in details:
            if kind == "heading":
                controls.append(body_heading(value))
            elif kind == "text":
                controls.append(body_text(value))
            elif kind == "math":
                controls.append(math_block(value))
            elif kind == "code":
                controls.append(code_block(value))
            elif kind == "bullets":
                controls.append(
                    ft.Column(
                        controls=[bullet_item(item) for item in value],
                        spacing=4,
                    )
                )
            elif kind == "cards":
                controls.append(
                    ft.Row(
                        controls=[
                            condition_card(label, card_value, description)
                            for label, card_value, description in value
                        ],
                        spacing=12,
                        run_spacing=12,
                        wrap=True,
                    )
                )
        return ft.Container(
            visible=False,
            margin=ft.Margin(0, 8, 0, 0),
            padding=ft.Padding(16, 16, 16, 16) if is_mobile else ft.Padding(28, 24, 28, 24),
            bgcolor=ft.Colors.with_opacity(0.50, blog_mid),
            border_radius=12,
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.with_opacity(0.18, blog_gold)),
                top=ft.BorderSide(1, ft.Colors.with_opacity(0.18, blog_gold)),
                right=ft.BorderSide(1, ft.Colors.with_opacity(0.18, blog_gold)),
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.18, blog_gold)),
            ),
            content=ft.Column(controls=controls, spacing=12),
        )

    body_controls: list[ft.Container] = []
    toggle_labels: list[ft.Text] = []

    def toggle_post(index: int):
        def handle_click(e: ft.ControlEvent) -> None:
            is_open = body_controls[index].visible
            for body, label in zip(body_controls, toggle_labels):
                body.visible = False
                label.value = "Read more"
            if not is_open:
                body_controls[index].visible = True
                toggle_labels[index].value = "Collapse"
            e.page.update()

        return handle_click

    post_widgets: list[ft.Control] = []
    for index, post in enumerate(posts):
        post_body = expanded_body(post["details"])
        toggle_label = ft.Text(
            "Read more",
            size=11,
            color=blog_muted,
            weight=ft.FontWeight.BOLD,
        )
        body_controls.append(post_body)
        toggle_labels.append(toggle_label)
        click_handler = toggle_post(index)

        post_widgets.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        category_chip(
                            post["category"],
                            post["category_color"],
                            post["category_bg"],
                        ),
                        ft.Container(
                            content=ft.Text(
                                post["title"],
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=blog_white,
                                font_family="Georgia",
                            ),
                            ink=True,
                            on_click=click_handler,
                        ),
                        ft.Text(
                            post["description"],
                            size=13,
                            color=blog_muted,
                            height=1.75,
                        ),
                        ft.Row(
                            controls=[blog_chip(chip) for chip in post["chips"]],
                            spacing=7,
                            run_spacing=7,
                            wrap=True,
                        ),
                        ft.Container(
                            content=toggle_label,
                            ink=True,
                            on_click=click_handler,
                            padding=ft.Padding(14, 6, 14, 6),
                            border_radius=6,
                            border=ft.Border(
                                left=ft.BorderSide(1, blog_line),
                                top=ft.BorderSide(1, blog_line),
                                right=ft.BorderSide(1, blog_line),
                                bottom=ft.BorderSide(1, blog_line),
                            ),
                        ),
                        post_body,
                    ],
                    spacing=14,
                ),
                padding=ft.Padding(0, post_pad, 0, post_pad),
                border=(
                    ft.Border(
                        bottom=ft.BorderSide(
                            1,
                            ft.Colors.with_opacity(0.06, "#FFFFFF"),
                        )
                    )
                    if index < len(posts) - 1
                    else None
                ),
            )
        )

    footer = ft.Container(
        alignment=ft.Alignment(0, 0),
        padding=ft.Padding(0, 28, 0, 50),
        content=ft.Container(
            width=min(360, content_width),
            padding=ft.Padding(0, 28, 0, 0),
            border=ft.Border(top=ft.BorderSide(1, blog_line)),
            content=ft.Column(
                controls=[
                    ft.Text(
                        "MineShield - Group 16 - Computer Programming I",
                        size=12,
                        color=blog_muted,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "Andre Cavota - Documentation Lead - Semester 1, 2026",
                        size=12,
                        color=blog_muted,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    content = ft.Container(
        width=content_width,
        padding=ft.Padding(horizontal_pad, 0, horizontal_pad, 0),
        content=ft.Column(
            controls=[
                ft.Container(
                    padding=ft.Padding(0, 56, 0, 40),
                    border=ft.Border(bottom=ft.BorderSide(1, blog_line)),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Technical Blog",
                                size=34 if is_mobile else 42,
                                weight=ft.FontWeight.BOLD,
                                color=blog_white,
                                font_family="Georgia",
                            ),
                            ft.Text(
                                "Confidence in Concepts - written explanations with notation",
                                size=14,
                                color=blog_muted,
                                italic=True,
                            ),
                        ],
                        spacing=8,
                    ),
                ),
                video_section(),
                *post_widgets,
                footer,
            ],
            spacing=0,
        ),
    )

    return ft.Column(
        controls=[
            ft.Container(
                expand=True,
                bgcolor=blog_bg,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=[blog_bg, blog_mid, blog_bg],
                ),
                content=ft.Row(
                    controls=[content],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            ),
        ],
        spacing=0,
        scroll=hidden_scroll(),
        expand=True,
    )


def build_github_legacy() -> ft.Column:
    commits = [
        ("#a3f2c1", "feat: add cost-calc module for metallurgical input form",
         "main", "2 days ago"),
        ("#b19de0", "fix: resolve ft.Colors deprecation in nav_bar",
         "main", "4 days ago"),
        ("#c84f12", "docs: update README with deployment steps",
         "main", "1 week ago"),
        ("#d20a9f", "refactor: extract reusable card() widget",
         "main", "1 week ago"),
        ("#e73c44", "test: add unit tests for overhead calculation",
         "main", "2 weeks ago"),
    ]

    prs = [
        ("PR #14", "Add DataTable results view", "Merged", "#10B981"),
        ("PR #11", "Refactor routing to ft.run() pattern", "Merged", "#10B981"),
        ("PR #08", "Reviewed: Mining module UI", "Reviewed", GOLD),
    ]

    commit_widgets = [
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.COMMIT, color=ACCENT, size=16),
                    ft.Text(
                        sha, size=11, color=ACCENT,
                        font_family="Courier New", width=80,
                    ),
                    ft.Text(msg, size=13, color=TEXT_PRIMARY, expand=True),
                    ft.Text(branch, size=11, color=ACCENT2),
                    ft.Text(age, size=11, color=TEXT_SECONDARY),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=SURFACE2,
            border_radius=8,
            padding=ft.Padding(14, 10, 14, 10),
        )
        for sha, msg, branch, age in commits
    ]

    pr_widgets = [
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.MERGE_TYPE_ROUNDED, color=col, size=16),
                    ft.Text(num, size=12, color=col,
                            weight=ft.FontWeight.BOLD, width=60),
                    ft.Text(title, size=13, color=TEXT_PRIMARY, expand=True),
                    badge(status, col),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=SURFACE2,
            border_radius=8,
            padding=ft.Padding(14, 10, 14, 10),
        )
        for num, title, status, col in prs
    ]

    impact_text = (
        "My primary contributions centred on the Metallurgical module. I built "
        "the material-cost input form and wired it to the Σ(Qᵢ × Pᵢ) + Overheads "
        "backend function. I also refactored shared UI helpers (card(), badge()) "
        "that were adopted across the Civil and Mining modules, reducing duplicated "
        "layout code by ~40%. Additionally I resolved a critical ft.Colors "
        "deprecation that blocked the CI pipeline for the full team."
    )

    return ft.Column(
        controls=[
            section_title(
                "GitHub Evidence",
                "Commit history · Pull requests · Impact summary",
            ),
            ft.Container(height=16),
            card(
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.HISTORY_ROUNDED,
                                        color=ACCENT, size=18),
                                ft.Text("Commit History", size=15,
                                        weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                            ],
                            spacing=8,
                        ),
                        ft.Container(height=8),
                        *commit_widgets,
                    ],
                    spacing=8,
                ),
            ),
            ft.Container(height=8),
            card(
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.MERGE_ROUNDED,
                                        color=ACCENT2, size=18),
                                ft.Text("Pull Request Logs", size=15,
                                        weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                            ],
                            spacing=8,
                        ),
                        ft.Container(height=8),
                        *pr_widgets,
                    ],
                    spacing=8,
                ),
            ),
            ft.Container(height=8),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE_ROUNDED,
                                        color=GOLD, size=18),
                                ft.Text("Impact Summary", size=15,
                                        weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                            ],
                            spacing=8,
                        ),
                        ft.Container(height=8),
                        ft.Text(impact_text, size=13, color=TEXT_SECONDARY),
                    ],
                    spacing=4,
                ),
                bgcolor=SURFACE,
                border_radius=12,
                padding=20,
                border=ft.Border(
                    left=ft.BorderSide(3, GOLD),
                    top=ft.BorderSide(1, BORDER),
                    right=ft.BorderSide(1, BORDER),
                    bottom=ft.BorderSide(1, BORDER),
                ),
            ),
        ],
        spacing=8,
        scroll=hidden_scroll(),
        expand=True,
    )


def build_github(viewport_width: float | int | None = None) -> ft.Column:
    view_width = current_view_width(viewport_width)
    is_mobile = view_width < MOBILE_BREAKPOINT
    content_width = available_width(view_width, 900, 32 if is_mobile else 72)

    commits = [
        (
            "a3f2d1",
            "docs: add complete traceability matrix FR-001 to FR-015",
            "Mapped all functional requirements to source files and team members in TRACEABILITY_MATRIX.md.",
        ),
        (
            "b82c09",
            "docs: create FINAL_SUBMISSION.md executive summary",
            "Compiled team reflections and project outcomes for the final submission package.",
        ),
        (
            "c14e77",
            "feat: add documentGenerator.js utility",
            "Utility for programmatic document generation and report exporting.",
        ),
        (
            "d99a4f",
            "docs: PRESENTATION_SLIDES.md and SRS_COMPLIANCE.md",
            "Final presentation structure and SRS compliance verification document.",
        ),
        (
            "e05b12",
            "feat: reportExporter.js for data export utility",
            "Implemented report export logic for analytics and hazard data.",
        ),
    ]

    prs = [
        (
            "Merged",
            "PR #34 - Phase 3 Documentation Package",
            "Merged 6 assigned files into develop. Reviewed by Simon Shitana.",
            TEAL,
        ),
        (
            "Merged",
            "PR #21 - Phase 2 Implementation Plan Docs",
            "Contributed analytics group documentation and Phase 2 plan authoring.",
            TEAL,
        ),
        (
            "Merged",
            "PR #08 - SRS Document Phase 1",
            "Initial SRS document covering all 6 sections and 15 functional requirements.",
            TEAL,
        ),
        (
            "Reviewed",
            "PR #31 - Analytics Dashboard Screen",
            "Reviewed implementation against FR-013 documentation requirements.",
            GOLD,
        ),
        (
            "Reviewed",
            "PR #29 - Architecture and Deployment Docs",
            "Cross-checked ARCHITECTURE.md against the SRS system description.",
            GOLD,
        ),
    ]

    GH_BG = "#0A0F2E"
    GH_NAVY_LIGHT = "#162260"
    GH_GOLD = "#C9A84C"
    GH_GOLD_LIGHT = "#E8C87A"
    GH_TEXT = "#F0F4FF"
    GH_MUTED = "#8892B0"
    GH_LINE = ft.Colors.with_opacity(0.25, GH_GOLD)
    GH_CARD = ft.Colors.with_opacity(0.45, GH_NAVY_LIGHT)
    GH_CARD_BORDER = ft.Colors.with_opacity(0.24, GH_GOLD)

    def soft_border(color: str = GH_CARD_BORDER, left_width: int = 1) -> ft.Border:
        return ft.Border(
            left=ft.BorderSide(left_width, color),
            top=ft.BorderSide(1, color),
            right=ft.BorderSide(1, color),
            bottom=ft.BorderSide(1, color),
        )

    def icon_box(icon: str) -> ft.Container:
        return ft.Container(
            width=30,
            height=30,
            border_radius=6,
            alignment=ft.Alignment(0, 0),
            bgcolor=ft.Colors.with_opacity(0.12, GH_GOLD),
            border=soft_border(ft.Colors.with_opacity(0.55, GH_GOLD)),
            content=ft.Icon(icon, size=16, color=GH_GOLD),
        )

    def evidence_card(title: str, icon: str, controls: list[ft.Control]) -> ft.Container:
        return ft.Container(
            col={"xs": 12, "md": 6},
            padding=18 if is_mobile else 24,
            border_radius=12,
            bgcolor=GH_CARD,
            border=soft_border(),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            icon_box(icon),
                            ft.Text(
                                title,
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=GH_TEXT,
                                font_family="Georgia",
                            ),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Container(height=6),
                    *controls,
                ],
                spacing=0,
            ),
        )

    def commit_item(sha: str, title: str, detail: str) -> ft.Container:
        return ft.Container(
            padding=ft.Padding(0, 12, 0, 12),
            border=ft.Border(
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.07, GH_TEXT))
            ),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            sha,
                            size=11,
                            color=GH_GOLD_LIGHT,
                            font_family="Courier New",
                        ),
                        bgcolor=ft.Colors.with_opacity(0.10, GH_GOLD),
                        border_radius=4,
                        padding=ft.Padding(8, 3, 8, 3),
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                title,
                                size=13,
                                color=GH_TEXT,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(
                                detail,
                                size=12,
                                color=GH_MUTED,
                                height=1.45,
                            ),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        )

    def status_pill(status: str, color: str) -> ft.Container:
        return ft.Container(
            content=ft.Text(
                status.upper(),
                size=10,
                color=color,
                weight=ft.FontWeight.BOLD,
            ),
            border_radius=18,
            padding=ft.Padding(9, 4, 9, 4),
            bgcolor=ft.Colors.with_opacity(0.11, color),
            border=soft_border(ft.Colors.with_opacity(0.32, color)),
        )

    def pr_item(status: str, title: str, detail: str, color: str) -> ft.Container:
        return ft.Container(
            padding=ft.Padding(0, 12, 0, 12),
            border=ft.Border(
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.07, GH_TEXT))
            ),
            content=ft.Row(
                controls=[
                    status_pill(status, color),
                    ft.Column(
                        controls=[
                            ft.Text(
                                title,
                                size=13,
                                color=GH_TEXT,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(detail, size=12, color=GH_MUTED, height=1.45),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        )

    def stat(num: str, label: str) -> ft.Container:
        return ft.Container(
            col={"xs": 6, "sm": 3},
            content=ft.Column(
                controls=[
                    ft.Text(
                        num,
                        size=34,
                        weight=ft.FontWeight.BOLD,
                        color=GH_GOLD,
                        font_family="Georgia",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        label.upper(),
                        size=11,
                        color=GH_MUTED,
                        weight=ft.FontWeight.W_600,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                spacing=3,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    commit_widgets = [commit_item(sha, title, detail) for sha, title, detail in commits]
    pr_widgets = [pr_item(status, title, detail, color) for status, title, detail, color in prs]

    return ft.Column(
        controls=[
            ft.Container(
                expand=True,
                bgcolor=GH_BG,
                padding=ft.Padding(16 if is_mobile else 24, 34 if is_mobile else 54, 16 if is_mobile else 24, 42 if is_mobile else 52),
                alignment=ft.Alignment(0, -1),
                content=ft.Column(
                    controls=[
                        ft.Container(
                            width=content_width,
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(
                                            "Computer Programming I  -  Group 16  -  Web Portfolio 2026",
                                            size=11,
                                            color=GH_GOLD_LIGHT,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        border_radius=40,
                                        padding=ft.Padding(20, 7, 20, 7),
                                        bgcolor=ft.Colors.with_opacity(0.08, GH_GOLD),
                                        border=soft_border(ft.Colors.with_opacity(0.55, GH_GOLD_LIGHT)),
                                    ),
                                    ft.Text(
                                        spans=[
                                            ft.TextSpan("Andre "),
                                            ft.TextSpan("Cavota", style=ft.TextStyle(color=GH_GOLD)),
                                        ],
                                        size=42 if is_mobile else 58,
                                        weight=ft.FontWeight.BOLD,
                                        color=GH_TEXT,
                                        font_family="Georgia",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "Documentation Lead - MineShield: Smart Mine Safety and Monitoring System",
                                        size=16,
                                        color=GH_MUTED,
                                        text_align=ft.TextAlign.CENTER,
                                        width=min(600, content_width),
                                        height=28,
                                    ),
                                    ft.Container(
                                        width=68,
                                        height=2,
                                        border_radius=2,
                                        gradient=ft.LinearGradient(
                                            begin=ft.Alignment(-1, 0),
                                            end=ft.Alignment(1, 0),
                                            colors=[
                                                ft.Colors.TRANSPARENT,
                                                GH_GOLD,
                                                ft.Colors.TRANSPARENT,
                                            ],
                                        ),
                                    ),
                                ],
                                spacing=18,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                        ft.ResponsiveRow(
                            width=min(700, content_width),
                            columns=12,
                            controls=[
                                stat("3", "Phases"),
                                stat("6", "Files Assigned"),
                                stat("15", "FRs Traced"),
                                stat("15%", "CA Weight"),
                            ],
                            spacing=14,
                            run_spacing=14,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Divider(height=44, color=GH_LINE),
                        ft.Container(
                            width=content_width,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "GitHub Evidence",
                                        size=38,
                                        weight=ft.FontWeight.BOLD,
                                        color=GH_TEXT,
                                        font_family="Georgia",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "Individual contribution verification through commit history and pull request logs for the MineShield repository.",
                                        size=14,
                                        color=GH_MUTED,
                                        text_align=ft.TextAlign.CENTER,
                                        width=min(560, content_width),
                                        height=48,
                                    ),
                                ],
                                spacing=9,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                        ft.ResponsiveRow(
                            width=content_width,
                            columns=12,
                            controls=[
                                evidence_card(
                                    "Commit History",
                                    ft.Icons.HISTORY_ROUNDED,
                                    commit_widgets,
                                ),
                                evidence_card(
                                    "Pull Request Log",
                                    ft.Icons.MERGE_ROUNDED,
                                    pr_widgets,
                                ),
                            ],
                            spacing=20,
                            run_spacing=20,
                        ),
                        ft.Container(
                            width=content_width,
                            content=ft.Column(
                                controls=[
                                    ft.Divider(height=34, color=GH_LINE),
                                    ft.Text(
                                        "MineShield  -  Group 16  -  Computer Programming I",
                                        size=12,
                                        color=GH_MUTED,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "Submitted: Sunday, May 31, 2026  -  Web Portfolio contributes 15% to overall CA",
                                        size=12,
                                        color=GH_MUTED,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                                spacing=4,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                    ],
                    spacing=28,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
        ],
        spacing=0,
        scroll=hidden_scroll(),
        expand=True,
    )


def build_marks() -> ft.Column:
    categories = [
        ("Flet Implementation", 30, 26, ACCENT),
        ("GitHub Evidence",     25, 22, ACCENT2),
        ("Blog & Video",        25, 23, GOLD),
        ("MATLAB Courses",      20, 20, "#10B981"),
    ]

    total_marks  = sum(m for _, m, _, _ in categories)
    earned_marks = sum(e for _, _, e, _ in categories)
    pct = int((earned_marks / total_marks) * 100)

    bar_items = []
    for name, out_of, earned, col in categories:
        ratio = earned / out_of
        bar_items.append(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(name, size=13, color=TEXT_PRIMARY, expand=True),
                            ft.Text(
                                f"{earned} / {out_of}",
                                size=13,
                                color=col,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                    ft.ProgressBar(value=ratio, bgcolor=SURFACE2, color=col),
                ],
                spacing=6,
            )
        )

    summary = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    f"{earned_marks}/{total_marks}",
                    size=48,
                    weight=ft.FontWeight.BOLD,
                    color=ACCENT,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    f"{pct}%  ·  15% of total CA",
                    size=14,
                    color=TEXT_SECONDARY,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
        ),
        alignment=ft.Alignment(0, 0),
        padding=30,
        bgcolor=SURFACE,
        border_radius=16,
        border=ft.Border(
            left=ft.BorderSide(2, ACCENT),
            top=ft.BorderSide(1, BORDER),
            right=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
        ),
    )

    return ft.Column(
        controls=[
            section_title("Marks Breakdown", "CA Weighting — 15% of overall grade"),
            ft.Container(height=16),
            summary,
            ft.Container(height=12),
            card(
                ft.Column(controls=bar_items, spacing=16),
            ),
        ],
        spacing=8,
        scroll=hidden_scroll(),
        expand=True,
    )


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def build_home() -> ft.Column:
    def floating_icon(icon: str, color: str, left: int, top: int) -> ft.Container:
        return ft.Container(
            left=left,
            top=top,
            width=76,
            height=76,
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.16, TEXT_PRIMARY),
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.with_opacity(0.18, TEXT_PRIMARY)),
                top=ft.BorderSide(1, ft.Colors.with_opacity(0.18, TEXT_PRIMARY)),
                right=ft.BorderSide(1, ft.Colors.with_opacity(0.18, TEXT_PRIMARY)),
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.18, TEXT_PRIMARY)),
            ),
            content=ft.Icon(icon, color=color, size=40),
            alignment=ft.Alignment(0, 0),
        )

    code_window = ft.Container(
        left=190,
        top=92,
        width=265,
        height=226,
        border_radius=8,
        bgcolor=ft.Colors.with_opacity(0.17, TEXT_PRIMARY),
        border=ft.Border(
            left=ft.BorderSide(1, ft.Colors.with_opacity(0.26, TEXT_PRIMARY)),
            top=ft.BorderSide(1, ft.Colors.with_opacity(0.26, TEXT_PRIMARY)),
            right=ft.BorderSide(1, ft.Colors.with_opacity(0.26, TEXT_PRIMARY)),
            bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.26, TEXT_PRIMARY)),
        ),
        content=ft.Column(
            controls=[
                ft.Container(
                    height=36,
                    padding=ft.Padding(18, 0, 0, 0),
                    border=ft.Border(
                        bottom=ft.BorderSide(
                            1, ft.Colors.with_opacity(0.22, TEXT_PRIMARY)
                        )
                    ),
                    content=ft.Row(
                        controls=[
                            ft.Container(width=10, height=10, border_radius=5, bgcolor="#D8DEE9"),
                            ft.Container(width=10, height=10, border_radius=5, bgcolor="#C7D2FE"),
                            ft.Container(width=10, height=10, border_radius=5, bgcolor="#94A3B8"),
                        ],
                        spacing=9,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "</>",
                                size=68,
                                weight=ft.FontWeight.BOLD,
                                color=ACCENT,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(
                                width=210,
                                height=8,
                                border_radius=4,
                                bgcolor=ft.Colors.with_opacity(0.25, TEXT_PRIMARY),
                            ),
                            ft.Container(
                                width=118,
                                height=8,
                                border_radius=4,
                                bgcolor=ft.Colors.with_opacity(0.10, TEXT_PRIMARY),
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=12,
                    ),
                ),
            ],
            spacing=0,
        ),
    )

    visual = ft.Container(
        expand=True,
        height=350,
        gradient=ft.RadialGradient(
            center=ft.Alignment(0.42, -0.05),
            radius=1.05,
            colors=[
                ft.Colors.with_opacity(0.45, ACCENT),
                ft.Colors.with_opacity(0.10, ACCENT),
                ft.Colors.TRANSPARENT,
            ],
        ),
        content=ft.Stack(
            controls=[
                floating_icon(ft.Icons.AUTO_GRAPH_ROUNDED, ORANGE, 95, 38),
                floating_icon(ft.Icons.CODE_ROUNDED, TEXT_PRIMARY, 470, 52),
                floating_icon(ft.Icons.TERMINAL_ROUNDED, ACCENT, 445, 282),
                code_window,
            ],
            width=570,
            height=350,
        ),
    )

    hero = ft.Container(
        height=430,
        border_radius=10,
        padding=ft.Padding(34, 32, 34, 32),
        bgcolor=ft.Colors.with_opacity(0.50, SURFACE),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[
                ft.Colors.with_opacity(0.86, "#06111F"),
                ft.Colors.with_opacity(0.70, SURFACE),
                ft.Colors.with_opacity(0.48, "#071B35"),
            ],
        ),
        border=ft.Border(
            left=ft.BorderSide(1, ft.Colors.with_opacity(0.72, BORDER)),
            top=ft.BorderSide(1, ft.Colors.with_opacity(0.72, BORDER)),
            right=ft.BorderSide(1, ft.Colors.with_opacity(0.72, BORDER)),
            bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.72, BORDER)),
        ),
        content=ft.Row(
            controls=[
                ft.Container(
                    width=760,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                width=118,
                                height=38,
                                border_radius=20,
                                padding=ft.Padding(15, 0, 13, 0),
                                bgcolor=ft.Colors.with_opacity(0.10, TEXT_PRIMARY),
                                border=ft.Border(
                                    left=ft.BorderSide(1, ft.Colors.with_opacity(0.10, TEXT_PRIMARY)),
                                    top=ft.BorderSide(1, ft.Colors.with_opacity(0.10, TEXT_PRIMARY)),
                                    right=ft.BorderSide(1, ft.Colors.with_opacity(0.10, TEXT_PRIMARY)),
                                    bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.10, TEXT_PRIMARY)),
                                ),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "Welcome",
                                            size=14,
                                            color=ACCENT,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Icon(
                                            ft.Icons.WAVING_HAND_ROUNDED,
                                            size=15,
                                            color=GOLD,
                                        ),
                                    ],
                                    spacing=6,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            ),
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        "Welcome to My",
                                        size=48,
                                        weight=ft.FontWeight.BOLD,
                                        color=TEXT_PRIMARY,
                                    ),
                                    ft.Text(
                                        "Web Portfolio",
                                        size=48,
                                        weight=ft.FontWeight.BOLD,
                                        color=ACCENT,
                                    ),
                                ],
                                spacing=12,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Text(
                                "Showcasing my technical achievements, learning journey,\n"
                                "and contributions across multiple platforms.",
                                size=16,
                                color=TEXT_SECONDARY,
                                height=1.5,
                            ),
                            ft.Row(
                                controls=[
                                    ft.Container(width=48, height=2, bgcolor=ACCENT),
                                    ft.Container(
                                        width=512,
                                        height=2,
                                        bgcolor=ft.Colors.with_opacity(0.36, BORDER),
                                    ),
                                ],
                                spacing=0,
                            ),
                        ],
                        spacing=24,
                    ),
                ),
                visual,
            ],
            spacing=24,
            wrap=True,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    def feature_card(
        title: str,
        description: str,
        action: str | None,
        icon: str | None,
        color: str,
        surface: str,
        target_url: str | ft.Url | None = None,
        action_icon: str | None = ft.Icons.ARROW_FORWARD_ROUNDED,
    ) -> ft.Container:
        is_link = bool(target_url)
        action_controls: list[ft.Control] = []
        if action:
            action_controls.append(
                ft.Text(
                    action,
                    size=13,
                    color=color,
                    weight=ft.FontWeight.BOLD,
                )
            )
        if action and action_icon:
            action_controls.append(ft.Icon(action_icon, color=color, size=16))
        action_content = (
            ft.Row(
                controls=action_controls,
                spacing=6,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
            if action_controls
            else None
        )
        if action_content and is_link:
            action_content = ft.TextButton(
                content=action_content,
                height=32,
                url=str(target_url),
                tooltip=f"Open {title}",
                style=ft.ButtonStyle(
                    padding=ft.Padding(0, 0, 0, 0),
                    shape=ft.RoundedRectangleBorder(radius=6),
                    overlay_color=ft.Colors.with_opacity(0.12, color),
                    mouse_cursor=ft.MouseCursor.CLICK,
                ),
            )
        feature = ft.Container(
            width=209,
            height=187,
            border_radius=11,
            padding=ft.Padding(20, 17, 20, 17),
            bgcolor=surface,
            ink=False,
            border=ft.Border(
                left=ft.BorderSide(1, ft.Colors.with_opacity(0.42, color)),
                top=ft.BorderSide(1, ft.Colors.with_opacity(0.42, color)),
                right=ft.BorderSide(1, ft.Colors.with_opacity(0.42, color)),
                bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.42, color)),
            ),
            content=ft.Column(
                controls=[
                    *(
                        [
                            ft.Container(
                                width=42,
                                height=42,
                                border_radius=9,
                                bgcolor=ft.Colors.with_opacity(0.16, color),
                                padding=ft.Padding(0, 0, 0, 4),
                                content=ft.Icon(icon, color=color, size=23),
                                alignment=ft.Alignment(0, -0.22),
                            )
                        ]
                        if icon
                        else []
                    ),
                    ft.Container(
                        height=38,
                        alignment=ft.Alignment(-1, -1),
                        content=ft.Text(
                            title,
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT_PRIMARY,
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ),
                    ft.Container(
                        height=34,
                        alignment=ft.Alignment(-1, -1),
                        content=ft.Text(
                            description,
                            size=13,
                            color=TEXT_SECONDARY,
                            height=1.25,
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ),
                    *(
                        [action_content]
                        if action_content
                        else []
                    ),
                ],
                spacing=7,
            ),
        )
        return feature

    featured_sections = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(width=3, height=18, border_radius=2, bgcolor=ACCENT),
                    ft.Text(
                        "FEATURED SECTIONS",
                        size=13,
                        color=TEXT_SECONDARY,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    feature_card(
                        "MATLAB Project",
                        "In-depth project showcasing MATLAB skills",
                        "See project",
                        ft.Icons.CODE_ROUNDED,
                        ACCENT2,
                        "#211044",
                        target_url=MATLAB_PROJECT_URL,
                    ),
                    feature_card(
                        "MineShield App",
                        "App development project built from scratch",
                        "Explore app",
                        ft.Icons.SHIELD_OUTLINED,
                        TEAL,
                        "#033A23",
                        target_url=MINESHIELD_APP_URL,
                    ),
                    feature_card(
                        "Typing Proficiency",
                        "Speed and accuracy records and progress",
                        "View certificate",
                        ft.Icons.KEYBOARD_ROUNDED,
                        GOLD,
                        "#332704",
                        target_url=TYPING_CERTIFICATE_URL,
                    ),
                ],
                spacing=14,
                run_spacing=14,
                wrap=True,
            ),
            ft.Container(height=1, bgcolor=ft.Colors.with_opacity(0.85, BORDER)),
        ],
        spacing=22,
    )
    featured_sections = ft.Container(
        padding=ft.Padding(34, 0, 34, 0),
        content=featured_sections,
    )

    return ft.Column(
        controls=[hero, featured_sections],
        spacing=34,
        scroll=hidden_scroll(),
        expand=True,
    )


def main_legacy(page: ft.Page) -> None:
    page.title       = "Individual Web Portfolio — Comp Prog I 2026"
    page.bgcolor     = BG
    page.padding     = 0
    page.theme_mode  = ft.ThemeMode.DARK
    page.theme       = ft.Theme(scrollbar_theme=portfolio_scrollbar_theme())
    page.dark_theme  = ft.Theme(scrollbar_theme=portfolio_scrollbar_theme())
    page.fonts       = {"Courier New": "https://fonts.cdnfonts.com/css/courier-new"}
    page.scroll      = ft.ScrollMode.HIDDEN

    # ── content area ──────────────────────────
    content_area = ft.Container(
        expand=True,
        padding=ft.Padding(20, 20, 20, 20),
        content=build_home(),
    )

    pages = [
        build_home,
        build_timeline,
        build_matlab,
        build_blog,
        build_github,
        build_marks,
    ]

    def on_nav_change(e: ft.ControlEvent) -> None:
        idx = page.navigation_bar.selected_index
        content_area.content = pages[idx]()
        page.update()

    # ── top app bar ───────────────────────────
    page.appbar = ft.AppBar(
        title=ft.Text(
            "Web Portfolio  ·  2026",
            size=16,
            weight=ft.FontWeight.W_600,
            color=TEXT_PRIMARY,
            font_family="Courier New",
        ),
        bgcolor=SURFACE,
        center_title=False,
        actions=[
            ft.Container(
                content=ft.Text(
                    "Flet 0.85.2",
                    size=11,
                    color=TEXT_SECONDARY,
                    font_family="Courier New",
                ),
                padding=ft.Padding(0, 0, 16, 0),
            ),
        ],
    )

    # ── bottom navigation bar ─────────────────
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        bgcolor=SURFACE,
        indicator_color=ft.Colors.with_opacity(0.15, ACCENT),
        destinations=[
            ft.NavigationBarDestination(
                icon=icon,
                label=label,
            )
            for label, icon in zip(NAV_LABELS, NAV_ICONS)
        ],
        on_change=on_nav_change,
    )

    page.add(content_area)


def build_home(viewport_width: float | int | None = None) -> ft.Column:
    view_width = current_view_width(viewport_width)
    is_mobile = view_width < MOBILE_BREAKPOINT
    show_visual = view_width >= 1240
    hero_title_size = 36 if is_mobile else 48
    profile_width = None if is_mobile else 680
    profile_avatar_frame = 86 if is_mobile else 104
    profile_avatar = profile_avatar_frame - 8

    def border(color: str = BORDER, opacity: float = 0.62) -> ft.Border:
        side = ft.BorderSide(1, ft.Colors.with_opacity(opacity, color))
        return ft.Border(left=side, top=side, right=side, bottom=side)

    def glass_icon(icon: str, color: str, left: int, top: int, size: int = 76) -> ft.Container:
        return ft.Container(
            left=left,
            top=top,
            width=size,
            height=size,
            border_radius=10,
            bgcolor="#152840",
            border=border(TEXT_PRIMARY, 0.14),
            content=ft.Icon(icon, color=color, size=40),
            alignment=ft.Alignment(0, 0),
        )

    code_window = ft.Container(
        left=180,
        top=78,
        width=270,
        height=226,
        border_radius=8,
        bgcolor="#19345A",
        border=border(TEXT_PRIMARY, 0.24),
        content=ft.Column(
            controls=[
                ft.Container(
                    height=36,
                    padding=ft.Padding(18, 0, 0, 0),
                    border=ft.Border(
                        bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.18, TEXT_PRIMARY))
                    ),
                    content=ft.Row(
                        controls=[
                            ft.Container(width=10, height=10, border_radius=5, bgcolor="#E5E7EB"),
                            ft.Container(width=10, height=10, border_radius=5, bgcolor="#CBD5E1"),
                            ft.Container(width=10, height=10, border_radius=5, bgcolor="#94A3B8"),
                        ],
                        spacing=9,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "</>",
                                size=68,
                                weight=ft.FontWeight.BOLD,
                                color=ACCENT,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(width=210, height=8, border_radius=4, bgcolor="#557099"),
                            ft.Container(width=118, height=8, border_radius=4, bgcolor="#314868"),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=12,
                    ),
                ),
            ],
            spacing=0,
        ),
    )

    visual = ft.Container(
        width=580,
        height=350,
        border_radius=10,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#06111F", "#0D2548", "#06111F"],
        ),
        content=ft.Stack(
            width=580,
            height=350,
            controls=[
                ft.Container(
                    left=70,
                    top=32,
                    width=430,
                    height=286,
                    border_radius=18,
                    bgcolor=ft.Colors.with_opacity(0.08, ACCENT),
                ),
                glass_icon(ft.Icons.AUTO_GRAPH_ROUNDED, ORANGE, 85, 42),
                glass_icon(ft.Icons.CODE_ROUNDED, TEXT_PRIMARY, 460, 55),
                glass_icon(ft.Icons.TERMINAL_ROUNDED, ACCENT, 435, 285),
                code_window,
            ],
        ),
    )

    profile_picture = ft.Container(
        width=profile_avatar_frame,
        height=profile_avatar_frame,
        border_radius=profile_avatar_frame / 2,
        padding=4,
        bgcolor="#0B1F35",
        border=border(ACCENT, 0.85),
        content=ft.Container(
            width=profile_avatar,
            height=profile_avatar,
            border_radius=profile_avatar / 2,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Image(
                src="profile_picture.jpg",
                width=profile_avatar,
                height=profile_avatar,
                fit="cover",
            ),
        ),
    )

    intro_chips = ft.Row(
        controls=[
            ft.Container(
                width=118,
                height=34,
                border_radius=18,
                padding=ft.Padding(14, 0, 12, 0),
                bgcolor="#1B2636",
                border=border(TEXT_PRIMARY, 0.10),
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "Welcome",
                            size=13,
                            color=ACCENT,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Icon(ft.Icons.WAVING_HAND_ROUNDED, size=14, color=GOLD),
                    ],
                    spacing=6,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            ft.Container(
                width=154,
                height=30,
                border_radius=16,
                padding=ft.Padding(12, 0, 12, 0),
                bgcolor=ft.Colors.with_opacity(0.12, TEAL),
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.VERIFIED_ROUNDED, color=TEAL, size=15),
                        ft.Text(
                            "Student Developer",
                            size=12,
                            color=TEAL,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                    spacing=6,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
        ],
        spacing=10,
        run_spacing=8,
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START,
    )

    skill_badges = ft.Row(
        controls=[
            badge("Python"),
            badge("MATLAB", GOLD),
            badge("MineShield", TEAL),
            badge("Typing Proficiency", ORANGE),
        ],
        spacing=8,
        run_spacing=8,
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START,
    )

    profile_copy = ft.Column(
        controls=[
            intro_chips,
            ft.Text(
                "Andre Cavota",
                size=25 if is_mobile else 26,
                weight=ft.FontWeight.BOLD,
                color=TEXT_PRIMARY,
                text_align=ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT,
            ),
            ft.Text(
                "Computer Programming I - Semester 1, 2026",
                size=12 if is_mobile else 13,
                color=TEXT_SECONDARY,
                text_align=ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT,
            ),
            ft.Text(
                "Building practical web, MATLAB, and engineering app projects with a focus on clean UI and useful problem solving.",
                size=12 if is_mobile else 13,
                color=TEXT_SECONDARY,
                text_align=ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT,
            ),
            skill_badges,
        ],
        spacing=7,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=(
            ft.CrossAxisAlignment.CENTER if is_mobile else ft.CrossAxisAlignment.START
        ),
        expand=not is_mobile,
    )

    profile_card = ft.Container(
        width=profile_width,
        border_radius=14,
        padding=ft.Padding(14 if is_mobile else 16, 14, 14 if is_mobile else 16, 14),
        bgcolor="#081A2C",
        border=border(BORDER, 0.72),
        content=(
            ft.Column(
                controls=[profile_picture, profile_copy],
                spacing=14,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            if is_mobile
            else ft.Row(
                controls=[profile_picture, profile_copy],
                spacing=18,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ),
    )

    hero_heading = (
        ft.Column(
            controls=[
                ft.Text(
                    "Welcome to My",
                    size=hero_title_size,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT_PRIMARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Web Portfolio",
                    size=hero_title_size,
                    weight=ft.FontWeight.BOLD,
                    color=ACCENT,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        if is_mobile
        else ft.Row(
            controls=[
                ft.Text(
                    "Welcome to My",
                    size=hero_title_size,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT_PRIMARY,
                ),
                ft.Text(
                    "Web Portfolio",
                    size=hero_title_size,
                    weight=ft.FontWeight.BOLD,
                    color=ACCENT,
                ),
            ],
            spacing=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    hero_copy = ft.Container(
        width=None if (is_mobile or not show_visual) else 760,
        expand=not show_visual and not is_mobile,
        content=ft.Column(
            controls=[
                profile_card,
                hero_heading,
                ft.Text(
                    "Showcasing my technical achievements, learning journey, and contributions across multiple platforms.",
                    size=14 if is_mobile else 16,
                    color=TEXT_SECONDARY,
                    height=1.5,
                    text_align=ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT,
                ),
                ft.Row(
                    controls=[
                        ft.Container(width=48, height=2, bgcolor=ACCENT),
                        ft.Container(expand=True, height=2, bgcolor="#193456"),
                    ],
                    spacing=0,
                ),
            ],
            spacing=14 if is_mobile else 16,
            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER if is_mobile else ft.CrossAxisAlignment.START
            ),
        ),
    )

    hero = ft.Container(
        height=None if is_mobile else 430,
        border_radius=10,
        padding=ft.Padding(18 if is_mobile else 34, 22 if is_mobile else 32, 18 if is_mobile else 34, 22 if is_mobile else 32),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#07111F", "#0B1423", "#071A31"],
        ),
        border=border(BORDER, 0.72),
        content=(
            hero_copy
            if is_mobile
            else ft.Row(
                controls=[hero_copy, *([visual] if show_visual else [])],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ),
    )

    def feature_card(
        title: str,
        description: str,
        action: str | None,
        icon: str | None,
        color: str,
        surface: str,
        target_url: str | ft.Url | None = None,
        action_icon: str | None = ft.Icons.ARROW_FORWARD_ROUNDED,
    ) -> ft.Container:
        is_link = bool(target_url)
        action_controls: list[ft.Control] = []
        if action:
            action_controls.append(
                ft.Text(
                    action,
                    size=13,
                    color=color,
                    weight=ft.FontWeight.BOLD,
                )
            )
        if action and action_icon:
            action_controls.append(ft.Icon(action_icon, color=color, size=16))
        action_content = (
            ft.Row(
                controls=action_controls,
                spacing=6,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
            if action_controls
            else None
        )
        if action_content and is_link:
            action_content = ft.TextButton(
                content=action_content,
                height=32,
                url=str(target_url),
                tooltip=f"Open {title}",
                style=ft.ButtonStyle(
                    padding=ft.Padding(0, 0, 0, 0),
                    shape=ft.RoundedRectangleBorder(radius=6),
                    overlay_color=ft.Colors.with_opacity(0.12, color),
                    mouse_cursor=ft.MouseCursor.CLICK,
                ),
            )
        feature = ft.Container(
            width=max(240, min(320, view_width - 88)) if is_mobile else 209,
            height=187,
            border_radius=11,
            padding=ft.Padding(20, 17, 20, 17),
            bgcolor=surface,
            ink=False,
            border=border(color, 0.42),
            content=ft.Column(
                controls=[
                    *(
                        [
                            ft.Container(
                                width=42,
                                height=42,
                                border_radius=9,
                                bgcolor=ft.Colors.with_opacity(0.16, color),
                                padding=ft.Padding(0, 0, 0, 4),
                                content=ft.Icon(icon, color=color, size=23),
                                alignment=ft.Alignment(0, -0.22),
                            )
                        ]
                        if icon
                        else []
                    ),
                    ft.Container(
                        height=38,
                        alignment=ft.Alignment(-1, -1),
                        content=ft.Text(
                            title,
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT_PRIMARY,
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ),
                    ft.Container(
                        height=34,
                        alignment=ft.Alignment(-1, -1),
                        content=ft.Text(
                            description,
                            size=13,
                            color=TEXT_SECONDARY,
                            height=1.25,
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ),
                    *(
                        [action_content]
                        if action_content
                        else []
                    ),
                ],
                spacing=7,
            ),
        )
        return feature

    featured_sections = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(width=3, height=18, border_radius=2, bgcolor=ACCENT),
                    ft.Text(
                        "FEATURED SECTIONS",
                        size=13,
                        color=TEXT_SECONDARY,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    feature_card(
                        "MATLAB Projects",
                        "In-depth project showcasing MATLAB skills",
                        "See project",
                        ft.Icons.CODE_ROUNDED,
                        ACCENT2,
                        "#211044",
                        target_url=MATLAB_PROJECT_URL,
                    ),
                    feature_card(
                        "MineShield App",
                        "App development project built from scratch",
                        "Explore app",
                        ft.Icons.SHIELD_OUTLINED,
                        TEAL,
                        "#033A23",
                        target_url=MINESHIELD_APP_URL,
                    ),
                    feature_card(
                        "Typing Proficiency",
                        "Speed and accuracy records and progress",
                        "View certificate",
                        ft.Icons.KEYBOARD_ROUNDED,
                        GOLD,
                        "#332704",
                        target_url=TYPING_CERTIFICATE_URL,
                    ),
                ],
                spacing=14,
                run_spacing=14,
                wrap=True,
                alignment=ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START,
            ),
            ft.Container(height=1, bgcolor=ft.Colors.with_opacity(0.85, BORDER)),
        ],
        spacing=22,
    )
    featured_sections = ft.Container(
        padding=ft.Padding(4 if is_mobile else 34, 0, 4 if is_mobile else 34, 0),
        content=featured_sections,
    )

    return ft.Column(
        controls=[hero, featured_sections],
        spacing=34,
        scroll=hidden_scroll(),
        expand=True,
    )


def build_timeline(viewport_width: float | int | None = None) -> ft.Column:
    view_width = current_view_width(viewport_width)
    is_mobile = view_width < MOBILE_BREAKPOINT
    linear_timeline = view_width < NARROW_BREAKPOINT
    content_width = available_width(view_width, 900, 28 if linear_timeline else 64)
    timeline_card_width = min(386, content_width - (54 if linear_timeline else 0))
    timeline_text_width = max(220, timeline_card_width - 48)
    navy_deep = "#0A0F2E"
    navy_light = "#162260"
    navy_accent = "#1E3A8A"
    timeline_gold = "#C9A84C"
    gold_light = "#E8C87A"
    white = "#F0F4FF"
    muted = "#8892B0"
    line = ft.Colors.with_opacity(0.25, timeline_gold)
    card_bg = ft.Colors.with_opacity(0.45, navy_light)
    card_border = ft.Colors.with_opacity(0.18, timeline_gold)

    timeline = [
        {
            "week": "Week 1 - Project Kickoff",
            "entries": [
                {
                    "side": "right",
                    "tag": "Role Assignment",
                    "title": "Appointed Documentation Lead",
                    "body": (
                        "Assigned as Documentation Lead for the 19-member MineShield team - "
                        "one of five named leadership roles alongside the Project Manager, "
                        "Firebase Lead, UI/UX Lead, and GitHub Manager."
                    ),
                },
                {
                    "side": "left",
                    "tag": "Team Structure - Group 4",
                    "title": "Documentation Sub-Group Formed",
                    "body": (
                        "Led Group 4 (Documentation) consisting of Hafeni Hilokuah, Elia "
                        "Gabriel, and Annaliah Simasiku. Established documentation standards "
                        "and writing conventions for the project."
                    ),
                },
            ],
        },
        {
            "week": "Week 2 - SRS Authorship",
            "entries": [
                {
                    "side": "right",
                    "tag": "SRS - Sections 1 & 2",
                    "title": "Product Introduction & System Overview",
                    "body": (
                        "Authored Section 1 (introducing MineShield, the team, and the "
                        "proposed product) and Section 2 (system description, target users, "
                        "technology overview, Firebase data model, assumptions and constraints)."
                    ),
                },
                {
                    "side": "left",
                    "tag": "SRS - Sections 3-6",
                    "title": "Functional Requirements & Use Cases",
                    "body": (
                        "Documented all 15 functional requirements (FR-001 to FR-015) with "
                        "priority levels and Firebase service mappings, non-functional "
                        "requirements, the use case diagram, and the project conclusion."
                    ),
                    "bullets": [
                        "FR-001 to FR-015 fully documented",
                        "High / Medium priority classifications assigned",
                        "Use case diagram: Worker, Supervisor, Visitor interactions",
                    ],
                },
            ],
        },
        {
            "week": "Week 3 - Phase 2 Planning",
            "entries": [
                {
                    "side": "right",
                    "tag": "Phase 2 - Group F Lead",
                    "title": "Analytics & Supervisor Dashboard Documentation",
                    "body": (
                        "Served as documentation lead for Group F, covering FR-011, FR-012, "
                        "and FR-013. Specified requirements for the AnalyticsDashboardScreen, "
                        "PastHazardsScreen, and all chart components."
                    ),
                    "bullets": [
                        "Documented BarChart, LineChart, PieChart component specs",
                        "Defined success criteria: supervisor sees hazard trends and can browse past hazards",
                    ],
                },
                {
                    "side": "left",
                    "tag": "Phase 2 - Implementation Plan",
                    "title": "Phase 2 Plan Document Authored",
                    "body": (
                        "Co-authored the Phase 2 Implementation Plan distributed to all 7 "
                        "groups, detailing task breakdowns per functional requirement, "
                        "success criteria, the two-week delivery timeline, and the Git "
                        "branching strategy."
                    ),
                },
            ],
        },
        {
            "week": "Week 4 - Phase 3 Preparation",
            "entries": [
                {
                    "side": "right",
                    "tag": "Phase 3 - Q&A Guide",
                    "title": "Q&A Preparation Guide - All 19 Members",
                    "body": (
                        "Authored the comprehensive Q&A preparation guide used by all 19 "
                        "presenters, covering 27 questions across 5 categories: general "
                        "project, functional requirements, technical implementation, project "
                        "management, and device-specific questions."
                    ),
                    "bullets": [
                        "Assigned a responsible team member to each question",
                        "Categories: General, FR-specific, Technical, PM, Device",
                    ],
                },
            ],
        },
        {
            "week": "Week 5 - Documentation Sprint",
            "entries": [
                {
                    "side": "left",
                    "tag": "Deliverable - TRACEABILITY_MATRIX.md",
                    "title": "Final SRS Traceability Matrix",
                    "body": (
                        "Created the traceability matrix mapping every functional requirement "
                        "(FR-001 to FR-015) to its specific source file, responsible team "
                        "member, and test case - serving as the definitive proof of SRS "
                        "compliance for the assessors."
                    ),
                },
                {
                    "side": "right",
                    "tag": "Deliverable - FINAL_SUBMISSION.md",
                    "title": "Executive Summary & Team Reflections",
                    "body": (
                        "Compiled all 19 team member reflections and drafted the executive "
                        "summary in FINAL_SUBMISSION.md, providing an overview of project "
                        "outcomes, lessons learned, and final deliverable status."
                    ),
                },
            ],
        },
        {
            "week": "Week 6 - Code & Compliance Files",
            "entries": [
                {
                    "side": "left",
                    "tag": "Code - documentGenerator.js",
                    "title": "Document Generator Utility",
                    "body": (
                        "Implemented src/utils/documentGenerator.js - a utility enabling "
                        "programmatic generation of structured safety reports from Firestore "
                        "hazard data, supporting the Civil and Metallurgical engineering "
                        "compliance reporting workflows."
                    ),
                },
                {
                    "side": "right",
                    "tag": "Code - reportExporter.js",
                    "title": "Report Exporter Utility",
                    "body": (
                        "Implemented src/utils/reportExporter.js - export logic for analytics "
                        "and hazard data, directly supporting FR-013 (Generate Analytics Reports)."
                    ),
                },
                {
                    "side": "left",
                    "tag": "Deliverables - Docs",
                    "title": "PRESENTATION_SLIDES.md & SRS_COMPLIANCE.md",
                    "body": (
                        "Authored the final presentation structure document and the SRS "
                        "compliance verification file confirming all 15 functional requirements "
                        "were satisfied in the submitted codebase."
                    ),
                    "chips": [
                        "documentGenerator.js",
                        "reportExporter.js",
                        "TRACEABILITY_MATRIX.md",
                        "FINAL_SUBMISSION.md",
                        "PRESENTATION_SLIDES.md",
                        "SRS_COMPLIANCE.md",
                    ],
                },
            ],
        },
        {
            "week": "Week 7 - Final Submission - May 31, 2026",
            "entries": [
                {
                    "side": "right",
                    "tag": "Presentation - 11:10 AM",
                    "title": "Live Q&A - Documentation & Traceability",
                    "body": (
                        "Presented the documentation and traceability work live to supervisors "
                        "and assessors on Sunday, May 31, 2026 at 11:10 AM, demonstrating FR "
                        "mapping, SRS compliance, and the complete traceability matrix."
                    ),
                },
                {
                    "side": "left",
                    "tag": "Sign-Off",
                    "title": "Phase 3 Completion Confirmed",
                    "body": (
                        "Signed the Phase 3 completion acknowledgement confirming: all 6 "
                        "assigned files committed to GitHub, app runs without crashes on the "
                        "test device, and full preparation for the Q&A session completed."
                    ),
                },
            ],
        },
    ]

    def outline(color: str, width: int = 1) -> ft.Border:
        side = ft.BorderSide(width, color)
        return ft.Border(left=side, top=side, right=side, bottom=side)

    def stat_card(value: str, label: str) -> ft.Container:
        return ft.Container(
            width=138 if not is_mobile else max(126, min(152, (content_width - 24) / 2)),
            height=82,
            content=ft.Column(
                controls=[
                    ft.Text(
                        value,
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=timeline_gold,
                        font_family="Georgia",
                    ),
                    ft.Text(
                        label.upper(),
                        size=10,
                        color=muted,
                        weight=ft.FontWeight.W_600,
                    ),
                ],
                spacing=3,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

    def section_header() -> ft.Container:
        return ft.Container(
            width=content_width,
            padding=ft.Padding(0, 20 if is_mobile else 34, 0, 18),
            content=ft.Column(
                controls=[
                    ft.Text(
                        "SECTION 01",
                        size=11,
                        color=timeline_gold,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Project Timeline",
                        size=30 if is_mobile else 36,
                        color=white,
                        weight=ft.FontWeight.BOLD,
                        font_family="Georgia",
                    ),
                    ft.Text(
                        "Weekly log of specific contributions to the MineShield group project across all three phases.",
                        size=14,
                        color=muted,
                        width=min(520, content_width - 24),
                        text_align=ft.TextAlign.CENTER,
                        height=1.55,
                    ),
                    ft.Container(
                        width=60,
                        height=2,
                        margin=ft.Margin(0, 10, 0, 0),
                        gradient=ft.LinearGradient(
                            begin=ft.Alignment(-1, 0),
                            end=ft.Alignment(1, 0),
                            colors=[
                                ft.Colors.TRANSPARENT,
                                timeline_gold,
                                ft.Colors.TRANSPARENT,
                            ],
                        ),
                    ),
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def week_label(text: str) -> ft.Container:
        return ft.Container(
            width=content_width,
            padding=ft.Padding(0, 26, 0, 20),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            text.upper(),
                            size=11,
                            color=timeline_gold,
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor=navy_accent,
                        border=outline(timeline_gold),
                        border_radius=40,
                        padding=ft.Padding(22, 8, 22, 8),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

    def card_tag(text: str) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Container(width=16, height=1, bgcolor=timeline_gold),
                ft.Text(
                    text.upper(),
                    size=10,
                    color=timeline_gold,
                    weight=ft.FontWeight.BOLD,
                ),
            ],
            spacing=7,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def bullet_item(text: str) -> ft.Row:
        return ft.Row(
            controls=[
                ft.Text(">", size=13, color=timeline_gold, weight=ft.FontWeight.BOLD),
                ft.Text(text, size=12, color=muted, width=max(180, timeline_text_width - 22), height=1.45),
            ],
            spacing=7,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    def file_chip(text: str) -> ft.Container:
        return ft.Container(
            content=ft.Text(text, size=10, color=gold_light),
            bgcolor=ft.Colors.with_opacity(0.10, timeline_gold),
            border=outline(ft.Colors.with_opacity(0.20, timeline_gold)),
            border_radius=4,
            padding=ft.Padding(8, 4, 8, 4),
        )

    def timeline_card(entry: dict) -> ft.Container:
        bullets = entry.get("bullets", [])
        chips = entry.get("chips", [])
        content_controls = [
            card_tag(entry["tag"]),
            ft.Text(
                entry["title"],
                size=18,
                color=white,
                weight=ft.FontWeight.BOLD,
                font_family="Georgia",
                width=timeline_text_width,
                height=1.25,
            ),
            ft.Text(entry["body"], size=13, color=muted, width=timeline_text_width, height=1.55),
        ]
        if bullets:
            content_controls.append(
                ft.Column(
                    controls=[bullet_item(item) for item in bullets],
                    spacing=4,
                )
            )
        if chips:
            content_controls.append(
                ft.Row(
                    controls=[file_chip(chip) for chip in chips],
                    spacing=6,
                    run_spacing=6,
                    wrap=True,
                )
            )

        return ft.Container(
            width=timeline_card_width,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            border_radius=12,
            bgcolor=card_bg,
            border=outline(card_border),
            shadow=ft.BoxShadow(
                blur_radius=28,
                color=ft.Colors.with_opacity(0.20, ft.Colors.BLACK),
            ),
            content=ft.Column(
                controls=[
                    ft.Container(
                        height=2,
                        gradient=ft.LinearGradient(
                            begin=ft.Alignment(-1, 0),
                            end=ft.Alignment(1, 0),
                            colors=[
                                ft.Colors.TRANSPARENT,
                                timeline_gold,
                                ft.Colors.TRANSPARENT,
                            ],
                        ),
                    ),
                    ft.Container(
                        padding=ft.Padding(24, 20, 24, 22),
                        content=ft.Column(controls=content_controls, spacing=10),
                    ),
                ],
                spacing=0,
            ),
        )

    def dot_column(height: int) -> ft.Container:
        return ft.Container(
            width=42,
            height=height,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        left=20,
                        top=0,
                        width=1,
                        height=height,
                        bgcolor=line,
                    ),
                    ft.Container(
                        left=13,
                        top=25,
                        width=16,
                        height=16,
                        border_radius=8,
                        bgcolor=timeline_gold,
                        border=outline(navy_deep, 3),
                        shadow=ft.BoxShadow(
                            blur_radius=16,
                            color=ft.Colors.with_opacity(0.50, timeline_gold),
                        ),
                    ),
                ],
            ),
        )

    def entry_height(entry: dict) -> int:
        body_extra = 24 if len(entry["body"]) > 220 else 0
        return 132 + body_extra + (26 * len(entry.get("bullets", []))) + (
            42 if entry.get("chips") else 0
        )

    def timeline_entry(entry: dict) -> ft.Container:
        height = entry_height(entry)
        current_card = timeline_card(entry)
        gap = ft.Container(width=28)
        empty = ft.Container(width=timeline_card_width, height=1)
        marker = dot_column(height + 18)
        if linear_timeline:
            return ft.Container(
                width=content_width,
                margin=ft.Margin(0, 0, 0, 20),
                content=ft.Row(
                    controls=[marker, ft.Container(width=12), current_card],
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            )
        controls = (
            [current_card, gap, marker, gap, empty]
            if entry["side"] == "left"
            else [empty, gap, marker, gap, current_card]
        )

        return ft.Container(
            width=content_width,
            margin=ft.Margin(0, 0, 0, 20),
            content=ft.Row(
                controls=controls,
                spacing=0,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        )

    timeline_controls = []
    for week in timeline:
        timeline_controls.append(week_label(week["week"]))
        timeline_controls.extend(timeline_entry(entry) for entry in week["entries"])

    footer = ft.Container(
        width=content_width,
        padding=ft.Padding(0, 28, 0, 42),
        content=ft.Column(
            controls=[
                ft.Container(width=min(300, content_width - 24), height=1, bgcolor=line),
                ft.Text(
                    "MineShield - Group 16 - Computer Programming I",
                    size=13,
                    color=muted,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Submitted: Sunday, May 31, 2026 - Protecting Lives Underground",
                    size=12,
                    color=muted,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Web Portfolio contributes 15% to overall CA",
                    size=12,
                    color=timeline_gold,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=7,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return ft.Column(
        controls=[
            ft.Container(
                expand=True,
                bgcolor=navy_deep,
                content=ft.Column(
                    controls=[
                        section_header(),
                        ft.Row(
                            controls=[
                                stat_card("3", "Phases"),
                                stat_card("6", "Files Assigned"),
                                stat_card("15", "FRs Traced"),
                                stat_card("15%", "CA Weight"),
                            ],
                            spacing=34,
                            wrap=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(height=16),
                        *timeline_controls,
                        footer,
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        ],
        spacing=0,
        scroll=hidden_scroll(),
        expand=True,
    )


def main(page: ft.Page) -> None:
    page.title       = "Individual Web Portfolio - Comp Prog I 2026"
    page.bgcolor     = BG
    page.padding     = 0
    page.theme_mode  = ft.ThemeMode.DARK
    page.theme       = ft.Theme(scrollbar_theme=portfolio_scrollbar_theme())
    page.dark_theme  = ft.Theme(scrollbar_theme=portfolio_scrollbar_theme())
    page.fonts       = {"Courier New": "https://fonts.cdnfonts.com/css/courier-new"}
    page.scroll      = ft.ScrollMode.HIDDEN

    pages = [
        build_home,
        build_timeline,
        build_matlab,
        build_blog,
        build_github,
    ]
    selected_index = 0
    header_shell = ft.Container()

    def build_scrollable_page(index: int) -> ft.Column:
        scrollable_page = pages[index](page.width)
        scrollable_page.scroll = ft.ScrollMode.HIDDEN
        return scrollable_page

    content_area = ft.Container(
        expand=True,
        content=build_scrollable_page(selected_index),
    )

    def show_page(index: int) -> None:
        nonlocal selected_index
        selected_index = index
        content_area.content = build_scrollable_page(index)
        header_shell.content = build_header()
        page.update()

    def nav_item(label: str, icon: str, index: int, compact: bool = False) -> ft.Container:
        active = selected_index == index
        blog_mode = selected_index == 3
        github_mode = selected_index == 4
        article_mode = blog_mode or github_mode
        nav_accent = "#C9A84C" if article_mode else ACCENT
        label_color = nav_accent if active else (TEXT_SECONDARY if article_mode else TEXT_PRIMARY)
        label_size = 12 if article_mode else 14
        body = (
            ft.Icon(icon, size=20, color=label_color)
            if compact
            else (
            ft.Row(
                controls=[
                    ft.Icon(icon, size=18, color=label_color),
                    ft.Text(
                        label,
                        size=label_size,
                        color=label_color,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
            if label == "GitHub"
            else ft.Text(label, size=label_size, color=label_color, weight=ft.FontWeight.BOLD)
            )
        )
        return ft.Container(
            width=46 if compact else 86,
            height=44 if compact else 58,
            border_radius=8 if compact else None,
            bgcolor=ft.Colors.with_opacity(0.10, nav_accent) if compact and active else None,
            tooltip=label,
            on_click=lambda e, i=index: show_page(i),
            content=ft.Column(
                controls=[
                    ft.Container(expand=True, alignment=ft.Alignment(0, 0), content=body),
                    ft.Container(
                        width=50,
                        height=2,
                        border_radius=1,
                        bgcolor=nav_accent if active else ft.Colors.TRANSPARENT,
                    ),
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def build_header() -> ft.Container:
        view_width = current_view_width(page.width)
        is_mobile = view_width < MOBILE_BREAKPOINT
        compact_nav = view_width < 1040
        blog_mode = selected_index == 3
        github_mode = selected_index == 4
        article_mode = blog_mode or github_mode
        header_accent = "#C9A84C" if article_mode else ACCENT
        header_border = ft.Colors.with_opacity(0.25, header_accent) if article_mode else ft.Colors.with_opacity(0.62, BORDER)
        header_bg = ft.Colors.with_opacity(0.92, "#0A0F2E") if article_mode else ft.Colors.with_opacity(0.42, SURFACE)

        if github_mode:
            logo = ft.Text(
                "Andre Cavota",
                size=18 if not is_mobile else 17,
                weight=ft.FontWeight.BOLD,
                color=header_accent,
                font_family="Georgia",
            )
        elif blog_mode:
            logo = ft.Row(
                controls=[
                    ft.Container(
                        width=28 if not is_mobile else 26,
                        height=28 if not is_mobile else 26,
                        border_radius=6,
                        alignment=ft.Alignment(0, 0),
                        bgcolor=header_accent,
                        content=ft.Text(
                            "AC",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color="#0A0F2E",
                            font_family="Georgia",
                        ),
                    ),
                    ft.Text(
                        "Andre Cavota",
                        size=16 if not is_mobile else 15,
                        weight=ft.FontWeight.BOLD,
                        color=header_accent,
                        font_family="Georgia",
                    ),
                ],
                spacing=8 if is_mobile else 10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        else:
            logo = ft.Row(
                controls=[
                    ft.Container(
                        width=38 if is_mobile else 44,
                        height=38 if is_mobile else 44,
                        border_radius=7 if is_mobile else 8,
                        alignment=ft.Alignment(0, 0),
                        gradient=ft.LinearGradient(
                            begin=ft.Alignment(-1, -1),
                            end=ft.Alignment(1, 1),
                            colors=[ACCENT, ft.Colors.with_opacity(0.22, ACCENT)],
                        ),
                        content=ft.Text(
                            "AC",
                            size=19 if is_mobile else 22,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT_PRIMARY,
                            font_family="Courier New",
                        ),
                    ),
                    (
                        ft.Text(
                            "Andre Cavota",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT_PRIMARY,
                        )
                        if is_mobile
                        else ft.Row(
                            controls=[
                                ft.Text("Andre", size=25, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                                ft.Text("Cavota", size=25, weight=ft.FontWeight.BOLD, color=ACCENT),
                            ],
                            spacing=7,
                        )
                    ),
                ],
                spacing=10 if is_mobile else 14,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )

        contact_foreground = (
            header_accent
            if github_mode
            else "#0A0F2E"
            if blog_mode
            else TEXT_PRIMARY
        )

        if is_mobile:
            contact_button = ft.Container(
                width=42,
                height=38,
                border_radius=8,
                bgcolor=ft.Colors.with_opacity(0.10, header_accent) if github_mode else header_accent,
                border=ft.Border(
                    left=ft.BorderSide(1, ft.Colors.with_opacity(0.45, header_accent)),
                    top=ft.BorderSide(1, ft.Colors.with_opacity(0.45, header_accent)),
                    right=ft.BorderSide(1, ft.Colors.with_opacity(0.45, header_accent)),
                    bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.45, header_accent)),
                ),
                url=CONTACT_EMAIL_URL,
                tooltip="Email Andre Cavota",
                alignment=ft.Alignment(0, 0),
                content=ft.Icon(ft.Icons.MAIL_OUTLINE_ROUNDED, color=contact_foreground, size=20),
            )
        else:
            contact_button = ft.FilledButton(
                "Contact",
                icon=ft.Icons.MAIL_OUTLINE_ROUNDED,
                icon_color=contact_foreground,
                width=118,
                height=36 if blog_mode else 39,
                color=contact_foreground,
                bgcolor=ft.Colors.with_opacity(0.10, header_accent) if github_mode else header_accent,
                url=CONTACT_EMAIL_URL,
                tooltip="Email Andre Cavota",
                style=ft.ButtonStyle(
                    padding=ft.Padding(0, 0, 0, 0),
                    side=(
                        ft.BorderSide(1, ft.Colors.with_opacity(0.45, header_accent))
                        if github_mode
                        else None
                    ),
                    shape=ft.RoundedRectangleBorder(radius=6),
                    overlay_color=ft.Colors.with_opacity(0.14, contact_foreground),
                    text_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD),
                    mouse_cursor=ft.MouseCursor.CLICK,
                ),
            )

        nav_controls = [
            nav_item(label, icon, index, compact=compact_nav)
            for index, (label, icon) in enumerate(zip(NAV_LABELS, NAV_ICONS))
        ]

        return ft.Container(
            height=114 if is_mobile else (58 if blog_mode else 74),
            border_radius=6 if article_mode else 10,
            padding=ft.Padding(12 if is_mobile else (18 if blog_mode else 22), 0, 12 if is_mobile else 20, 0),
            bgcolor=header_bg,
            border=ft.Border(
                left=ft.BorderSide(1, header_border),
                top=ft.BorderSide(1, header_border),
                right=ft.BorderSide(1, header_border),
                bottom=ft.BorderSide(1, header_border),
            ),
            content=(
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[logo, ft.Container(expand=True), contact_button],
                            spacing=10,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=nav_controls,
                            spacing=5,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=8,
                    alignment=ft.MainAxisAlignment.CENTER,
                )
                if is_mobile
                else ft.Row(
                    controls=[
                        logo,
                        ft.Container(expand=True),
                        ft.Row(
                            controls=nav_controls,
                            spacing=8 if not compact_nav else 4,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        contact_button,
                    ],
                    spacing=22,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ),
        )

    header_shell.content = build_header()
    page.appbar = None
    page.navigation_bar = None

    def handle_resize(e: ft.PageResizeEvent) -> None:
        content_area.content = build_scrollable_page(selected_index)
        header_shell.content = build_header()
        page.update()

    page.on_resize = handle_resize

    page.add(
        ft.Container(
            expand=True,
            padding=ft.Padding(10, 6, 10, 0),
            bgcolor=BG,
            content=ft.Column(
                controls=[
                    header_shell,
                    content_area,
                ],
                spacing=24,
                expand=True,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(
        main,
        view=ft.AppView.WEB_BROWSER,
        port=8550,
        assets_dir=str(ASSETS_DIR),
    )
