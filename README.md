# Condor's Python Cookbook
## Basic Python Syntax
### Variables
```python
# variable_name = value
my_name = "Bob Ross"
my_fav_num = 17
pi = 3.1415926535897932384626
are_you_tired = True
```
### Printing
```python
# Simple printing
print("Hi")  # Hi
print(3 * 4) # 12
```
```python
# Concatenation (adding strings)
name = "Condor"
time_of_day = "afternoon"
print("Good " + time_of_day + ", " + name) # Good afternoon, Condor
```
```python
# Using multiple parameters in the print function
other_name = "Condan"
fav_num = 27
# Notice how this method can combine multiple data types.
# It also places a space (' ') between each argument
print("Hey", other_name, "I can't believe you like the number", fav_num) 
# Hey Condan I can't believe you like the number 27
```
```python
# String formatting
my_hp = 100
your_hp = 80
# All your blanks are the '{}' characters. The arguments inside the '.format()' method fill in those blanks.
print("My HP: {}\nYour HP: {}".format(my_hp, your_hp)) # My HP: 100
                                                       # Your HP: 80
```
### User Input
```python
# Note: the input function always returns a value as a string
users_name = input("What's your name? ")
```
```python
# Turn all the characters to uppercase
users_name = users_name.upper()
```
```python
# Turn all the cahracters to lowercase
users_name = users_name.lower()
```
### Casting
```python
# Casting is going from one data type to another
# Casting to an int
num1 = '8'
print(num1 * 3)  # prints out '888'

num1 = int(num1) # Convert num1 into an integer using the 'int()' function
print(num1 * 3)  # prints out 24
```
```python
# Casting to a string
my_fav_num = 17
print("My favorite number is " + str(my_fav_num)) # prints "My favorite number is 17"
```
### Conditional Statements
```python
# if alone
fav_pokemon = "Ditto"
if fav_pokemon == "Ditto":
    # This code will run
    print("Me too, thanks")
```
```python
# if + else
my_health = -10
if my_health > 0:
    print("I am alive")
else:
    # This code will run
    print("I'm not alive")
```
```python
# if + elif + else
my_fav_num = 17
if my_fav_num < 5:
    print("That's a small number")
elif my_fav_num < 20:
    # This code will run
    print("That's an average number")
elif my_fav_num < 100:
    print("That a big number")
else:
    print("ARE YOU INSANE! THAT IS A REALLY BIG NUMBER")
```
### Looping
```python
# While loops are used when we want to loop an unspecified/unknown amount of times
while True:
    print("Hi, Phil Swift here with F L E X S E A L.")
```
```python
# For loops count a given amount of times or go through all values in a list
# In Python, all for loops follow the following syntax:
# for VARIABLE in LIST:
#   CODE HERE
# So to count a specified number of times, use the range() function to generate a list of 
# a given length that counts up from 0


for counter in range(4):
    print(counter)
# prints out:
# 0
# 1
# 2
# 3
```

### Functions
```python
""" Basic Format
    def name_of_function(list_of_inputs):
        # Code inside the function
    
    Notice how there is no return type (e.g., public int, public void), just the 'def' keyword
"""
# Function definition
def greet(name):
    print("Hello,", name)

greet("Condor") # prints out "Hello, Condor"
```
```python
# Function with a return
# Return statements indicate what value will replace the function when it is called (used)
def triple(num):
    return 3 * num

# When this gets called, Python computes that 3 * 10 = 30 inside the triple function.
# Then, the value 30 replaces the text 'triple(10)', thus assigning a value of 30 to the 'number' variable
number = triple(10)
```
### Import statements
Just a note: all import statements in a file usually go at the top of the Python file, one module after another separated by a single line
```python
import time # imports the entire time module

# When using functions inside the time module, you put 'time.' in front of the name of the functions 
time.sleep(5)
current_time = time.time()
```
```python
from random import random, randint # imports the random() and randint() functions from the random module

# Now, you can use these functions without using the 'random.' syntax
random_decimal = random()
random_int = random_int(10)
```
## Pygame
### Installing pygame (in Terminal)
```sh
$ pip install pygame
$ pip3 install pygame
```
### Open a window
```python
import pygame # Import all of pygame

# Start up pygame
pygame.init()

# Setup the display window
width = 800
height = 500
game_display = pygame.display.set_mode((width, height)) # Notice the extra set of parentheses (because these are tuples)!
game_display.fill((255, 255, 255)) # Fill the display with the (red, green, blue) color combination (in this case, white)
pygame.display.update() # Update the display
```
## Circuitry
### GPIO Map
![GPIO MAP](https://github.com/pi-condor/cookbook/blob/master/GPIO%20PROTO%2B%20Instructor%20Large.png)
### LEDs
```python
from gpiozero import LED
from time import sleep

# The number inside the LED constructor is the pin number on the Raspberry Pi
# You can find these numbers in the gameplan module, or right above :)
my_led = LED(4)

# Turn the LED on for 5 seconds, then turn it off
my_led.on()
sleep(5)
my_led.off()

# Toggle the LED on and off every second
while True:
    my_led.toggle()
    sleep(1)
```
### Buttons
```python
from gpiozero import LED, Button
from time import sleep

my_led = LED(4)
my_button = Button(17)

while True:
    # Notice how Button.is_pressed is a property of the Button class, not a method/function.
    # That means we don't use parentheses
    if my_button.is_pressed:
        my_led.on()
    else:
        my_led.off()
```
```python
from gpiozero import LED, Button
from time import sleep

my_led = LED(4)
my_button = Button(17)

while True:
    # Notice how Button.is_pressed is a property of the Button class, not a method/function.
    # That means we don't use parentheses
    if my_button.is_pressed:
        my_led.on()
    else:
        my_led.off()
```
