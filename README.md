# DualShock 4 Joystick Emulator

This is a simple Python script using yannbouteiller's [vgamepad module](https://github.com/yannbouteiller/vgamepad) that emulates the right joystick of a DualShock controller.

This was created pretty much exclusively to combat the fact that ShadPS4 does not yet support mouse inputs as I'm writing this. The left joystick isn't much of a problem since it's bound to WASD by default, but the default bindings for the right joystick are not practical for most games.

I currently don't have plans to expand this to support other bindings or to add a gui or anything. If you want to tweak the values, head on into the Python script and you should hopefully have an easy enough time tweaking it to your liking. I'd also like to suggest AutoHotkey for binding other keys, ShadPS4 has keyboard bindings for every DualShock input even if they're not intuitive. The result of that though is that AutoHotkey works fine.
## Requirements
I've had some issues when trying to use this without a patch for my monitor's native resolution. If yours isn't supported by default, try (this mod.)[https://www.nexusmods.com/bloodborne/mods/79?tab=description]
## Installation

Simply activate the venv for the script and then, in the root directory, run:
```bash
python3 main.py
```
The emulator locks your cursor into position to prevent it from reaching the edge of the screen, so you'll need to use Alt+Tab or toggle the emulator to switch to your desired window.
To exit the emulator, press CTRL+Q. You can also use CTRL+T to toggle the emulator function without closing it entirely.

**This was written for and tested on 60 FPS Bloodborne! 30 FPS may feel different or janky. Feel free to tweak some stuff if it does.**
