"""Compatibility launcher for the portfolio Flet app.

The deployable app lives in src/main.py so Flet's web build can package it
cleanly with src/assets.
"""

import flet as ft

from src.main import ASSETS_DIR, main


if __name__ == "__main__":
    ft.run(
        main,
        view=ft.AppView.WEB_BROWSER,
        port=8550,
        assets_dir=str(ASSETS_DIR),
    )
