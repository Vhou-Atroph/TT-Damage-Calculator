"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph

Run the Toontown Damage Calculator with python -m tt_damage_calculator instead!
"""

__version__ = "4.3.2"

# Imports for library functionality
from .tt_damage_calculator import Gag, cog_hp, gag_calculator, full_calc, lvl_ind
# Imports for app functionality
from .widgets import App

def main():
    app = App()
    app.run()
