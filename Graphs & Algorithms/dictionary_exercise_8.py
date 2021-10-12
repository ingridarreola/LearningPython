# Dictionary Exercise ---> Using Dictionaries --> Try/Except to Get a Key

#### LESSON  
# We saw that we can avoid KeyErrors by checking if a key is in a dictionary first. Another method we could use is a try/except

###  [Step 0]
# we start with a dictionary
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

### [Step 1]
# Use a try block to try to print the caffeine level of "matcha". If there is a KeyError, print "Unknown Caffeine Level"

#fist set what you want to check
key_to_check = "matcha"
#use this key_to_check in the try except below
try:
  print(caffeine_level[key_to_check])
except KeyError:
  print("Unknown Caffeine Level")

# prints out ----> Unknown Caffeine Level

### [Step 2]
# Above the try block, add "matcha" to the dictionary with a value of 30.
caffeine_level["matcha"] = 30

# if it's above the keys_to_check then it will print out ---> 30
