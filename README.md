MicroPython OLED Display Projects with Raspberry Pi Pico W 

This repository contains three hands-on MicroPython exercises using a Raspberry Pi Pico W, an SSD1306 OLED display, and a push button. 
These projects demonstrate basic I/O, display handling, and user interaction — great for embedded systems and IoT beginners. 

Hardware Used :

Raspberry Pi Pico W  
SSD1306 128x64 OLED display (I2C)  
Push button  
Jumper wires  
Breadboard 

Setup: 

Flash your Raspberry Pi Pico W with MicroPython. 

Wire the hardware as per the diagram attached. 

Use Thonny or any MicroPython IDE to run the files. 

 Exercises 

✅ ex1_centered_name_toggle.py 

Displays your name centered on the OLED when the button is pressed. Press again to clear the screen. Calculates exact center based on text length. 

✅ ex2_scrolling_messages.py 

Takes user input from the REPL and displays messages line by line. When the screen is full, older messages scroll up to show the newest at the bottom.
Pressing the button empties the display

✅ ex3_dice_draw_on_oled.py 

Simulates a dice roll (1-6) on each button press and visually draws the corresponding side on the OLED like a real dice face. 

Requirements :

Install the ssd1306 

Made With 

MicroPython  

Raspberry Pi Pico W  

SSD1306 I2C OLED 

 
