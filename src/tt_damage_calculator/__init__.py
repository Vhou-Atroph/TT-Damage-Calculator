"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph

Run the Toontown Damage Calculator with python -m tt_damage_calculator instead!
"""

__version__ = "4.3.0"

from .widgets import App

def main():
    app = App()
    app.run()
