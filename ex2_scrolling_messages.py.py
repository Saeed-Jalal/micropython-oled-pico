from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import sys
import select

# OLED dimensions
WIDTH = 128
HEIGHT = 64

# Create I2C connection
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Button setup
button = Pin(15, Pin.IN, Pin.PULL_UP)
button_was_pressed = False

# Screen config
line_height = 8
max_lines = HEIGHT // line_height
messages = []

# Setup for non-blocking input
poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

def redraw_screen():
    oled.fill(0)
    for i, msg in enumerate(messages[-max_lines:]):
        oled.text(msg, 0, i * line_height)
    oled.show()

print("IOT (CTRL+C to stop):")

try:
    while True:
        # Check for button press
        if button.value() == 0 and not button_was_pressed:
            messages = []
            oled.fill(0)
            oled.show()
            button_was_pressed = True
            time.sleep(0.2)
        elif button.value() == 1 and button_was_pressed:
            button_was_pressed = False
            time.sleep(0.05)

        # Check if there is input available
        if poll.poll(0):  # Non-blocking check
            line = sys.stdin.readline().strip()
            messages.append(line)
            redraw_screen()

        time.sleep(0.1)  # Small delay to avoid CPU overload
except KeyboardInterrupt:
    print("Exiting...")
    oled.fill(0)
    oled.show()


