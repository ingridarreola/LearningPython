# Dictionary Exercise ---> Using Dictionaries --> Get All Values

#### LESSON  
# dictionary_name.items() will print out the keys & values in that dictionary. A for loop can iterate through these things in the dictionary

###  [Step 0]
# we start with a dictionary
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

###  [Step 1]
# Use a for loop to iterate through the items of pct_women_in_occupation. For each key : value pair, print out a string that looks like:
#### Women make up [value] percent of [key]s.

for key, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + key + "s."  )

## Women make up 28 percent of CEOs.
## Women make up 9 percent of Engineering Managers.
## Women make up 58 percent of Pharmacists.
## Women make up 40 percent of Physicians.
## Women make up 37 percent of Lawyers.
## Women make up 9 percent of Aerospace Engineers.