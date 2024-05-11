"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph
"""

import os, pathlib, platform, sys
from tkinter import IntVar, BooleanVar, DoubleVar, StringVar, Tk, Frame, Label, Text, Button, Checkbutton, OptionMenu, PhotoImage, Menu, Toplevel, NORMAL, DISABLED, WORD, END

from . import tt_damage_calculator

class CalculationResults(Frame):
    """Class for the Calculation Results frame."""

    def __init__(self, parent:Frame):
        Frame.__init__(self, parent)
        self.damage_label = Label(self, text="Damage this round:", font=('Arial', 16, 'normal'))
        self.damage_counter = Label(self, text="0", font=('Arial', 16, 'bold'))
        self.level_counter = Label(self, text="Level 0", font=('Arial', 8, 'normal'))
        self.organic_indicator = Label(self, text="Organic = OFF", font=('Arial', 10, 'bold'))

        self.damage_label.grid(column=0, row=0)
        self.damage_counter.grid(column=1, row=0)
        self.level_counter.grid(column=2, row=0)
        self.organic_indicator.grid(column=0, row=1, columnspan=3)

    def update_org(self, state:bool):
        """Update the organic gag label to be accurate to whatever state the calculator is currently in."""

        if state:
            self.organic_indicator.configure(text="ORGANIC = ON")
        else:
            self.organic_indicator.configure(text="ORGANIC = OFF")

class ToggleButtons(Frame):
    """Class for the Toggle Buttons frame."""

    def __init__(self, window:Tk, parent:Frame):
        Frame.__init__(self, parent)
        self.window = window
        self.organic = Button(self, text="Toggle Organic", font=('Arial', 11, 'normal'), command=self.window.toggle_organic)
        self.lure = Checkbutton(self, text='Cog lured', variable=self.window.lure, onvalue=1, offvalue=0, font=('Arial', 11, 'normal'), command=self.window.calculate)
        self.clear = Button(self, text='Reset damage', font=('Arial', 11, 'normal'), command=self.window.reset_calculation)

        self.organic.grid(column=1, row=0, padx=5)
        self.lure.grid(column=0, row=0, padx=5)
        self.clear.grid(column=2, row=0, columnspan=2, padx=5)

class HistoryBox(Text):
    """Class for the History Box widget, a more complicated version of the normal tkinter Text widget."""

    def __init__(self, parent:Frame):
        Text.__init__(self, parent)
        self['width'] = 25
        self['height'] = 22
        self['state'] = DISABLED
        self['font'] = ('Arial', 10, 'normal')
        self['wrap'] = WORD
    
    def add(self, text:str):
        """Add a line to the start of the History Box."""

        self.configure(state=NORMAL)
        self.insert("1.0", text)
        self.configure(state=DISABLED)
    
    def clear(self):
        """Clear the History Box of text."""

        self.configure(state=NORMAL)
        self.delete("1.0", END)
        self.configure(state=DISABLED)

class HistoryFrame(Frame):
    """Class for the History Frame widget, a frame that contains the calculator's history box, and toggle for cog health and SOS cards."""

    def __init__(self, window:Tk, parent:Frame):
        Frame.__init__(self, parent)
        self.window = window
        self.label = Label(self, text="History")
        self.box = HistoryBox(self)
        self.clear_button = Button(self, text="Clear History", command=self.box.clear)
        self.sos_button = Button(self, text="Show health and\nSOS cards", command=lambda: self.window.bottom.toggle())

        self.label.grid(column=0, row=0)
        self.box.grid(column=0, row=1)
        self.clear_button.grid(column=0, row=2, pady=3)
        self.sos_button.grid(column=0, row=4, pady=3)

class GagFrame(Frame):
    """Class for the Gag Frame widget, a type of frame that automatically places itself in the gag calculator."""

    def __init__(self, parent:Frame, row:int):
        Frame.__init__(self, parent)
        self.grid(row=row, column=0)

