# Boot Message
print "Starting..."

import board
import busio

# Basic Switch Imports
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros

# RGB LED Imports
from kmk.extensions.RGB import RGB

# Encoder Imports
from kmk.modules.encoder import EncoderHandler

# SSD1306 OLED Display Imports
from kmk.extensions.display.ssd1306 import SSD1306

# Keyboard Instance
keyboard = KMKKeyboard()

# Add Macro Extension
macros = Macros()
keyboard.modules.append(macros)

# Define Switch Pins
PINS = [board.D1, board.D2, board.D3, board.D4, board.D26, board.D27]

# Define that we are not using a matrix (KeyScanner)
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Add RGB Extension
rgb = RGB(pixel_pin=board.GP0, num_pixels=10)
keyboard.extensions.append(rgb)

# Display Setup
spi_bus = busio(board.SCL, board.SDA)
display = Display(
display=driver
)

# Define keyboard outputs for pins (change to shortcuts later)
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F]
]

# Encoder Setup
encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]

encoder_handler.pins = (board.GP28, board.GP29, None, False, 2,)



# Start kmk
if __name__ = '__main__':
    keyboard.go()


