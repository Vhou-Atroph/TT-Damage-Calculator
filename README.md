# TT-Damage-Calculator
 Gag damage calculator for [Toontown Rewritten](https://toontownrewritten.com/).

![The Program](https://github.com/Vhou-Atroph/TT-Damage-Calculator/blob/main/preview.png?raw=true)

# Usage
**Gag Selection**

Click any gag on the grid to add it to the calculation. 

**Statuses/Modifiers**

Buttons are available above the grid, allowing you to factor in things on calculation, such as a cog being lured that round, organic gags, and cog defense level. Lure and/or Defense can be locked in with the Lock menu, preventing them from resetting when the user clicks on the 'Reset Damage' button. When the organic button is pressed, every gag added subsequently will be calculated as organic. This will be indicated by every gag button turning orange, as well as a text indicator under the calculated damage. Click again to disable this.  

**Other Features**

There are three buttons in the bottom right corner of the program.  
'Clear History' will clear all text in the History panel, which logs previous calculations.  
'Pin to Top' will ensure the program is always on top and visible.  
'Show Health and SOS Cards' brings up a grid of all cog health values from Level 7 to Level 20, as well as the major SOS cards for Trap, Sound, and Drop.  
The latter two buttons can both be toggled off by pressing them a second time.  

The program has various keybinds to expedite calculation:
| Keybind     | Description       |
| ----------- | ----------------- |
| shift       | Toggle Organic    |
| ctrl+d      | Toggle Defense    |
| ctrl+l      | Toggle Lure       |
| ctrl+r      | Reset Calculation |

**NOTE: Version 2.0 Damage Mechanics**
Toontown Rewritten has recently announced and playtested changes to how Version 2.0 Cogs take damage.
As of writing this and adding their functionality to the calculator, they have yet to be added to the game and are still subject to change before release.
Currently, Version 2.0 Cogs take less damage from each separate gag used, reducing the damage values by 2 times the Cog's level, and is presumably subtracted before all other calculations.
Do note that the way their damage calculation works is VERY messy and hard to display with a calculator.
At times, the damage displayed will claim it can defeat a 2.0 Cog of a significantly higher level than it states, or decrease when adding a new gag to the calculation. This is because the damage number is simply a display to make it easier to follow calculations; this damage number is based on the second cog level listed in the V2 damage row, and due to calculations wildly changing between different 2.0 Cog levels this number should NOT be trusted to be exact on any other levels.
You should only fully trust the level listed next to the damage number as a true indicator of whether you can defeat a Cog of that level.
It is also important to remember that, due to carryover no longer being a mechanic, the level displayed for a 2.0 being defeated only refers to the first layer.

# Final Notes
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/I2I65IWZG)
