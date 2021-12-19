# Intro to Classes ---> Methods --> Methods with Arguments

## [Step 1]
####### You decide to create a program that calculates the area of a circle. Create a Circle class with class variable pi. Set pi to the approximation 3.14.

class Circle:
  pi = 3.14


## [Step 2]
####### Give Circle an area method that takes two parameters: self and radius. Return the area as given by this formula: area = pi * radius ** 2

#- Cirlce is my class
#-- this class has a variable, which is pi
#---- this has a method which is area
#----- this method takes 2 parameters, which are self and radius

class Circle:
  pi = 3.14
  def area(self, radius):
    area = Circle.pi * radius ** 2
    return area

## [Step 3]
####### Create an instance of Circle. Save it into the variable circle.

circle = Circle()


## [Step 4]
####### You go to measure several circles you happen to find around. A medium pizza that is 12 inches across. Your teaching table which is 36 inches across. The Round Room auditorium, which is 11,460 inches across. -----> You save the areas of these three things into pizza_area, teaching_table_area, and round_room_area. 
# Remember that the radius of a circle is half the diameter. We gave three diameters here, so halve them before you calculate the given circle’s area.

pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)