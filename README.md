# DualShock 4 Joystick Emulator
DS4-Joystick-Emulator is a simple Python script for Windows that uses yannbouteiller's vgamepad module to emulate the right joystick of a DualShock controller.

This was created pretty much exclusively to combat the fact that ShadPS4 does not yet support mouse movement inputs at the time I'm writing this. The left joystick isn't much of a problem since it's bound to WASD by default, but the default bindings for the right joystick are impractical for most games.

I currently don't have plans to expand this to support other bindings or to add a gui or anything. If you want to tweak the values, head on into the Python script and you should hopefully have an easy enough time tweaking it to your liking. I'd also like to suggest AutoHotkey for binding other keys, ShadPS4 has keyboard bindings for every DualShock input even if they're not intuitive. The result of that though is that AutoHotkey works fine.

---
## Requirements

[python3](https://www.python.org/)
## Running the Program
Download the latest release from the releases page and extract the file wherever you please.
Open the folder you just extracted and run run.ps1. This should open a new PowerShell window with the script running.
Open your game and start playing!

---
Troubleshooting
MacOS and Linux may work, but there is no official support and they are untested. Please do not open issues if you are not using Windows 10/11.

"The script crashes when I launch it" Make sure you have a valid python3 install.

I've had some issues when trying to use this for Bloodborne without a patch for my monitor's native resolution. If yours isn't supported by default, try [this mod.](https://www.nexusmods.com/bloodborne/mods/79)

This was written for and tested on 60 FPS Bloodborne! 30 FPS may feel different or janky. Feel free to tweak some stuff if it does. 
