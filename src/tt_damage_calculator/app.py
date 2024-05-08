"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph

TT-Damage-Calculator is a gag damage calculator for Toontown Rewritten. It has an interface built with Python's tkinter library, and is supplemented with modules written in Rust.

CONTRIBUTORS:
- Vhou-Atroph
- BoggTech
"""

import os, pathlib, sys, webbrowser
from tkinter import *

from . import tt_damage_calculator
from . import update_checker
from . import widgets

# Window
global window
window = widgets.App()
asset_path = window.asset_path
whole_cream_pie_img = PhotoImage(file=asset_path + "/assets/img/whole-cream-pie.png")
window.iconphoto(True, whole_cream_pie_img)
window.resizable(0, 0)

# Variables
organic = BooleanVar()

settings = tt_damage_calculator.Settings(asset_path + "/assets/settings.toml")

# Total damage calculation
def calc_dmg(*args):
  tot_dmg = tt_damage_calculator.full_calc(window.trap, window.sound, window.throw, window.squirt, window.drop, window.nogroup.get(), window.lure.get(), window.defense_buff.get(), window.defense_debuff.get())
  window.results.level_counter.configure(text=tt_damage_calculator.lvl_ind_string(tt_damage_calculator.lvl_ind(tot_dmg), int(window.defense_buff.get() * 100), int(window.defense_debuff.get() * 100)))
  window.results.damage_counter.configure(text=str(tot_dmg))

# Toggles
tog_btns = Frame(window.column_0)
org_btn = Button(tog_btns, text='Toggle Organic', font=('Arial', 11, 'normal'))
lur_check = Checkbutton(tog_btns, text='Cog window.lure', variable=window.lure, onvalue=1, offvalue=0, font=('Arial', 11, 'normal'), command=calc_dmg)
clear_btn = Button(tog_btns, text='Reset damage', font=('Arial', 11, 'normal'))

# The Gags
class GagButton(Button):
  def __init__(self, parent, image, gag):
    self.gag = gag
    Button.__init__(self, parent)
    self['image'] = image
    if self.gag.gtype == "Gag":
      self['bg'] = '#1888D3'
      self['activebackground'] = '#186AD3'
      self['text'] = '0'
      self['font'] = ('Impress BT', 8, 'bold')
      self['compound'] = 'top'
      self['fg'] = 'white'
      self['activeforeground'] = 'white'
    self['command'] = self.press
    if parent:
      self.grid(row=0, column=self.gag.level)
    
  def list(self):
    match self.gag.track:
      case "Trap":
        return window.trap
      case "Sound":
        return window.sound
      case "Throw":
        return window.throw
      case "Squirt":
        return window.squirt
      case "Drop":
        return window.drop
      
  def press(self):
    data = self.gag.button_press(organic.get())
    self.list().append(data[0])
    hist_box.add("Gag used: " + data[1] + " (" + str(data[0]) + ")\n")
    if self.gag.gtype == "Gag":
      self.configure(text=int(self.cget("text")) + 1)
    calc_dmg()

gag_frame = Frame(window.column_0)
# Sound
snd_frame = Frame(gag_frame)
bike_horn_img = PhotoImage(file=asset_path + '/assets/img/bike-horn.png')
bike_horn = GagButton(snd_frame, image=bike_horn_img, gag=tt_damage_calculator.Gag("Gag", "Bike Horn", "Sound", 0, 4))
whistle_img = PhotoImage(file=asset_path + '/assets/img/whistle.png')
whistle = GagButton(snd_frame, image=whistle_img, gag=tt_damage_calculator.Gag("Gag", "Whistle", "Sound", 1, 7))
bugle_img = PhotoImage(file=asset_path + '/assets/img/bugle.png')
bugle = GagButton(snd_frame, image=bugle_img, gag=tt_damage_calculator.Gag("Gag", "Bugle", "Sound", 2, 11))
aoogah_img = PhotoImage(file=asset_path + '/assets/img/aoogah.png')
aoogah = GagButton(snd_frame, image=aoogah_img, gag=tt_damage_calculator.Gag("Gag", "Aoogah", "Sound", 3, 16))
elephant_trunk_img = PhotoImage(file=asset_path + '/assets/img/elephant-trunk.png')
elephant_trunk = GagButton(snd_frame, image=elephant_trunk_img, gag=tt_damage_calculator.Gag("Gag", "Elephant Trunk", "Sound", 4, 21))
fog_horn_img = PhotoImage(file=asset_path + '/assets/img/fog-horn.png')
fog_horn = GagButton(snd_frame, image=fog_horn_img, gag=tt_damage_calculator.Gag("Gag", "Fog Horn", "Sound", 5, 50))
opera_singer_img = PhotoImage(file=asset_path + '/assets/img/opera-singer.png')
opera_singer = GagButton(snd_frame, image=opera_singer_img, gag=tt_damage_calculator.Gag("Gag", "Opera Singer", "Sound", 6, 90))
# Throw
trw_frame = Frame(gag_frame)
cupcake_img = PhotoImage(file=asset_path + '/assets/img/cupcake.png')
cupcake = GagButton(trw_frame, image=cupcake_img, gag=tt_damage_calculator.Gag("Gag", "Cupcake", "Throw", 0, 6))
fruit_pie_slice_img = PhotoImage(file=asset_path + '/assets/img/fruit-pie-slice.png')
fruit_pie_slice = GagButton(trw_frame, image=fruit_pie_slice_img, gag=tt_damage_calculator.Gag("Gag", "Fruit Pie Slice", "Throw", 1, 10))
cream_pie_slice_img = PhotoImage(file=asset_path + '/assets/img/cream-pie-slice.png')
cream_pie_slice = GagButton(trw_frame, image=cream_pie_slice_img, gag=tt_damage_calculator.Gag("Gag", "Cream Pie Slice", "Throw", 2, 17))
whole_fruit_pie_img = PhotoImage(file=asset_path + '/assets/img/whole-fruit-pie.png')
whole_fruit_pie = GagButton(trw_frame, image=whole_fruit_pie_img, gag=tt_damage_calculator.Gag("Gag", "Whole Fruit Pie", "Throw", 3, 27))
whole_cream_pie = GagButton(trw_frame, image=whole_cream_pie_img, gag=tt_damage_calculator.Gag("Gag", "Whole Cream Pie", "Throw", 4, 40))
birthday_cake_img = PhotoImage(file=asset_path + '/assets/img/birthday-cake.png')
birthday_cake = GagButton(trw_frame, image=birthday_cake_img, gag=tt_damage_calculator.Gag("Gag", "Birthday Cake", "Throw", 5, 100))
wedding_cake_img = PhotoImage(file=asset_path + '/assets/img/wedding-cake.png')
wedding_cake = GagButton(trw_frame, image=wedding_cake_img, gag=tt_damage_calculator.Gag("Gag", "Wedding Cake", "Throw", 6, 120))
# Squirt
sqt_frame = Frame(gag_frame)
squirting_flower_img = PhotoImage(file=asset_path + '/assets/img/squirting-flower.png')
squirting_flower = GagButton(sqt_frame, image=squirting_flower_img, gag=tt_damage_calculator.Gag("Gag", "Squirting Flower", "Squirt", 0, 4))
water_glass_img = PhotoImage(file=asset_path + '/assets/img/glass-of-water.png')
water_glass = GagButton(sqt_frame, image=water_glass_img, gag=tt_damage_calculator.Gag("Gag", "Glass of Water", "Squirt", 1, 8))
squirt_gun_img = PhotoImage(file=asset_path + '/assets/img/squirt-gun.png')
squirt_gun = GagButton(sqt_frame, image=squirt_gun_img, gag=tt_damage_calculator.Gag("Gag", "Squirt Gun", "Squirt", 2, 12))
seltzer_bottle_img = PhotoImage(file=asset_path + '/assets/img/seltzer-bottle.png')
seltzer_bottle = GagButton(sqt_frame, image=seltzer_bottle_img, gag=tt_damage_calculator.Gag("Gag", "Seltzer Bottle", "Squirt", 3, 21))
fire_hose_img = PhotoImage(file=asset_path + '/assets/img/fire-hose.png')
fire_hose = GagButton(sqt_frame, image=fire_hose_img, gag=tt_damage_calculator.Gag("Gag", "Fire Hose", "Squirt", 4, 30))
storm_cloud_img = PhotoImage(file=asset_path + '/assets/img/storm-cloud.png')
storm_cloud = GagButton(sqt_frame, image=storm_cloud_img, gag=tt_damage_calculator.Gag("Gag", "Storm Cloud", "Squirt", 5, 80))
geyser_img = PhotoImage(file=asset_path + '/assets/img/geyser.png')
geyser = GagButton(sqt_frame, image=geyser_img, gag=tt_damage_calculator.Gag("Gag", "Geyser", "Squirt", 6, 105))
# Drop
drp_frame = Frame(gag_frame)
flower_pot_img = PhotoImage(file=asset_path + '/assets/img/flower-pot.png')
flower_pot = GagButton(drp_frame, image=flower_pot_img, gag=tt_damage_calculator.Gag("Gag", "Flower Pot", "Drop", 0, 10))
sandbag_img = PhotoImage(file=asset_path + '/assets/img/sandbag.png')
sandbag = GagButton(drp_frame, image=sandbag_img, gag=tt_damage_calculator.Gag("Gag", "Sandbag", "Drop", 1, 18))
anvil_img = PhotoImage(file=asset_path + '/assets/img/anvil.png')
anvil = GagButton(drp_frame, image=anvil_img, gag=tt_damage_calculator.Gag("Gag", "Anvil", "Drop", 2, 30))
big_weight_img = PhotoImage(file=asset_path + '/assets/img/big-weight.png')
big_weight = GagButton(drp_frame, image=big_weight_img, gag=tt_damage_calculator.Gag("Gag", "Big Weight", "Drop", 3, 45))
safe_img = PhotoImage(file=asset_path + '/assets/img/safe.png')
safe = GagButton(drp_frame, image=safe_img, gag=tt_damage_calculator.Gag("Gag", "Safe", "Drop", 4, 70))
grand_piano_img = PhotoImage(file=asset_path + '/assets/img/grand-piano.png')
grand_piano = GagButton(drp_frame, image=grand_piano_img, gag=tt_damage_calculator.Gag("Gag", "Grand Piano", "Drop", 5, 170))
toontanic_img = PhotoImage(file=asset_path + '/assets/img/toontanic.png')
toontanic = GagButton(drp_frame, image=toontanic_img, gag=tt_damage_calculator.Gag("Gag", "Toontanic", "Drop", 6, 180))
# Trap
trp_frame = Frame(gag_frame)
banana_peel_img = PhotoImage(file=asset_path + '/assets/img/banana-peel.png')
banana_peel = GagButton(trp_frame, image=banana_peel_img, gag=tt_damage_calculator.Gag("Gag", "Banana Peel", "Trap", 0, 12))
rake_img = PhotoImage(file=asset_path + '/assets/img/rake.png')
rake = GagButton(trp_frame, image=rake_img, gag=tt_damage_calculator.Gag("Gag", "Rake", "Trap", 1, 18))
marbles_img = PhotoImage(file=asset_path + '/assets/img/marbles.png')
marbles = GagButton(trp_frame, image=marbles_img, gag=tt_damage_calculator.Gag("Gag", "Marbles", "Trap", 2, 35))
quicksand_img = PhotoImage(file=asset_path + '/assets/img/quicksand.png')
quicksand = GagButton(trp_frame, image=quicksand_img, gag=tt_damage_calculator.Gag("Gag", "Quicksand", "Trap", 3, 50))
trapdoor_img = PhotoImage(file=asset_path + '/assets/img/trapdoor.png')
trapdoor = GagButton(trp_frame, image=trapdoor_img, gag=tt_damage_calculator.Gag("Gag", "Trapdoor", "Trap", 4, 85))
tnt_img = PhotoImage(file=asset_path + '/assets/img/tnt.png')
tnt = GagButton(trp_frame, image=tnt_img, gag=tt_damage_calculator.Gag("Gag", "TNT", "Trap", 5, 180))
railroad_img = PhotoImage(file=asset_path + '/assets/img/railroad.png')
railroad = GagButton(trp_frame, image=railroad_img, gag=tt_damage_calculator.Gag("Gag", "Railroad", "Trap", 6, 200))

gag_btns=[
  bike_horn, whistle, bugle, aoogah, elephant_trunk, fog_horn, opera_singer,
  cupcake, fruit_pie_slice, cream_pie_slice, whole_fruit_pie, whole_cream_pie, birthday_cake, wedding_cake,
  squirting_flower, water_glass, squirt_gun, seltzer_bottle, fire_hose, storm_cloud, geyser,
  flower_pot, sandbag, anvil, big_weight, safe, grand_piano, toontanic,
  banana_peel, rake, marbles, quicksand, trapdoor, tnt, railroad
  ]

# Add groupless damaging gag
def use_groupless(name:str, damage:int):
  window.nogroup.set(window.nogroup.get() + damage)
  hist_box.add("Gag used: " + name + " (" + str(damage) + ")\n")
  calc_dmg()

# Calculation history
hist = Frame(window.column_1)
hist_lbl = Label(hist, text="History")
hist_box = widgets.HistoryBox(hist)
clear_hist_btn = Button(hist, text="Clear History", command=hist_box.clear)
cog_calc = Button(hist, text="Show Health and\n SOS Cards")

# Cog HP
cog_health_sheet = Frame(window)
cog_health_img = PhotoImage(file=asset_path + '/assets/img/coghp.png')
cog_health_lbl = Label(cog_health_sheet, image=cog_health_img)

# SOS Cards
sos_cards = Frame(window)
sos_trp = Frame(sos_cards)
clerk_will_img = PhotoImage(file=asset_path + '/assets/img/clerkwill.png')
clerk_will = GagButton(sos_trp,image=clerk_will_img, gag=tt_damage_calculator.Gag("Sos", "Clerk Will", "Trap", 0, 60))
clerk_penny_img = PhotoImage(file=asset_path + '/assets/img/clerkpenny.png')
clerk_penny = GagButton(sos_trp,image=clerk_penny_img, gag=tt_damage_calculator.Gag("Sos", "Clerk Penny", "Trap", 1, 120))
clerk_clara_img = PhotoImage(file=asset_path + '/assets/img/clerkclara.png')
clerk_clara = GagButton(sos_trp,image=clerk_clara_img, gag=tt_damage_calculator.Gag("Sos", "Clerk Clara", "Trap", 2, 180))
sos_snd = Frame(sos_cards)
barb_img = PhotoImage(file=asset_path + '/assets/img/barbaraseville.png')
barb = GagButton(sos_snd,image=barb_img, gag=tt_damage_calculator.Gag("Sos", "Barbara Seville", "Sound", 0, 35))
sid_img = PhotoImage(file=asset_path + '/assets/img/sidsonata.png')
sid = GagButton(sos_snd,image=sid_img, gag=tt_damage_calculator.Gag("Sos", "Sid Sonata", "Sound", 1, 55))
moe_img = PhotoImage(file=asset_path + '/assets/img/moezart.png')
moe = GagButton(sos_snd,image=moe_img, gag=tt_damage_calculator.Gag("Sos", "Moe Zart", "Sound", 2, 75))
sos_drp = Frame(sos_cards)
ned_img = PhotoImage(file=asset_path + '/assets/img/clumsyned.png')
ned = GagButton(sos_drp,image=ned_img, gag=tt_damage_calculator.Gag("Sos", "Clumsy Ned", "Drop", 0, 60))
franz_img = PhotoImage(file=asset_path + '/assets/img/franzneckvein.png')
franz = GagButton(sos_drp,image=franz_img, gag=tt_damage_calculator.Gag("Sos", "Franz Neckvein", "Drop", 1, 100))
bess_img = PhotoImage(file=asset_path + '/assets/img/barnaclebessie.png')
bess = GagButton(sos_drp,image=bess_img, gag=tt_damage_calculator.Gag("Sos", "Barnacle Bessie", "Drop", 2, 170))

### Keybinds
window.bind('<' + settings.keybinds.defense + '>', lambda par: [window.defense_buff.set(tt_damage_calculator.advance_float([0.0,0.1,0.15,0.2,0.25], window.defense_buff.get())), calc_dmg()])
window.bind('<' + settings.keybinds.negative_defense + '>', lambda par: [window.defense_debuff.set(tt_damage_calculator.advance_float([0.0,0.2,0.4,0.5,0.6], window.defense_debuff.get())), calc_dmg()])
window.bind('<' + settings.keybinds.lure + '>', lambda par: [window.lure.set(tt_damage_calculator.toggleswap(window.lure.get())), calc_dmg()])
window.bind('<' + settings.keybinds.lock + '>', lambda par: [window.status_lock.set(tt_damage_calculator.toggleswap(window.status_lock.get())), calc_dmg()])
window.bind('<' + settings.keybinds.pin + '>', lambda par: [window.pinned.set(tt_damage_calculator.toggleswap(window.pinned.get())), window.pin()])

# Organic gag toggle
def organic_toggle(*arg):
  data = tt_damage_calculator.orgswap(organic.get())
  organic.set(data[0])
  window.results.update_org(organic.get())
  for i in gag_btns:
    i.configure(bg=data[2], activebackground=data[3])
org_btn.configure(command=organic_toggle)
window.bind('<' + settings.keybinds.organic + '>', organic_toggle)

# Clear inputs function
def clear_inputs(*arg):
  hist_box.add(tt_damage_calculator.CalculationResults(int(window.results.damage_counter.cget("text")), tt_damage_calculator.lvl_ind(int(window.results.damage_counter.cget("text"))), window.lure.get(), window.defense_buff.get(), window.defense_debuff.get()).build())
  if organic.get():
    organic_toggle()
  window.reset_tracks()
  for i in gag_btns:
    i.configure(text='0')
  if not window.status_lock.get():
    window.reset_vars()
  calc_dmg()
clear_btn.configure(command=clear_inputs)
window.bind('<' + settings.keybinds.reset + '>', clear_inputs)

# Cog HP Cheatsheet Function
def cog_health_calc_hide():
  cog_health_sheet.grid_remove()
  sos_cards.grid_remove()
  window.geometry('')
  cog_calc.configure(text='Show Health and\n SOS Cards', command=cog_health_calc_show)

def cog_health_calc_show():
  cog_health_sheet.grid(column=0, row=3)
  cog_health_lbl.grid(column=0, row=0)
  sos_cards.grid(column=1, row=3)
  cog_calc.configure(text='Hide Health and\n SOS Cards', command=cog_health_calc_hide)
  window.geometry('')
cog_calc.configure(command=cog_health_calc_show)

# Geometry - Main Columns
window.column_0.grid(column=0, row=0, padx=5)
window.column_1.grid(column=1, row=0, padx=10)

# Geometry - Toggles
tog_btns.grid(column=0, row=1, pady=5)
lur_check.grid(column=0, row=0, padx=5)
org_btn.grid(column=1, row=0, padx=5)
clear_btn.grid(column=2, row=0, columnspan=2, padx=5)

# Geometry - Gags
gag_frame.grid(column=0, row=2, pady=10)
snd_frame.grid(column=0, row=1,)
trw_frame.grid(column=0, row=2)
sqt_frame.grid(column=0, row=3)
drp_frame.grid(column=0, row=4)
trp_frame.grid(column=0, row=0)
sos_trp.grid(column=0, row=0)
sos_snd.grid(column=0, row=1)
sos_drp.grid(column=0, row=2)

# Geometry - Calculation History
hist.grid(column=0, row=0)
hist_lbl.grid(column=0, row=0)
hist_box.grid(column=0, row=1)
clear_hist_btn.grid(column=0, row=2, pady=3)
cog_calc.grid(column=0, row=4, pady=3)

# Geometry - Calculation Results
window.results.grid(column=0, row=0)

### Custom Gags ###
global custom_track
custom_track = StringVar()
custom_track.set("Trap")


def cgags():
  global cgags
  def add_custom_gag():
    custom_gag = GagButton(None, None, tt_damage_calculator.Gag("Custom", "Custom " + custom_track.get(), custom_track.get(), 0, int(damage_entry.get(1.0, END))))
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
