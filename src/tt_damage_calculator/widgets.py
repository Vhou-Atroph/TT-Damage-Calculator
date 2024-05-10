"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph
"""
import os, pathlib, platform, sys
from tkinter import IntVar, BooleanVar, DoubleVar, Tk, Frame, Label, Text, Button, Checkbutton, PhotoImage, Menu, NORMAL, DISABLED, WORD, END

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
        self.lure = Checkbutton(self, text='Cog lured', variable=self.window.lure, onvalue=1, offvalue=0, font=('Arial', 11, 'normal'), command=window.calculate)
        self.clear = Button(self, text='Reset damage', font=('Arial', 11, 'normal'))

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

    def __init__(self, parent:Frame):
        Frame.__init__(self, parent)
        self.label = Label(self, text="History")
        self.box = HistoryBox(self)
        self.clear_button = Button(self, text="Clear History", command=self.box.clear)
        self.sos_button = Button(self, text="Show health and\nSOS cards", command=print("unimplemented!"))

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
        self.window = window
        self.gag = gag
        Button.__init__(self, parent)
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
        self.clerk_will_image = PhotoImage(file=window.asset_path + '/assets/img/clerkwill.png')
        self.clerk_will = GagButton(window, self.trap, image=self.clerk_will_image, gag=tt_damage_calculator.Gag("Sos", "Clerk Will", "Trap", 0, 60))
        self.clerk_penny_image = PhotoImage(file=window.asset_path + '/assets/img/clerkpenny.png')
        self.clerk_penny = GagButton(window, self.trap, image=self.clerk_penny_image, gag=tt_damage_calculator.Gag("Sos", "Clerk Penny", "Trap", 1, 120))
        self.clerk_clara_image = PhotoImage(file=window.asset_path + '/assets/img/clerkclara.png')
        self.clerk_clara = GagButton(window, self.trap, image=self.clerk_clara_image, gag=tt_damage_calculator.Gag("Sos", "Clerk Clara", "Trap", 2, 180))

        self.sound = GagFrame(self, 1)
        self.barbara_seville_image = PhotoImage(file=window.asset_path + '/assets/img/barbaraseville.png')
        self.barbara_seville = GagButton(window, self.sound ,image=self.barbara_seville_image, gag=tt_damage_calculator.Gag("Sos", "Barbara Seville", "Sound", 0, 35))
        self.sid_sonata_image = PhotoImage(file=window.asset_path + '/assets/img/sidsonata.png')
        self.sid_sonata = GagButton(window, self.sound, image=self.sid_sonata_image, gag=tt_damage_calculator.Gag("Sos", "Sid Sonata", "Sound", 1, 55))
        self.moe_zart_image = PhotoImage(file=window.asset_path + '/assets/img/moezart.png')
        self.moe_zart = GagButton(window, self.sound, image=self.moe_zart_image, gag=tt_damage_calculator.Gag("Sos", "Moe Zart", "Sound", 2, 75))

        self.drop = GagFrame(self, 2)
        self.clumsy_ned_image = PhotoImage(file=window.asset_path + '/assets/img/clumsyned.png')
        self.clumsy_ned = GagButton(window, self.drop, image=self.clumsy_ned_image, gag=tt_damage_calculator.Gag("Sos", "Clumsy Ned", "Drop", 0, 60))
        self.franz_neckvein_img = PhotoImage(file=window.asset_path + '/assets/img/franzneckvein.png')
        self.franz_neckvein = GagButton(window, self.drop, image=self.franz_neckvein_img, gag=tt_damage_calculator.Gag("Sos", "Franz Neckvein", "Drop", 1, 100))
        self.barnacle_bessie_image = PhotoImage(file=window.asset_path + '/assets/img/barnaclebessie.png')
        self.barnacle_bessie = GagButton(window, self.drop, image=self.barnacle_bessie_image, gag=tt_damage_calculator.Gag("Sos", "Barnacle Bessie", "Drop", 2, 170))

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
        self.build_ui()
        self.toolbar()

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
        #TODO: Recolor buttons

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

    def pin(self):
        """Pin or unpin the gag calculator depending on the 'pinned' variable."""

        self.attributes('-topmost', self.pinned.get())

    def build_ui(self):
        """Builds the UI for the calculator."""

        self.column_0 = Frame(self)
        self.column_1 = Frame(self)

        self.results = CalculationResults(self.column_0)
        self.toggles = ToggleButtons(self, self.column_0)

        self.history = HistoryFrame(self.column_1)

        self.coghp = CogHealth(self)
        self.sos = SosCards(self)

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
        program_menu.add_checkbutton(label="Pin window", command=self.pin, variable=self.pinned, onvalue=True, offvalue=False, accelerator="Placeholder")
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
        calculations_menu.add_checkbutton(label="Lock Status", variable=self.status_lock, onvalue=True, offvalue=False, accelerator="Placeholder")
        calculations_menu.add_command(label="Custom Gags", command=print("unimplemented!"))
        toolbar.add_cascade(label="Calculations", menu=calculations_menu)

        self.configure(menu=toolbar)
