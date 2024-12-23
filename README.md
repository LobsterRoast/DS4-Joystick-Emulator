# DualShock 4 Joystick Emulator

This is a simple Python script using yannbouteiller's [vgamepad module](https://github.com/yannbouteiller/vgamepad) that emulates the right joystick of a DualShock controller.

This was created pretty much exclusively to combat the fact that ShadPS4 does not yet support mouse inputs as I'm writing this. The left joystick isn't much of a problem since it's bound to WASD by default, but the default bindings for the right joystick are not practical for most games.

I currently don't have plans to expand this to support other bindings or to add a gui or anything. If you want to tweak the values, head on into the Python script and you should hopefully have an easy enough time tweaking it to your liking. I'd also like to suggest AutoHotkey for binding other keys, ShadPS4 has keyboard bindings for every DualShock input even if they're not intuitive. The result of that though is that AutoHotkey works fine.

### Installation

Simply activate the venv for the script and then, in the root directory, run:
```bash
python3 main.py
```
To exit the emulator, press CTRL+Q. You can also use CTRL+T to toggle the emulator function without closing it entirely.
