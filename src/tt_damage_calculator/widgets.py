"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph
"""
import os, pathlib, sys
from tkinter import IntVar, BooleanVar, DoubleVar, Tk, Frame, Label, Text, Button, PhotoImage, NORMAL, DISABLED, WORD, END

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

    def __init__(self, parent:GagFrame, image:PhotoImage, gag:tt_damage_calculator.Gag, output:HistoryBox, orgstate:BooleanVar):
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
    
    def press(self, output:HistoryBox, orgstate:bool):
        """Function to execute when Gag Button is pressed."""

        gaginfo = self.gag.button_press(orgstate)
        self.configure(text=int(self.cget("text")) + 1)
        output.add("Gag used: " + gaginfo[1] + " (" + str(gaginfo[0]) + ")\n")
        #TODO: implement gag calculation here

class App(Tk):
    """Class for the gag calculator's full app."""

    def __init__(self):
        Tk.__init__(self)

        # Base
        self.title("Toontown Damage Calculator")
        self.pinned = BooleanVar()
        self.get_asset_path()
        self.settings = tt_damage_calculator.Settings(self.asset_path + "/assets/settings.toml")
        # Tracks / Variables
        self.reset_tracks()
        self.reset_vars()

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

    def reset_vars(self):
        """Resets the program's variables for the next calculation (if desired)."""

        self.org = BooleanVar()
        self.lure = BooleanVar()
        self.buff_defense = DoubleVar()
        self.debuff_defense = DoubleVar()

    def pin(self):
        """Pin or unpin the gag calculator depending on the 'pinned' variable."""

        self.attributes('-topmost', self.pinned.get())
