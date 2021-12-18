# Dictionary Exercise ---> Using Dictionaries --> Get All Keys

#### LESSON  
# dictionary_name.keys() will print out the keys in that dictionary

###  [Step 0]
# we start with a dictionary
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

###  [Step 1]
# Create a variable called users and assign it to be a dict_keys object of all of the keys of the user_ids dictionary.
users = user_ids.keys()

###  [Step 2]
# Create a variable called lessons and assign it to be a dict_keys object of all of the keys of the num_exercises dictionary.

lessons = num_exercises.keys()

###  [Step 3]
# Print users to the console.
print(users)
# prints out...
## dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])


###  [Step 4]
# Print lessons to the console.
print(lessons)

# prints out...
## dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])
