# TT-Damage-Calculator

 Gag damage calculator for [Toontown Rewritten](https://toontownrewritten.com/).

![The Program](https://github.com/Vhou-Atroph/TT-Damage-Calculator/blob/main/preview.png?raw=true)

## Building

### Prerequisites

Whatever operating system you have, to run the TT-Damage-Calculator from its source, you are required to have both Python and Rust installed. You can download Python at <https://www.python.org/> and Rust at <https://www.rust-lang.org/>. Rust is required to compile the Rust libraries (tt_calc, tt_gags, and tt_settings), and Python is required to run the program itself.

### Windows

To run the program on Windows, you must compile the Rust libraries into .pyd files. To do this, you must first navigate to the main project file (for tt_calc this would be `mod/tt_calc`) and run the command `cargo build --release` in your favorite terminal. The library should then compile.  
Once the file is compiled, the file `mod/[module]/target/release/[module].dll` should have been created. Change the extension to `.pyd` and place the file in `mod/`. This should be done for each Rust library.

### Linux

To run the program on Linux, you must compile the Rust libraries into .so files. To do this, you must first navigate to the main project file (for tt_calc this would be `mod/tt_calc`) and run the command `cargo build --release` in your favorite terminal. The library should then compile.  
Once the file is compiled, the file `mod/[module]/target/release/lib[module].so` should have been created. Change the file's name to `[module].so` and it in `mod/`. This should be done for each Rust library.

## Usage

### Gag Selection

Click any gag on the grid to add it to the calculation.

### Statuses/Modifiers

Buttons are available above the grid, allowing you to factor in things on calculation, such as a cog being lured that round, organic gags, if the cog is a v2, and cog defense level. Lure and/or Defense can be locked in with the Lock menu, preventing them from resetting when the user clicks on the 'Reset Damage' button. When the organic button is pressed, every gag added subsequently will be calculated as organic. This will be indicated by every gag button turning orange, as well as a text indicator under the calculated damage. Click again to disable this.  

### Concerning V2 Damage

V2 damage is weird. There are some levels where certain gag combos seem like they would work on higher cogs, but actually don't because of reinforced plating. An example is 2 regular fogs and 2 regular trunks. While this does 113 damage to level 8 cogs- more than enough damage for level 9 cogs- it will only do 108 damage to level 9 cogs, just under the 110 damage needed to destroy them. The calculator will show damage done to the highest level of v2 cogs defeated when the v2 toggle is active. Be sure to keep this in mind and pay attention to the level indicator rather than the damage number.  
The v2 toggle is not compatible with cog defense. This is because I do not know how the interaction would work and I don't think they would ever interact. If they ever do, screenshot this and make fun of me for it.  

### Other Features

There are three buttons in the bottom right corner of the program.  
'Clear History' will clear all text in the History panel, which logs previous calculations.  
'Pin to Top' will ensure the program is always on top and visible.  
'Show Health and SOS Cards' brings up a grid of all cog health values from Level 7 to Level 20, as well as the major SOS cards for Trap, Sound, and Drop.  
The latter two buttons can both be toggled off by pressing them a second time.  

The program has various keybinds to expedite calculation:
| Keybind     | Description         |
| ----------- | ------------------- |
| shift       | Toggle Organic      |
| ctrl+d      | Toggle Defense      |
| ctrl+l      | Toggle Lure         |
| ctrl+v      | Toggle v2 Calculator|
| ctrl+r      | Reset Calculation   |
| alt+up      | Toggle Pinned Window|

## Final Notes

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/I2I65IWZG)
