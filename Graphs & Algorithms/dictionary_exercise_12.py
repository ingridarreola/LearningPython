# Dictionary Exercise ---> Using Dictionaries --> Get All Values

#### LESSON  
# dictionary_name.values() will print out the values in that dictionary

###  [Step 0]
# we start with a dictionary
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

###  [Step 1]
# Create a variable called total_exercises and set it equal to 0.

total_exercises = 0

###  [Step 2]
# Iterate through the values in the num_exercises list and add each value to the total_exercises variable.

for total in num_exercises.values():
  total_exercises += total # this adds the values to the variable above, so everything first adds to 0 then each number as it goes through
  print(total_exercises)

# this prints out
## 10
## 23
## 38
## 60
## 79
## 97
## 115

###  [Step 3]
# Print the total_exercises variable to the console.

print(total_exercises)
## 115