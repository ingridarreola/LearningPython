# Dictionary Exercise ---> Using Dictionaries --> Safely Get a Key

#### LESSON  
# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default

###  [Step 0]
# we start with a dictionary
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

###  [Step 1]
# Use .get() to get the value of "teraCoder"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called tc_id. Print tc_id to the console

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
# prints out ---> 100019


### [Step 2]
# Use .get() to get the value of "superStackSmash"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called stack_id. Print stack_id to the console

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
# prints out ---> 100000