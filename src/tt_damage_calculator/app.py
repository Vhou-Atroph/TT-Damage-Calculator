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

# Variables
settings = tt_damage_calculator.Settings(window.asset_path + "/assets/settings.toml")

### Keybinds
window.bind('<' + settings.keybinds.defense + '>', lambda par: [window.defense_buff.set(tt_damage_calculator.advance_float([0.0,0.1,0.15,0.2,0.25], window.defense_buff.get())), window.calculate()])
window.bind('<' + settings.keybinds.negative_defense + '>', lambda par: [window.defense_debuff.set(tt_damage_calculator.advance_float([0.0,0.2,0.4,0.5,0.6], window.defense_debuff.get())), window.calculate()])
window.bind('<' + settings.keybinds.lure + '>', lambda par: [window.lure.set(tt_damage_calculator.toggleswap(window.lure.get())), window.calculate()])
window.bind('<' + settings.keybinds.lock + '>', lambda par: [window.status_lock.set(tt_damage_calculator.toggleswap(window.status_lock.get())), window.calculate()])
window.bind('<' + settings.keybinds.pin + '>', lambda par: [window.pinned.set(tt_damage_calculator.toggleswap(window.pinned.get())), window.pin()])

# Organic gag toggle
window.bind('<' + settings.keybinds.organic + '>', lambda par: [window.toggle_organic()])

# Clear inputs function
window.bind('<' + settings.keybinds.reset + '>', lambda par: [window.reset_calculation()])

### Custom Gags ###
global custom_track
custom_track = StringVar()
custom_track.set("Trap")


def cgags():
  global cgags
  def add_custom_gag():
    custom_gag = widgets.GagButton(window, None, None, tt_damage_calculator.Gag("Custom", "Custom " + custom_track.get(), custom_track.get(), 0, int(damage_entry.get(1.0, END))))
    custom_gag.press()

  cgags = Toplevel(window)
  cgags.title = "Custom Gag Entry"
  cgags.resizable(0, 0)
  damage_label = Label(cgags, text="Damage", font=('Arial', 11, 'normal'))
  damage_entry = Text(cgags, width=10, height=1, font=('Arial', 11, 'normal'))
  gtype_label = Label(cgags, text="Gag Track", font=('Arial', 11, 'normal'))
  gtype_dropdown = OptionMenu(cgags, custom_track, *["Trap", "Sound", "Throw", "Squirt", "Drop"])
  custom_add = Button(cgags, text="Add to Calculation", font=('Arial', 11, 'normal'), command=add_custom_gag)

  damage_label.grid(column=0, row=0, pady=3, padx=2)
  damage_entry.grid(column=1, row=0, pady=3, padx=2)
  gtype_label.grid(column=0, row=1, pady=3, padx=2)
  gtype_dropdown.grid(column=1, row=1, pady=3, padx=2)
  custom_add.grid(column=0, row=2, columnspan=2, pady=8, padx=25)
