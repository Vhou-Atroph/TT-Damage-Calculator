"""
TT-Damage-Calculator
Copyright (C) 2022-2024 Vhou-Atroph
"""
from tkinter import Frame, Text, NORMAL, DISABLED, WORD, END

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