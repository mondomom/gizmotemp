# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid teal
background, a smaller cyan rectangle, and some red text.
-- Coded by me :)  27 Oct 2024
"""
import displayio
import terminalio
import adafruit_thermistor
import board
import time
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
from adafruit_bitmap_font import bitmap_font

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(240, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x008080  # Teal

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(200, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x00FFFF  # Cyan
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Set up the font
font_file = "/fonts/LeagueSpartan_Bold_16.bdf"
font = bitmap_font.load_font(font_file)

# Draw a label
text_group = displayio.Group(scale=2, x=50, y=80)
text = "Hello World!"
# text_area = label.Label(terminalio.FONT, text=text, color=0xFF0101)  # Red text
text_area = label.Label(font, text=text, color=0xFF0101)  # Red text
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

# Set up the Temperature Sensor
thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)

while True:
    temp_c = round(thermistor.temperature, 1) # round to one decimal place (saves space!)
    temp_f = thermistor.temperature * 9 / 5 + 32
    print("Temperature is: %f C and %f F" % (temp_c, temp_f))
    text = ("Temp:\n" + str(temp_c) + " C")
    #text = ("Current Temp:\n  " + temp_c + " C")
    text_area.text = text
    time.sleep(30)
