# Intro to Classes ---> String Representation

# Lesson: One of the first things we learn as programmers is how to print out information that we need for debugging. This default string representation gives us some information, like where the class is defined and our computer’s memory address where this object is stored, but is usually not useful information to have when we are trying to debug our code.

## [Step 0]
####### We start out with the following code below -- from a previous exercise:

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

## [Step 1]
####### Add a __repr__() method to the Circle class that returns

# this would go underneath the def circumference
### we would put in quotes what we are being asked to return
###### we would use ".format" to define what the radius is

    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)


## [Step 2]
####### Print out medium_pizza, teaching_table, and round_room.

print(medium_pizza)
print(teaching_table)
print(round_room)


#### this prints out the stuff below....
# Circle with radius 6.0
# Circle with radius 18.0
# Circle with radius 5730.0