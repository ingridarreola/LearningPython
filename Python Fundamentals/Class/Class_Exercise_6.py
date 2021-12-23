# Intro to Classes ---> Self
# Lesson:  the self keyword refers to the object and not the class being called. This is the strength of writing object-oriented programs. We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.

## [Step 1]
####### you’ll find our familiar friend, the Circle class. Even though we usually know the diameter beforehand, what we need for most calculations is the radius. In Circle‘s constructor set the instance variable self.radius to equal half the diameter that gets passed in.

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:

    self.radius = diameter * 0.5

## [Step 2]
####### Define three Circles with three different diameters. A medium pizza, medium_pizza, that is 12 inches across. Your teaching table, teaching_table, which is 36 inches across. The Round Room auditorium, round_room, which is 11,460 inches across.

# note that these are being defined outside of the class (i.e. no indentation for these pairs)
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)


## [Step 3]
####### Define a new method circumference for your circle object that takes only one argument, self, and returns the circumference of a circle with the given radius by this formula:       circumference = 2 * pi * radius

    def circumference(self):
        return 2 * self.pi * self.radius

## [Step 4]
####### Print out the circumferences of medium_pizza, teaching_table, and round_room.

# Have to assign Circle. first so that it knows where circumference comes from ... from up above

print(Circle.circumference(medium_pizza))
print(Circle.circumference(teaching_table))
print(Circle.circumference(round_room))