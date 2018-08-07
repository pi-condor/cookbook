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
Simple printing
```python
print("Hi")  # Hi
print(3 * 4) # 12
```
Concatenation (adding strings)
```python
name = "Condor"
time_of_day = "afternoon"
print("Good " + time_of_day + ", " + name) # Good afternoon, Condor
```
Using multiple parameters in the print function
```python
other_name = "Condan"
fav_num = 27
# Notice how this method can combine multiple data types.
# It also places a space (' ') between each argument
print("Hey", other_name, "I can't believe you like the number", fav_num) 
# Hey Condan I can't believe you like the number 27
```
String formatting
```python
my_hp = 100
your_hp = 80
# All your blanks are the '{}' characters. The arguments inside the '.format()' method fill in those blanks.
print("My HP: {}\nYour HP: {}".format(my_hp, your_hp)) # My HP: 100
                                                       # Your HP: 80
```
### User Input
Getting input
```python
# Note: the input function always returns a value as a string
users_name = input("What's your name? ")
```
Changing the capitalization of input
```python
# Turn all the characters to uppercase
users_name = users_name.upper()

# Turn all the cahracters to lowercase
users_name = users_name.lower()
```
### Casting
Casting is just going from one data type to another<br><br>
Casting to an integer
```python
num1 = '8'
print(num1 * 3)  # prints out '888'

num1 = int(num1) # Convert num1 into an integer using the 'int()' function
print(num1 * 3)  # prints out 24
```
Casting to a string
```python
my_fav_num = 17
print("My favorite number is " + str(my_fav_num)) # prints "My favorite number is 17"
```
### Conditional Statements
if statements
```python
fav_pokemon = "Ditto"
if fav_pokemon == "Ditto":
    # This code will run
    print("Me too, thanks")
```
if + else statements
```python
my_health = -10
if my_health > 0:
    print("I am alive")
else:
    # This code will run
    print("I'm not alive")
```
if + elif + else statements
```python
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
while loops
```python
# While loops are used when we want to loop an unspecified/unknown amount of times
while True:
    print("Hi, Phil Swift here with F L E X S E A L.")
```
for loops
```python
# For loops count a given amount of times or go through all values in a list
# In Python, all for loops follow the following syntax:
# for VARIABLE in LIST:
#   CODE HERE
# So to count a specified number of times, use the range(num) function.
# The range function can to generate a list of a given length that counts up from 0

for counter in range(4):
    print(counter)
# prints out:
# 0
# 1
# 2
# 3
```

### Functions
The basic format of a function is as follows:
```
    def name_of_function(list_of_inputs):
        # Code inside the function
```    
Notice how there is no return type (e.g., public int, public void) like in Java, just the 'def' keyword<br><br>
Simple function
```python
def greet(name):
    print("Hello,", name)

greet("Condor") # prints out "Hello, Condor"
```
Return statements
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
Just a note: all import statements in a file usually go at the top of the Python file, one module after another separated by a single line<br><br>
Importing entire modules
```python
import time # imports the entire time module

# When using functions inside the time module, you put 'time.' in front of the name of the functions 
time.sleep(5)
current_time = time.time()
```
Importing specific functions from modules
```python
from random import random, randint # imports the random() and randint() functions from the random module

# Now, you can use these functions without using the 'random.' syntax
random_decimal = random()
random_int = random_int(10)
```
### Random Numbers
Basics of RNG
```python
import random

# 'random()' generates a random number from 0 - 1
random_decimal = random.random()

# 'randomint(num)' generates a random int from 0 - num
random_int = random.randint(100) # can be 1, 2, 3, ..., or 100

# 'choose(list_of_options) will pick a random value from list_of_options
random_choice = random.choose(['fists', 'feet', 'flex seal']) #either fists, feet, or flex seal

# 'uniform(lower_bound, upper_bound) will generate a decimal between lower_bound and upper_bound
random_val = random.uniform(10, 20) # a random decimal between 10.0 and 20.0
```
Running code based on randomly-generated numbers
```python
import random

if random.random() <= 0.75:
    # This code will run 75% of the time
    print("We got into the if")
else:
    print("Looks like we got into the else)
```
## Pygame
### Good pygame tutorial
[https://pythonprogramming.net/](https://pythonprogramming.net/)
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

# Keep the LED on until the button is  pressed
my_led.on()
my_button.wait_for_press()
my_led.off()
```