class GagButton(Button):
    """Class for the Gag Button widget, a more complicated version of the normal tkinter Button widget."""

    def __init__(self, window:Tk, parent:GagFrame, image:PhotoImage, gag:tt_damage_calculator.Gag):
        Button.__init__(self, parent)
        self.window = window
        self.gag = gag
        self['image'] = image
        self['command'] = lambda: self.press()
        if self.gag.gtype == "Gag":
            self['text'] = "0"
            self['font'] = ('Impress BT', 8, 'bold')
            self['compound'] = 'top'
            self['fg'] = 'white'
            self['activeforeground'] = 'white'
        self.recolor(False)
        if parent:
            self.grid(row=0, column=self.gag.level)
    
    def recolor(self, orgstate:bool):
        """Recolor the Gag Button based on whether or not the gag is a gag (not an SOS) and if organic mode is enabled or not."""

        if self.gag.gtype == "Gag" and orgstate:
            self['bg'] = "darkorange"
            self['activebackground'] = "orange"
        elif self.gag.gtype == "Gag":
            self['bg'] = "#1888D3"
            self['activebackground'] = "#186AD3"

    def list(self):
        """Determines what list a particular gag belongs to."""

        match self.gag.track:
            case "Trap":
                return self.window.trap
            case "Sound":
                return self.window.sound
            case "Throw":
                return self.window.throw
            case "Squirt":
                return self.window.squirt
            case "Drop":
                return self.window.drop
    
    def press(self):
        """Function to execute when Gag Button is pressed."""

        gaginfo = self.gag.button_press(self.window.organic.get())
        self.list().append(gaginfo[0])
        self.window.history.box.add("Gag used: " + gaginfo[1] + " (" + str(gaginfo[0]) + ")\n")
        if self.gag.gtype == "Gag":
            self.configure(text=int(self.cget("text")) + 1)
        self.window.calculate()

