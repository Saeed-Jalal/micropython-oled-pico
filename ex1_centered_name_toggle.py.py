from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Display dimensions
WIDTH = 128
HEIGHT = 64

# Create I2C connection
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)

# Initialize OLED display
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Button setup
button = Pin(15, Pin.IN, Pin.PULL_UP)
button_was_pressed = False
screen_on = False

# Text and its dimensions
name = "Saeed Jalal"  # Replace with your actual name
char_width = 8  # Default font is 8x8 pixels
char_height = 8

# Calculate position to center the text
x = (WIDTH - len(name) * char_width) // 2
y = (HEIGHT - char_height) // 2

while True:
    if button.value() == 0 and not button_was_pressed:
        screen_on = not screen_on  # Toggle screen state
        oled.fill(0)  # Clear screen (whether turning off or preparing to draw)
        if screen_on:
            oled.text(name, x, y)
        oled.show()
        button_was_pressed = True
        time.sleep(0.1)  # Debounce delay

    elif button.value() == 1 and button_was_pressed:
        button_was_pressed = False
        time.sleep(0.05)
