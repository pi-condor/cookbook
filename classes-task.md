# Classes in Python
  - Classes are templates that allow us to create reusable structures in our code
  - They are useful for grouping together related values and actions into one large data type
  - They have two things: 
     1. Properties (variables associated with the class)
     2. Methods (functions that act on those variables)
  - An object is just an instance/specific version of a class.
     - So Condor could be an instance or object of the `Human` class
  - To access the properties and methods inside a class, use the `.` operator (AKA the dot operator)
  - Every class has a function called `__init__()` that constructs, or returns, an object of the class.
  - Every method in Python NEEDS an argument inside of it called `self`.
    - `self` refers to the current object that is using the method in the code
## An example program that uses a class
```python
class Instructor():

    # This __init__() method is used to define all the properties in our instructor class
    def __init__(self, name, course_name):
        # Give all objects of the instructor class the following attributes
        self.name        = name
        self.course_name = course_name
        self.location    = "Kean University"
        self.students    = []
    
    # This is an example of a method that teaches the students
    def teach(self):
        print(self.name, "is currently teaching", self.course_name)
    
    # Add a student to the instructor's course
    def add_student(self, student_name):
        self.students.append(student_name)
    
    # Another example method to print all students in an instructor's course
    def print_roster(self):
        print(self.name, "has", len(self.students), "students in his course: ")
        for student in self.students:
            print("\t", student)

# Create objects of the Instructor class
keychain = Instructor("Keychain", "Minecraft Mod Builder")
blue_jay = Instructor("Blue Jay", "Fortnite and Unreal")
condor   = Instructor("Condor", "Pi-Top")
moose    = Instructor("Moose", "Roblox")

# Use the class methods on the objects
keychain.teach()
blue_jay.teach()

condor.add_student("Troy")
condor.add_student("Gabriella")
condor.add_student("Chad")

print()
condor.print_roster()
```
## Assignment
After you've read through all the comments in the previous code sample, try writing the following program:
 - Create a class called `Point`
 - Create a constructor for the `Point` class that takes in two parameters: x and y
    - Inside the constructor, define x and y properties for your `Point` class
 - Create a `print()` method that prints: "Point(X, Y)". Make sure, of course, that you display the actual x and y values of the point, not the letters 'x' and 'y'
 - Create a `distance_to()` method that returns a double which is the distance between a given point and the provided point
 - Create two `Point` objects
    - Print out both points
    - Find the distance between each point
