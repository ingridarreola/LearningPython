# Intro to Classes ---> Methods --> Instance Variables
# Lesson:  a class is a schematic for a data type and an object is an instance of a class, but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has? This is because each instance of a class can hold different kinds of data.
# The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

## [Step 1]
####### In script.py we have defined a Store class. Create two objects from this store class, named alternative_rocks and isabelles_ices.

class Store:
  pass

alternative_rocks = Store()

isabelles_ices =  Store()


## [Step 2]
####### Give them both instance attributes called store_name. Set alternative_rocks‘s store_name to "Alternative Rocks". Set isabelles_ices‘s store_name to "Isabelle's Ices".

alternative_rocks.store_name = "Alternative Rocks"

isabelles_ices.store_name = "Isabelle's Ices"