class Gags(Frame):
    """Class for gag buttons and their frames."""

    def __init__(self, window:Tk, parent:Frame):
        Frame.__init__(self, parent)
        self.window = window

        self.trap = GagFrame(self, 0)
        self.banana_peel_image = PhotoImage(file=self.window.asset_path + "/assets/img/banana-peel.png")
        self.banana_peel = GagButton(self.window, self.trap, image=self.banana_peel_image, gag=tt_damage_calculator.Gag("Gag", "Banana Peel", "Trap", 0, 12))
        self.rake_image = PhotoImage(file=self.window.asset_path + "/assets/img/rake.png")
        self.rake = GagButton(self.window, self.trap, image=self.rake_image, gag=tt_damage_calculator.Gag("Gag", "Rake", "Trap", 1, 18))
        self.marbles_image = PhotoImage(file=self.window.asset_path + "/assets/img/marbles.png")
        self.marbles = GagButton(self.window, self.trap, image=self.marbles_image, gag=tt_damage_calculator.Gag("Gag", "Marbles", "Trap", 2, 35))
        self.quicksand_image = PhotoImage(file=self.window.asset_path + "/assets/img/quicksand.png")
        self.quicksand = GagButton(self.window, self.trap, image=self.quicksand_image, gag=tt_damage_calculator.Gag("Gag", "Quicksand", "Trap", 3, 50))
        self.trapdoor_image = PhotoImage(file=self.window.asset_path + "/assets/img/trapdoor.png")
        self.trapdoor = GagButton(self.window, self.trap, image=self.trapdoor_image, gag=tt_damage_calculator.Gag("Gag", "Trapdoor", "Trap", 4, 85))
        self.tnt_image = PhotoImage(file=self.window.asset_path + "/assets/img/tnt.png")
        self.tnt = GagButton(self.window, self.trap, image=self.tnt_image, gag=tt_damage_calculator.Gag("Gag", "TNT", "Trap", 5, 180))
        self.railroad_image = PhotoImage(file=self.window.asset_path + "/assets/img/railroad.png")
        self.railroad = GagButton(self.window, self.trap, image=self.railroad_image, gag=tt_damage_calculator.Gag("Gag", "Railroad", "Trap", 6, 200))

        self.sound = GagFrame(self, 1)
        self.bike_horn_image = PhotoImage(file=self.window.asset_path + "/assets/img/bike-horn.png")
        self.bike_horn = GagButton(self.window, self.sound, image=self.bike_horn_image, gag=tt_damage_calculator.Gag("Gag", "Bike Horn", "Sound", 0, 4))
        self.whistle_image = PhotoImage(file=self.window.asset_path + "/assets/img/whistle.png")
        self.whistle = GagButton(self.window, self.sound, image=self.whistle_image, gag=tt_damage_calculator.Gag("Gag", "Whistle", "Sound", 1, 7))
        self.bugle_image = PhotoImage(file=self.window.asset_path + "/assets/img/bugle.png")
        self.bugle = GagButton(self.window, self.sound, image=self.bugle_image, gag=tt_damage_calculator.Gag("Gag", "Bugle", "Sound", 2, 11))
        self.aoogah_image = PhotoImage(file=self.window.asset_path + "/assets/img/aoogah.png")
        self.aoogah = GagButton(self.window, self.sound, image=self.aoogah_image, gag=tt_damage_calculator.Gag("Gag", "Aoogah", "Sound", 3, 16))
        self.elephant_trunk_image = PhotoImage(file=self.window.asset_path + "/assets/img/elephant-trunk.png")
        self.elephant_trunk = GagButton(self.window, self.sound, image=self.elephant_trunk_image, gag=tt_damage_calculator.Gag("Gag", "Elephant Trunk", "Sound", 4, 21))
        self.foghorn_image = PhotoImage(file=self.window.asset_path + "/assets/img/fog-horn.png")
        self.foghorn = GagButton(self.window, self.sound, image=self.foghorn_image, gag=tt_damage_calculator.Gag("Gag", "Fog Horn", "Sound", 5, 50))
        self.opera_image = PhotoImage(file=self.window.asset_path + "/assets/img/opera-singer.png")
        self.opera = GagButton(self.window, self.sound, image=self.opera_image, gag=tt_damage_calculator.Gag("Gag", "Opera Singer", "Sound", 6, 90))

        self.throw = GagFrame(self, 2)
        self.cupcake_image = PhotoImage(file=self.window.asset_path + "/assets/img/cupcake.png")
        self.cupcake = GagButton(self.window, self.throw, image=self.cupcake_image, gag=tt_damage_calculator.Gag("Gag", "Cupcake", "Throw", 0, 6))
        self.fruit_pie_slice_image = PhotoImage(file=self.window.asset_path + "/assets/img/fruit-pie-slice.png")
        self.fruit_pie_slice = GagButton(self.window, self.throw, image=self.fruit_pie_slice_image, gag=tt_damage_calculator.Gag("Gag", "Fruit Pie Slice", "Throw", 1, 10))
        self.cream_pie_slice_image = PhotoImage(file=self.window.asset_path + "/assets/img/cream-pie-slice.png")
        self.cream_pie_slice = GagButton(self.window, self.throw, image=self.cream_pie_slice_image, gag=tt_damage_calculator.Gag("Gag", "Cream Pie Slice", "Throw", 2, 17))
        self.whole_fruit_pie_image = PhotoImage(file=self.window.asset_path + "/assets/img/whole-fruit-pie.png")
        self.whole_fruit_pie = GagButton(self.window, self.throw, image=self.whole_fruit_pie_image, gag=tt_damage_calculator.Gag("Gag", "Whole Fruit Pie", "Throw", 3, 27))
        self.whole_cream_pie_image = PhotoImage(file=self.window.asset_path + "/assets/img/whole-cream-pie.png")
        self.whole_cream_pie = GagButton(self.window, self.throw, image=self.whole_cream_pie_image, gag=tt_damage_calculator.Gag("Gag", "Whole Cream Pie", "Throw", 4, 40))
        self.birthday_cake_image = PhotoImage(file=self.window.asset_path + "/assets/img/birthday-cake.png")
        self.birthday_cake = GagButton(self.window, self.throw, image=self.birthday_cake_image, gag=tt_damage_calculator.Gag("Gag", "Birthday Cake", "Throw", 5, 100))
        self.wedding_cake_image = PhotoImage(file=self.window.asset_path + "/assets/img/wedding-cake.png")
        self.wedding_cake = GagButton(self.window, self.throw, image=self.wedding_cake_image, gag=tt_damage_calculator.Gag("Gag", "Wedding Cake", "Throw", 6, 120))

        self.squirt = GagFrame(self, 3)
        self.squirting_flower_image = PhotoImage(file=self.window.asset_path + "/assets/img/squirting-flower.png")
        self.squirting_flower = GagButton(self.window, self.squirt, image=self.squirting_flower_image, gag=tt_damage_calculator.Gag("Gag", "Squirting Flower", "Squirt", 0, 4))
        self.glass_of_water_image = PhotoImage(file=self.window.asset_path + "/assets/img/glass-of-water.png")
        self.glass_of_water = GagButton(self.window, self.squirt, image=self.glass_of_water_image, gag=tt_damage_calculator.Gag("Gag", "Glass of Water", "Squirt", 1, 8))
        self.squirt_gun_image = PhotoImage(file=self.window.asset_path + "/assets/img/squirt-gun.png")
        self.squirt_gun = GagButton(self.window, self.squirt, image=self.squirt_gun_image, gag=tt_damage_calculator.Gag("Gag", "Squirt Gun", "Squirt", 2, 12))
        self.seltzer_bottle_image = PhotoImage(file=self.window.asset_path + "/assets/img/seltzer-bottle.png")
        self.seltzer_bottle = GagButton(self.window, self.squirt, image=self.seltzer_bottle_image, gag=tt_damage_calculator.Gag("Gag", "Seltzer Bottle", "Squirt", 3, 21))
        self.firehose_image = PhotoImage(file=self.window.asset_path + "/assets/img/fire-hose.png")
        self.firehose = GagButton(self.window, self.squirt, image=self.firehose_image, gag=tt_damage_calculator.Gag("Gag", "Fire Hose", "Squirt", 4, 30))
        self.storm_cloud_image = PhotoImage(file=self.window.asset_path + "/assets/img/storm-cloud.png")
        self.storm_cloud = GagButton(self.window, self.squirt, image=self.storm_cloud_image, gag=tt_damage_calculator.Gag("Gag", "Storm Cloud", "Squirt", 5, 80))
        self.geyser_image = PhotoImage(file=self.window.asset_path + "/assets/img/geyser.png")
        self.geyser = GagButton(self.window, self.squirt, image=self.geyser_image, gag=tt_damage_calculator.Gag("Gag", "Geyser", "Squirt", 6, 105))

        self.drop = GagFrame(self, 4)
        self.flowerpot_image = PhotoImage(file=self.window.asset_path + "/assets/img/flower-pot.png")
        self.flowerpot = GagButton(self.window, self.drop, image=self.flowerpot_image, gag=tt_damage_calculator.Gag("Gag", "Flower Pot", "Drop", 0, 10))
        self.sandbag_image = PhotoImage(file=self.window.asset_path + "/assets/img/sandbag.png")
        self.sandbag = GagButton(self.window, self.drop, image=self.sandbag_image, gag=tt_damage_calculator.Gag("Gag", "Sandbag", "Drop", 1, 18))
        self.anvil_image = PhotoImage(file=self.window.asset_path + "/assets/img/anvil.png")
        self.anvil = GagButton(self.window, self.drop, image=self.anvil_image, gag=tt_damage_calculator.Gag("Gag", "Anvil", "Drop", 2, 30))
        self.big_weight_image = PhotoImage(file=self.window.asset_path + "/assets/img/big-weight.png")
        self.big_weight = GagButton(self.window, self.drop, image=self.big_weight_image, gag=tt_damage_calculator.Gag("Gag", "Big Weight", "Drop", 3, 45))
        self.safe_image = PhotoImage(file=self.window.asset_path + "/assets/img/safe.png")
        self.safe = GagButton(self.window, self.drop, image=self.safe_image, gag=tt_damage_calculator.Gag("Gag", "Safe", "Drop", 4, 70))
        self.grand_piano_image = PhotoImage(file=self.window.asset_path + "/assets/img/grand-piano.png")
        self.grand_piano = GagButton(self.window, self.drop, image=self.grand_piano_image, gag=tt_damage_calculator.Gag("Gag", "Grand Piano", "Drop", 5, 170))
        self.toontanic_image = PhotoImage(file=self.window.asset_path + "/assets/img/toontanic.png")
        self.toontanic = GagButton(self.window, self.drop, image=self.toontanic_image, gag=tt_damage_calculator.Gag("Gag", "Toontanic", "Drop", 6, 180))

        self.list= [
            self.banana_peel, self.rake, self.marbles, self.quicksand, self.trapdoor, self.tnt, self.railroad,
            self.bike_horn, self.whistle, self.bugle, self.aoogah, self.elephant_trunk, self.foghorn, self.opera,
            self.cupcake, self.fruit_pie_slice, self.cream_pie_slice, self.whole_fruit_pie, self.whole_cream_pie, self.birthday_cake, self.wedding_cake,
            self.squirting_flower, self.glass_of_water, self.squirt_gun, self.seltzer_bottle, self.firehose, self.storm_cloud, self.geyser,
            self.flowerpot, self.sandbag, self.anvil, self.big_weight, self.safe, self.grand_piano, self.toontanic
            ]

