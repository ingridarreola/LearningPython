# Intro to Classes ---> Methods --> Constructors
# Lesson: Constructors have two underscores (double-underscore abbreviated to “dunder”) on either side of them. This method is used to initialize a newly created object. It is called every time the class is instantiated. Methods that are used to prepare an object being instantiated are called constructors. 

## [Step 1]
####### Add a constructor to our Circle class. Since we seem more frequently to know the diameter of a circle, it should take the argument diameter. It doesn’t need to do anything yet, just write pass in the body of the constructor.

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    pass


## [Step 2]
####### Now have the constructor print out the message "New circle with diameter: {diameter}" when a new circle is created. Create a circle teaching_table with diameter 36.

  # Edit to the constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
# we use {} to call the parameter
# we use .format ---> to define what diameter is equal to ... it's equal to the parameter


teaching_table = Circle(36)
# this prints out ----> New circle with diameter: 36
# we can call our class directly with Circle
# we pass 36 as our parameter asks for us to define a diameter