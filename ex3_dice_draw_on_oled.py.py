from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import urandom
import time

# OLED setup
WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Button setup
button = Pin(15, Pin.IN, Pin.PULL_UP)
button_was_pressed = False

# Dice dot drawing positions
cx, cy = WIDTH // 2, HEIGHT // 2
offset = 10  # Distance between center and surrounding pips
radius = 2   # Size of dots (just filled pixels for now)

def draw_dot(x, y):
    oled.fill_rect(x - radius, y - radius, radius * 2, radius * 2, 1)

def draw_dice_face(number):
    oled.fill(0)
    
    # Coordinates for dots
    positions = {
        1: [(cx, cy)],
        2: [(cx - offset, cy - offset), (cx + offset, cy + offset)],
        3: [(cx - offset, cy - offset), (cx, cy), (cx + offset, cy + offset)],
        4: [(cx - offset, cy - offset), (cx + offset, cy - offset),
            (cx - offset, cy + offset), (cx + offset, cy + offset)],
        5: [(cx - offset, cy - offset), (cx + offset, cy - offset),
            (cx, cy),
            (cx - offset, cy + offset), (cx + offset, cy + offset)],
        6: [(cx - offset, cy - offset), (cx + offset, cy - offset),
            (cx - offset, cy),     (cx + offset, cy),
            (cx - offset, cy + offset), (cx + offset, cy + offset)]
    }

    for (x, y) in positions[number]:
        draw_dot(x, y)

    oled.show()

while True:
    if button.value() == 0 and not button_was_pressed:
        roll = urandom.getrandbits(3) % 6 + 1
        print("You rolled a", roll)
        draw_dice_face(roll)
        button_was_pressed = True
        time.sleep(0.1)  # Debounce

    elif button.value() == 1 and button_was_pressed:
        button_was_pressed = False
        time.sleep(0.05)