class CogHealth(Frame):
    """Class for the Cog Health cheat sheet frame."""

    def __init__(self, window:Tk):
        Frame.__init__(self, window)
        self.image = PhotoImage(file=window.asset_path + '/assets/img/coghp.png')
        self.label = Label(self, image=self.image)

        self.label.grid(column=0, row=0)

class SosCards(Frame):
    """Class for the SOS cards frame."""

    def __init__(self, window:Tk):
        Frame.__init__(self, window)

        self.trap = GagFrame(self, 0)
        self.clerk_will_image = PhotoImage(file=window.asset_path + "/assets/img/clerkwill.png")
        self.clerk_will = GagButton(window, self.trap, image=self.clerk_will_image, gag=tt_damage_calculator.Gag("Sos", "Clerk Will", "Trap", 0, 60))
        self.clerk_penny_image = PhotoImage(file=window.asset_path + "/assets/img/clerkpenny.png")
        self.clerk_penny = GagButton(window, self.trap, image=self.clerk_penny_image, gag=tt_damage_calculator.Gag("Sos", "Clerk Penny", "Trap", 1, 120))
        self.clerk_clara_image = PhotoImage(file=window.asset_path + "/assets/img/clerkclara.png")
        self.clerk_clara = GagButton(window, self.trap, image=self.clerk_clara_image, gag=tt_damage_calculator.Gag("Sos", "Clerk Clara", "Trap", 2, 180))

        self.sound = GagFrame(self, 1)
        self.barbara_seville_image = PhotoImage(file=window.asset_path + "/assets/img/barbaraseville.png")
        self.barbara_seville = GagButton(window, self.sound ,image=self.barbara_seville_image, gag=tt_damage_calculator.Gag("Sos", "Barbara Seville", "Sound", 0, 35))
        self.sid_sonata_image = PhotoImage(file=window.asset_path + "/assets/img/sidsonata.png")
        self.sid_sonata = GagButton(window, self.sound, image=self.sid_sonata_image, gag=tt_damage_calculator.Gag("Sos", "Sid Sonata", "Sound", 1, 55))
        self.moe_zart_image = PhotoImage(file=window.asset_path + "/assets/img/moezart.png")
        self.moe_zart = GagButton(window, self.sound, image=self.moe_zart_image, gag=tt_damage_calculator.Gag("Sos", "Moe Zart", "Sound", 2, 75))

        self.drop = GagFrame(self, 2)
        self.clumsy_ned_image = PhotoImage(file=window.asset_path + "/assets/img/clumsyned.png")
        self.clumsy_ned = GagButton(window, self.drop, image=self.clumsy_ned_image, gag=tt_damage_calculator.Gag("Sos", "Clumsy Ned", "Drop", 0, 60))
        self.franz_neckvein_img = PhotoImage(file=window.asset_path + "/assets/img/franzneckvein.png")
        self.franz_neckvein = GagButton(window, self.drop, image=self.franz_neckvein_img, gag=tt_damage_calculator.Gag("Sos", "Franz Neckvein", "Drop", 1, 100))
        self.barnacle_bessie_image = PhotoImage(file=window.asset_path + "/assets/img/barnaclebessie.png")
        self.barnacle_bessie = GagButton(window, self.drop, image=self.barnacle_bessie_image, gag=tt_damage_calculator.Gag("Sos", "Barnacle Bessie", "Drop", 2, 170))

