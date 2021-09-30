# Dictionary Exercise ---> Creating Dictionarys --> Overwrite Values

#### LESSON  
#--------- We know that we can add a key by using syntax like:
#--------------------- menu["avocado toast"] = 7 
# That same syntax would overwrite the value if it already existed in the dictionary

## [Step 1]
####### We start with this defined dictionary

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

## [Step 2]
####### Add the key "Supporting Actress" and set the value to "Viola Davis".

oscar_winners.update({"Supporting Actress": "Viola Davis"})

## [Step 3]
####### Without changing the definition of the dictionary oscar_winners, change the value associated with the key "Best Picture" to "Moonlight".

oscar_winners["Best Picture"] = "Moonlight"