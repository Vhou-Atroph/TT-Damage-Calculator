"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph
"""
from tkinter import BooleanVar, Frame, Text, Button, PhotoImage, NORMAL, DISABLED, WORD, END

from . import tt_damage_calculator

class HistoryBox(Text):
    """Class for the History Box widget, a more complicated version of the normal tkinter Text widget."""

    def __init__(self, frame: Frame):
        Text.__init__(self, frame)
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