class HideableBottom():
    """Class that allows the visibility of the HP cheat sheet and SOS Cards to be toggled on or off."""

    def __init__(self, window:Tk):
        self.window = window
        self.coghp = CogHealth(self.window)
        self.sos = SosCards(self.window)
        self.visible = False

    def toggle(self):
        """Toggles the visibility of the bottom."""

        if self.visible:
            self.coghp.grid_remove()
            self.sos.grid_remove()
            self.window.history.sos_button.configure(text='Show Health and\n SOS Cards')
        else:
            self.coghp.grid(column=0, row=3)
            self.sos.grid(column=1, row=3)
            self.window.history.sos_button.configure(text='Hide Health and\n SOS Cards')
        self.visible = tt_damage_calculator.toggleswap(self.visible)
        self.window.geometry('')

class CustomGags(Toplevel):
    """Class for the Custom Gags Toplevel widget."""

    def __init__(self, window:Tk):
        Toplevel.__init__(self, window)
        self.window = window
        self.track = StringVar()
        self.track.set("Trap")
        self.title = "Custom Gag Entry"
        self.resizable(0, 0)
        self.wm_transient(self.window)
        self.build_ui()

    def add(self):
        """Add a custom gag to the calculation."""

        GagButton(self.window, None, None, tt_damage_calculator.Gag("Custom", "Custom " + self.track.get(), self.track.get(), 0, int(self.damage.get(1.0, END)))).press()

    def build_ui(self):
        """Builds the UI for the custom gags widget."""

        self.damage_label = Label(self, text="Damage", font=('Arial', 11, 'normal'))
        self.damage = Text(self, width=10, height=1, font=('Arial', 11, 'normal'))
        self.gag_label = Label(self, text="Gag Track", font=('Arial', 11, 'normal'))
        self.gag_dropdown = OptionMenu(self, self.track, *["Trap", "Sound", "Throw", "Squirt", "Drop"])
        self.button = Button(self, text="Add to Calculation", font=('Arial', 11, 'normal'), command=self.add)
        self.damage_label.grid(column=0, row=0, pady=3, padx=2)
        self.damage.grid(column=1, row=0, pady=3, padx=2)
        self.gag_label.grid(column=0, row=1, pady=3, padx=2)
        self.gag_dropdown.grid(column=1, row=1, pady=3, padx=2)
        self.button.grid(column=0, row=2, columnspan=2, pady=8, padx=25)

