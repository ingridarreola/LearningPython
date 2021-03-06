# Dictionary Exercise ---> Using Dictionaries --> Review

#### LESSON  
# Creating a new dictionary and using .pop() to remove things from the original dictionary and placing it into an empty dictionary with the following syntax ----> new_dictionary["new key"] = old_dictionary.pop("old key")
# dictionary_name.items() will print out the keys & values in that dictionary. A for loop can iterate through these things in the dictionary

###  [Step 0]
# we start with a dictionary
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

###  [Step 1]
# We have provided a pack of tarot cards, tarot. You are going to do a three card spread of your past, present, and future.
# Create an empty dictionary called spread.

spread = {}

###  [Step 2]
# The first card you draw is card 13. Pop the value assigned to the key 13 out of the tarot dictionary and assign it as the value of the "past" key of spread.

#.pop() removes the value from tarot dictionary
# new_dictionary["new key"] = old_dictionary.pop("old key")
spread["past"] = tarot.pop(13)

###  [Step 3]
# The second card you draw is card 22. Pop the value assigned to the key 22 out of the tarot dictionary and assign it as the value of the "present" key of spread.

# new_dictionary["new key"] = old_dictionary.pop("old key")
spread["present"] = tarot.pop(22)


###  [Step 4]
# The third card you draw is card 10. Pop the value assigned to the key 10 out of the tarot dictionary and assign it as the value of the "future" key of spread.

# new_dictionary["new key"] = old_dictionary.pop("old key")
spread["future"] = tarot.pop(10)


###  [Step 5]
# Iterate through the items in the spread dictionary and for each key: value pair, print out a string that says: "Your {key} is the {value} card."

# dictionary_name.items() will print out the keys & values in that dictionary. A for loop can iterate through these things in the dictionary

for key, value in spread.items():
    print("Your " + key + " is the " + str(value) + " card.")

#prints out the following --->
### Your past is the Death card.
### Your present is the The Fool card.
### Your future is the Wheel of Fortune card.