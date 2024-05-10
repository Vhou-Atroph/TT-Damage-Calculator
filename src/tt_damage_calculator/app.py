"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph

TT-Damage-Calculator is a gag damage calculator for Toontown Rewritten. It has an interface built with Python's tkinter library, and is supplemented with modules written in Rust.

CONTRIBUTORS:
- Vhou-Atroph
- BoggTech
"""

from tkinter import *

from . import tt_damage_calculator
from . import update_checker
from . import widgets

# Window
global window
window = widgets.App()