class App(Tk):
    """Class for the gag calculator's full app."""

    def __init__(self):
        Tk.__init__(self)
        self.title("Toontown Damage Calculator")
        self.resizable(0,0)
        self.pinned = BooleanVar()
        self.status_lock = BooleanVar()
        self.get_asset_path()
        self.reset_tracks()
        self.make_vars()
        self.settings = tt_damage_calculator.Settings(self.asset_path + "/assets/settings.toml")
        self.build_ui()
        self.toolbar()
        self.keybinds()
        self.iconphoto(True, self.gags.whole_cream_pie_image)

    def get_asset_path(self):
        """Gets the asset path for the program."""

        self.asset_path = str(pathlib.Path(__file__).parent.resolve())
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            self.asset_path = os.getcwd()

    def reset_tracks(self):
        """Empties the track lists and sets nogroup to 0 for the next calculation."""

        self.trap = []
        self.sound = []
        self.throw = []
        self.squirt = []
        self.drop = []
        self.nogroup = IntVar()

    def make_vars(self):
        """Creates battle variables used in calculation. This will not reset the variables properly; use reset_vars() instead."""

        self.organic = BooleanVar()
        self.lure = BooleanVar()
        self.defense_buff = DoubleVar()
        self.defense_debuff = DoubleVar()

    def reset_vars(self):
        """Resets battle variables for future calculations."""

        self.lure.set(False)
        self.defense_buff.set(0.0)
        self.defense_debuff.set(0.0)

    def toggle_organic(self):
        """Toggles the organic variable"""

        self.organic.set(tt_damage_calculator.toggleswap(self.organic.get()))
        self.results.update_org(self.organic.get())
        for i in self.gags.list:
            i.recolor(self.organic.get())

    def add_nogroup(self, gag:str, damage:int):
        """Add gags that do not do group (or lure) bonus damage to the calculation."""

        self.nogroup.set(self.nogroup.get() + damage)
        self.history.box.add("Gag used: " + gag + " (" + str(damage) + ")\n")
        self.calculate()

    def calculate(self):
        """Updates the damage total according to the gags used during the current calculation."""

        damage = tt_damage_calculator.full_calc(self.trap, self.sound, self.throw, self.squirt, self.drop, self.nogroup.get(), self.lure.get(), self.defense_buff.get(), self.defense_debuff.get())
        self.results.damage_counter.configure(text=str(damage))
        self.results.level_counter.configure(text=tt_damage_calculator.lvl_ind_string(tt_damage_calculator.lvl_ind(damage), int(self.defense_buff.get() * 100), int(self.defense_debuff.get() * 100)))

    def reset_calculation(self):
        """Resets the current calculation."""

        self.history.box.add(tt_damage_calculator.CalculationResults(int(self.results.damage_counter.cget("text")), tt_damage_calculator.lvl_ind(int(self.results.damage_counter.cget("text"))), self.lure.get(), self.defense_buff.get(), self.defense_debuff.get()).build())
        if not self.status_lock.get():
            self.reset_vars()
            if self.organic.get():
                self.toggle_organic()
        self.reset_tracks()
        for i in self.gags.list:
            i.configure(text="0")
        self.calculate()

    def pin(self):
        """Pin or unpin the gag calculator depending on the 'pinned' variable."""

        self.attributes('-topmost', self.pinned.get())

    def build_ui(self):
        """Builds the UI for the calculator."""

        self.column_0 = Frame(self)
        self.column_1 = Frame(self)

        self.results = CalculationResults(self.column_0)
        self.toggles = ToggleButtons(self, self.column_0)
        self.gags = Gags(self, self.column_0)

        self.history = HistoryFrame(self, self.column_1)

        self.bottom = HideableBottom(self)

        self.column_0.grid(column=0, row=0, padx=5)
        self.column_1.grid(column=1, row=0, padx=10)
        self.toggles.grid(column=0, row=1, pady=5)
        self.gags.grid(column=0, row=2, pady=10)
        self.history.grid(column=0, row=0)
        self.results.grid(column=0, row=0)

    def custom_gags(self):
        """Opens the custom gags toplevel."""

        self.custom_gags_widget = CustomGags(self)

    def file(self, filepath):
        """Open a specified file in its default app."""

        match platform.system():
            case "Windows":
                os.startfile(filepath)
            case "Darwin":
                os.system(("open " + filepath))
            case "Linux":
                os.system(("xdg-open " + filepath))

    def toolbar(self):
        """Creates the program's toolbar."""

        toolbar = Menu(self)

        program_menu = Menu(toolbar, tearoff=0)
        program_menu.add_command(label="Settings", command=lambda:self.file(self.asset_path + "/assets/settings.toml"))
        program_menu.add_checkbutton(label="Pin window", command=self.pin, variable=self.pinned, onvalue=True, offvalue=False, accelerator=self.settings.keybinds.pin)
        program_menu.add_separator()
        program_menu.add_command(label="Exit", command=lambda:window.destroy(), accelerator="Alt-F4")
        toolbar.add_cascade(label="Program", menu=program_menu)

        calculations_menu = Menu(toolbar, tearoff=0)
        def_menu = Menu(calculations_menu, tearoff=0)
        def_menu.add_radiobutton(label="None", value=0.0, variable=self.defense_buff, command=self.calculate)
        def_menu.add_radiobutton(label="10% (1⭐)", value=0.1, variable=self.defense_buff, command=self.calculate)
        def_menu.add_radiobutton(label="15% (2⭐)", value=0.15, variable=self.defense_buff, command=self.calculate)
        def_menu.add_radiobutton(label="20% (3⭐)", value=0.2, variable=self.defense_buff, command=self.calculate)
        def_menu.add_radiobutton(label="25% (4⭐)", value=0.25, variable=self.defense_buff, command=self.calculate)
        calculations_menu.add_cascade(label="Cog Defense Up", menu=def_menu)
        def_menu2 = Menu(calculations_menu, tearoff=0)
        def_menu2.add_radiobutton(label="None", value=0.0, variable=self.defense_debuff, command=self.calculate)
        def_menu2.add_radiobutton(label="-20%", value=0.2, variable=self.defense_debuff, command=self.calculate)
        def_menu2.add_radiobutton(label="-40%", value=0.4, variable=self.defense_debuff, command=self.calculate)
        def_menu2.add_radiobutton(label="-50%", value=0.5, variable=self.defense_debuff, command=self.calculate)
        def_menu2.add_radiobutton(label="-60%", value=0.6, variable=self.defense_debuff, command=self.calculate)
        calculations_menu.add_cascade(label="Cog Defense Down", menu=def_menu2)
        calculations_menu.add_command(label="Snowball", command=lambda: self.add_nogroup("Snowball", 1))
        calculations_menu.add_separator()
        calculations_menu.add_checkbutton(label="Lock Status", variable=self.status_lock, onvalue=True, offvalue=False, accelerator=self.settings.keybinds.lock)
        calculations_menu.add_command(label="Custom Gags", command=lambda: self.custom_gags())
        toolbar.add_cascade(label="Calculations", menu=calculations_menu)

        self.configure(menu=toolbar)

    def keybinds(self):
        """Creates the program's keybinds."""

        self.bind('<' + self.settings.keybinds.defense + '>', lambda par: [self.defense_buff.set(tt_damage_calculator.advance_float([0.0,0.1,0.15,0.2,0.25], self.defense_buff.get())), self.calculate()])
        self.bind('<' + self.settings.keybinds.negative_defense + '>', lambda par: [self.defense_debuff.set(tt_damage_calculator.advance_float([0.0,0.2,0.4,0.5,0.6], self.defense_debuff.get())), self.calculate()])
        self.bind('<' + self.settings.keybinds.lure + '>', lambda par: [self.lure.set(tt_damage_calculator.toggleswap(self.lure.get())), self.calculate()])
        self.bind('<' + self.settings.keybinds.lock + '>', lambda par: [self.status_lock.set(tt_damage_calculator.toggleswap(self.status_lock.get())), self.calculate()])
        self.bind('<' + self.settings.keybinds.pin + '>', lambda par: [self.pinned.set(tt_damage_calculator.toggleswap(self.pinned.get())), self.pin()])
        self.bind('<' + self.settings.keybinds.organic + '>', lambda par: [self.toggle_organic()])
        self.bind('<' + self.settings.keybinds.reset + '>', lambda par: [self.reset_calculation()])

    def run(self):
        """Run the app."""

        self.mainloop()
