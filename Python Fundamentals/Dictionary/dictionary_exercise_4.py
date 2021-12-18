# Dictionary Exercise ---> Creating Dictionarys --> Dict Comprehensions

#### LESSON  
#--------- Let’s say we have two lists that we want to combine into a dictionary, Python allows you to create a dictionary using a dict comprehension, with this syntax:
#****** dictionary_name = {key:value for key, value in zip(list_1, list_2)}   ******

##### Remember that zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:
####### + Takes a pair from the iterator of tuple
####### + Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list
####### + Creates a key : value item in the students dictionar
####### + Repeats steps 1-3 for the entire iterator of pairs


#### [Step 0]
### we start with lists
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

## [Step 1]
####### You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list.

zipped_drinks = zip(drinks, caffeine)

## [Step 2]
####### Create a dictionary called drinks_to_caffeine by using a dict comprehension that goes through the zipped_drinks iterator and turns each tuple pair into a key:value item.

drinks_to_caffeine = {drinks: caffeine for drinks, caffeine in zipped_drinks}

##### syntax is
# dict_variable = {key: value for key, value in zip_iterator}