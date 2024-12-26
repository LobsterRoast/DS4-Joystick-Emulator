# DualShock 4 Joystick Emulator
DS4-Joystick-Emulator is a simple Python script for Windows that uses yannbouteiller's vgamepad module to emulate the right joystick of a DualShock controller.

`DS4-joystickEmulator` is a simple Python script for Windows that uses yannbouteiller's [vgamepad module](https://github.com/yannbouteiller/vgamepad) to emulate the right joystick of a DualShock controller.

This was created pretty much exclusively to combat the fact that [ShadPS4](https://github.com/shadps4-emu/shadps4) does not yet support mouse inputs at the time I'm writing this. The left joystick isn't much of a problem since it's bound to WASD by default, but the default bindings for the right joystick are impractical for most games.

I currently don't have plans to expand this to support other bindings or to add a gui or anything. If you want to tweak the values, head on into the Python script and you should hopefully have an easy enough time tweaking it to your liking. I'd also like to suggest AutoHotkey for binding other keys, ShadPS4 has keyboard bindings for every DualShock input even if they're not intuitive. The result of that though is that [AutoHotkey](https://www.autohotkey.com/) works fine.

---

## Requirements
- Python3 [download here](https://www.python.org/downloads/)

---

## Running the Program

1. Download the latest release from the [releases page](https://github.com/LobsterRoast/DS4-Joystick-Emulator/releases/tag/v1.0.1) and extract the file wherever you please.
2. Open the folder you just extracted and run `run.ps1`. This should open a new PowerShell window with the script running.
3. Open bloodborne and start playing!

---

## Troubleshooting

- `MacOS` and `Linux` *may* work, but there is no official support. Please do not open issues if you are not using `Windows 10/11`.

- *"The script crashes when I launch it!!"* Please make sure you have a valid Python3 Installation. [Download here.](https://www.python.org/downloads/) 

- I've had some issues when trying to use this without a patch for my monitor's native resolution. If your monitor's resolution isn't supported by default, try [this mod.](https://www.nexusmods.com/bloodborne/mods/79?tab=description)

**This was written for and tested on 60 FPS Bloodborne! 30 FPS may feel different or janky. Feel free to tweak some stuff if it does.**

---

## Modifying the Source (Advanced users)

- Lines `26` and `27` of `main.py` are the mouse `x` and `y` sensitivity. If you feel like this needs to be higher or lower, change the values to your liking.

```python
# Mouse Sensitivity
x_sensitivity = 20
y_sensitivity = 20
```

- Lines `16` and `17` are your screen's resolution. If this needs to be manually changed for some reason, (i.e the script is reporting incorrect values) then you should change this.

```python
# you can change this, but I would not recommend this.
screen_width = screen.width
screen_height = screen.height
```

---

## Reporting Bugs

If you notice any bugs, please open an issue on this github page.
=======
