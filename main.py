import vgamepad as vg
import time
import math
import keyboard
from screeninfo import get_monitors
from pynput.mouse import Controller

print("Joystick Emulator Activated.\nPress 'ctrl + q' to exit.\nPress 'ctrl + t' to toggle the emulator.")

# Initialize library modules
mouse = Controller()
gamepad = vg.VDS4Gamepad()
screen = get_monitors()[0]

# you can change this, but I would not recommend this.
screen_width = screen.width
screen_height = screen.height

# deadzones dont feel so great on mouse and keyboard, so this is used to implement logic that gets around ShadPS4's deadzones
deadzones = 35

# Mouse Sensitivity
x_sensitivity = 20
y_sensitivity = 20

# Changing this will result in undefined behaviour
center_x, center_y = screen_width/2, screen_height/2
active = True

def clamp(i, minval, maxval):
	i = max(minval, i)
	i = min(maxval, i)
	return i

while True:
	if active == True:
		current_x, current_y = mouse.position[0] - center_x, mouse.position[1] - center_y
		# Mouse has to be reset to center of the screen to stop it from reaching the edge
		mouse.position = center_x, center_y
		dx_buf, dy_buf = current_x - center_x, current_y - center_y
		dx = dx * 0.2 + center_x if dx_buf == 0 else dx_buf + center_x
		dy = dy * 0.2 + center_y if dy_buf == 0 else dy_buf + center_y
		# Library measures from the center of the screen, so we add center_x/y here and also multiply by sensitivity
		transformed_x, transformed_y = dx * x_sensitivity + center_x, dy * y_sensitivity + center_y
		# Find the sign by which the deadzones will be multiplied
		dz_mult_x = 0 if dx == 0 else math.copysign(1, dx)
		dz_mult_y = 0 if dx == 0 else math.copysign(1, dy)
		# Technically this method for cancelling out the deadzones is an overcorrection since it doesn't take into account that the deadzones are circular rather than square
		# That being said, I beat the entire game like this and the effects weren't noticable. Feel free to make a PR request to fix it but I'm too lazy right now lmao
		joystick_x = int(clamp(round(transformed_x*255/screen_width, 0)+deadzones*dz_mult_x, 0, 255))
		# library documentation said the values should be between 0 and 255, but 0 didn't work for the y-axis, so it's clamped to bottom out at 1
		joystick_y = int(clamp(round(transformed_y*255/screen_height, 0)+deadzones*dz_mult_y, 1, 255))
		gamepad.right_joystick(x_value=joystick_x, y_value=joystick_y)
		gamepad.update()
	if (keyboard.is_pressed('ctrl') and keyboard.is_pressed('q')):
		break
	if (keyboard.is_pressed('ctrl') and keyboard.is_pressed('t')):
		active = not active
		time.sleep(0.2)
	# Best if the sleep delay is untouched. Higher or lower values may feel exceedingly janky (note that this was tested at 60fps) 
	time.sleep(0.004)
