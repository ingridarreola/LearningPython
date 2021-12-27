# Intro to Classes ---> Review

# Lesson: Create two classes and define their interactions. This is object-oriented programming.

## [Step 1]
####### Define a class Student this will be our data model at Jan van Eyck High School and Conservatory.

class Student():
  pass


## [Step 2]
####### Add a constructor for Student. Have the constructor take in two parameters: a name and a year. Save those two as attributes .name and .year.

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year

## [Step 3]
####### Create three instances of the Student class: Roger van der Weyden, year 10 ||| Sandro Botticelli, year 12 ||| Pieter Bruegel the Elder, year 8

## Note --
#### these instances have to be outside of the indent from that class, so they're actually created as three instances of the class itself

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


## [Step 4]
####### Create a Grade class, with minimum_passing as an attribute set to 65.

class Grade:
  minimum_passing = 65


## [Step 5]
####### Give Grade a constructor. Take in a parameter score and assign it to self.score.

  def __init__(self, score):
    self.score = score


## [Step 6]
#######  In the body of the constructor for Student, declare self.grades as an empty list.

###### Note --
########## this is defined inside of the Student class i.e. after line 18

    self.grades = []

## [Step 7]
####### Add an .add_grade() method to Student that takes a parameter, grade. .add_grade() should verify that grade is of type Grade and if so, add it to the Student‘s .grades. If grade isn’t an instance of Grade then .add_grade() should do nothing.

###### Note --
########## This is inside of Student class so it should be going after the previous self.grades line

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)


## [Step 8]
####### Add an .add_grade() method to Student that takes a parameter, grade. .add_grade() should verify that grade is of type Grade and if so, add it to the Student‘s .grades. If grade isn’t an instance of Grade then .add_grade() should do nothing.

###### Note --
########## This should be added at the very bottom of the entire script ... after pieter has been defined as its own line

pieter.add_grade(Grade(100))

########
####
## The final script is shown below for this exercise

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

class Grade:
  minimum_passing = 65
      

  def __init__(self, score):
    self.score = score


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
