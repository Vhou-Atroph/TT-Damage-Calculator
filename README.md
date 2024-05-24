# ![TT-Damage-Calculator](wiki/headerfooter.png)

![Badge showing the current workflow status of the Toontown Damage Calculator](https://img.shields.io/github/actions/workflow/status/Vhou-Atroph/TT-Damage-Calculator/ci.yml) [![Badge showing the latest release of the Toontown Damage Calculator.](https://img.shields.io/github/v/release/Vhou-Atroph/TT-Damage-Calculator)](https://github.com/Vhou-Atroph/TT-Damage-Calculator/releases/latest) ![Badge showing the license of the Toontown Damage Calculator.](https://img.shields.io/github/license/Vhou-Atroph/TT-Damage-Calculator) ![Badge showing the number of downloads the Toontown Damage Calculator has received.](https://img.shields.io/github/downloads/Vhou-Atroph/TT-Damage-Calculator/total)

 Gag damage calculator for [Toontown Rewritten](https://toontownrewritten.com/).

![The Program](wiki/preview.png)

## Downloading

### Windows, Linux, and MacOS Executable

The executable version of the calculator requires the least setup, and is highly portable with the limitation that it only easily works on devices running the required operating system. You can find a download for the latest version of the executable either at <https://github.com/Vhou-Atroph/TT-Damage-Calculator/releases/latest/> on GitHub, or at <https://vhou.gloop.group/projects/gagcalc> near the bottom of the page.

The downloaded archive should contain the executable, a [LICENSE](LICENSE) file, and the assets folder. Once you extract the zip file to your preferred directory, the calculator should run normally!

`Note: The MacOS executable version of the gag calculator may not work properly, as it is untested due to a lack of access to the relevant hardware.`

#### Linux Executable

The Linux executable is compiled on an Ubuntu Github Actions runner, but the application should work on any distribution that uses glibc.

![TT-Damage-Calculator running on Arch Linux](wiki/arch.png)

### Python Package

Downloading the Toontown Damage Calculator as a Python package will require [downloading the Python programming language](https://www.python.org/downloads/) and [pipx](https://pipx.pypa.io/stable/installation/). Once this is done, you can open your command terminal and run the following command:

```shell
pipx install tt_damage_calculator
```

If you don't want to use pipx, `pip install tt_damage_calculator` should also work.

This will install the calculator as a Python package to your computer. You can run the calculator from the command line by inputting one of the following commands into your terminal:

```shell
tt-damage-calculator
tt_damage_calculator
```

If you are unable to download the calculator via pip for your system, you will need to build it yourself by following the [Building: Wheels (All Platforms)](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Building:-Wheels-(All-Platforms)) guide on the wiki.

#### On Linux and MacOS

On certain Linux distributions and MacOS, your installation of Python may not come with tkinter, which will greatly restrict your ability to run the program (you won't be able to). You can fix this with one of the below commands:

```shell
sudo apt-get install python3-tk # Debian based distributions
sudo dnf install python3-tkinter # Fedora based distributions
sudo yum install python3-tkinter # RHEL based distributions
sudo pacman -Syu tk # Arch based distributions
sudo zypper in python-tk # openSUSE based distributions
sudo xbps-install python3-tkinter # Void based distributions
brew install python-tk # MacOS
```

For other distributions, you will need to consult your wikis:

- [Gentoo](https://wiki.gentoo.org/wiki/Tkinter)
- [NixOS](https://nixos.wiki/wiki/Python)

### Arch User Repository

If you use an Arch-based Linux distribution, you can download the calculator through the [AUR](https://aur.archlinux.org/)! To do so, you can run the following commands through your terminal:

```shell
git clone https://aur.archlinux.org/tt-damage-calculator.git
cd tt-damage-calculator
makepkg -si
```

Alternatively, you can use an AUR helper to install the package. Once it is installed, you will be able to run the program on the command line just as if you downloaded it as a Python package:

```shell
tt-damage-calculator
```

## Building

There are guides on the [repository's wiki](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki) for building the calculator:

- [Building: Wheels (All Platforms)](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Building:-Wheels-(All-Platforms))
- [Building: Linux](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Building:-Linux)
- [Building: MacOS Executable](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Building:-MacOS-Executable)
- [Building: Windows Executable](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Building:-Windows-Executable)
- [Building: Github Actions](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Building:-Github-Actions)

## Usage

The [TT-Damage-Calculator wiki](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki) has several guides on the usage of the program:

- [Usage: Defense](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Usage:-Defense)
- [Usage: Gags](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Usage:-Gags)
- [Usage: History](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Usage:-History)
- [Usage: Keybinds](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Usage:-Keybinds)
- [Usage: Lock Status](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Usage:-Lock-Status)
- [Usage: Lure](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Usage:-Lure)

### Gag Selection

Click any gag on the grid to add it to the calculation.

### Statuses/Modifiers

There are three buttons available above the gag selection that allow for certain functionalities: if a cog being lured that round, whether a gag is organic or not, and the ability to reset the current calculation. Other cog modifiers such as defense can be found in the menu bar under "Calculations."

### Other Features

There are two buttons in the bottom right corner of the program.  
'Clear History' will clear all text in the History panel, which logs previous calculations.  
'Show Health and SOS Cards' brings up a grid of all cog health values from Level 7 to Level 20, as well as the major SOS cards for Trap, Sound, and Drop. This can be toggled by clicking on it a second time.

The program has various keybinds to expedite calculation:

| Keybind     | Description             |
| ----------- | ----------------------- |
| shift       | Toggle Organic          |
| ctrl+l      | Toggle Lure             |
| ctrl+r      | Reset  Calculation      |
| ctrl+d      | Cycle  Defense          |
| alt+d       | Cycle  Negative Defense |
| ctrl+x      | Lock/Unlock statuses    |
| alt+up      | Toggle Pinned Window    |

It is possible to change these keybinds. There is a guide on the wiki to doing so on the [Usage: Keybinds](https://github.com/Vhou-Atroph/TT-Damage-Calculator/wiki/Usage:-Keybinds#editing-a-keybind) page.

## License

Code in TT-Damage-Calculator is licensed under the [GNU General Public License v3.0](/LICENSE).

## Final Notes

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/I2I65IWZG)
