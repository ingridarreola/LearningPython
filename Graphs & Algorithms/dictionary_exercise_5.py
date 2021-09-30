# Dictionary Exercise ---> Creating Dictionarys --> Review

#### LESSON  
#--------- So far we have learned:
#[+] How to create a dictionary
#[+] How to add elements to a dictionary
#[+] How to update elements in a dictionary
#[+] How to use a list comprehension to create a dictionary from two list

###  [Step 0]
# we start with two lists
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

## [Step 1]
####### We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.
# Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.

plays = {songs: playcounts for songs, playcounts in zipped_music}

## [Step 2]
####### Print plays.

print(plays)

## [Step 3]
####### After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.

plays["Purple Haze"] = 1

## [Step 4]
####### This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to be 94 in the plays dictionary.

plays["Respect"] = 94

## [Step 5]
####### Create a dictionary called library that has two key: value pairs:
# key "The Best Songs" with a value of plays, the dictionary you create
# key "Sunday Feelings" with a value of an empty dictionary

library = {"The Best Songs": plays, "Sunday Feelings": {}}

## [Step 6]
####### print library

print(library)
