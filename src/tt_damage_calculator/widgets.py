"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph
"""
import os, pathlib, sys
from tkinter import IntVar, BooleanVar, DoubleVar, Tk, Frame, Label, Text, Button, PhotoImage, Menu, NORMAL, DISABLED, WORD, END

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
        self['command'] = lambda: self.press(output, orgstate.get())
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
        else:
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
    
    def press(self, output:HistoryBox, orgstate:bool):
        """Function to execute when Gag Button is pressed."""

        gaginfo = self.gag.button_press(orgstate)
        self.list().append(gaginfo[0])
        output.add("Gag used: " + gaginfo[1] + " (" + str(gaginfo[0]) + ")\n")
        if self.gag.gtype == "Gag":
            self.configure(text=int(self.cget("text")) + 1)
        #TODO: implement gag calculation here

class App(Tk):
    """Class for the gag calculator's full app."""

    def __init__(self):
        Tk.__init__(self)
        self.title("Toontown Damage Calculator")
        self.pinned = BooleanVar()
        self.status_lock = BooleanVar()
        self.get_asset_path()
        self.reset_tracks()
        self.make_vars()
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

        self.lure = BooleanVar()
        self.defense_buff = DoubleVar()
        self.defense_debuff = DoubleVar()

    def reset_vars(self):
        """Resets battle variables for future calculations."""

        self.lure.set(False)
        self.defense_buff.set(0.0)
        self.defense_debuff.set(0.0)

    def pin(self):
        """Pin or unpin the gag calculator depending on the 'pinned' variable."""
        self.attributes('-topmost', self.pinned.get())

    def toolbar(self):
        """Creates the program's toolbar"""

        toolbar = Menu(self)

        program_menu = Menu(toolbar, tearoff=0)
        program_menu.add_checkbutton(label="Pin window", command=self.pin, variable=self.pinned, onvalue=True, offvalue=False, accelerator="Placeholder")
        program_menu.add_separator()
        program_menu.add_command(label="Exit", command=lambda:window.destroy(), accelerator="Alt-F4")
        toolbar.add_cascade(label="Program", menu=program_menu)

        calculations_menu = Menu(toolbar, tearoff=0)
        def_menu = Menu(calculations_menu, tearoff=0)
        def_menu.add_radiobutton(label="None", value=0.0, variable=self.defense_buff, command=print("unimplemented!"))
        def_menu.add_radiobutton(label="10% (1⭐)", value=0.1, variable=self.defense_buff, command=print("unimplemented!"))
        def_menu.add_radiobutton(label="15% (2⭐)", value=0.15, variable=self.defense_buff, command=print("unimplemented!"))
        def_menu.add_radiobutton(label="20% (3⭐)", value=0.2, variable=self.defense_buff, command=print("unimplemented!"))
        def_menu.add_radiobutton(label="25% (4⭐)", value=0.25, variable=self.defense_buff, command=print("unimplemented!"))
        calculations_menu.add_cascade(label="Cog Defense Up", menu=def_menu)
        def_menu2 = Menu(calculations_menu, tearoff=0)
        def_menu2.add_radiobutton(label="None", value=0.0, variable=self.defense_debuff, command=print("unimplemented!"))
        def_menu2.add_radiobutton(label="-20%", value=0.2, variable=self.defense_debuff, command=print("unimplemented!"))
        def_menu2.add_radiobutton(label="-40%", value=0.4, variable=self.defense_debuff, command=print("unimplemented!"))
        def_menu2.add_radiobutton(label="-50%", value=0.5, variable=self.defense_debuff, command=print("unimplemented!"))
        def_menu2.add_radiobutton(label="-60%", value=0.6, variable=self.defense_debuff, command=print("unimplemented!"))
        calculations_menu.add_cascade(label="Cog Defense Down", menu=def_menu2)
        calculations_menu.add_command(label="Snowball", command=lambda:(use_groupless("Snowball", 1)))
        calculations_menu.add_separator()
        calculations_menu.add_checkbutton(label="Lock Status", variable=self.status_lock, onvalue=True, offvalue=False, accelerator="Placeholder")
        calculations_menu.add_command(label="Custom Gags", command=print("unimplemented!"))
        toolbar.add_cascade(label="Calculations", menu=calculations_menu)

        self.configure(menu=toolbar)
