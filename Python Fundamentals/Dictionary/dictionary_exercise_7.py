# Dictionary Exercise ---> Using Dictionaries --> Get an Invalid Key

#### LESSON  

###  [Step 0]
# we start with a dictionary that maps the elements of astrology to the zodiac signs. Run the code. It should throw a KeyError! "energy" does not exist as one of the elements.

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}


print(zodiac_elements["energy"])

#prints out ----> KeyError: 'energy'
### this is saying that it does not exist as one of the elements.

###  [Step 1]
# Add the key "energy" to the zodiac_elements. It should map to a value of "Not a Zodiac element". Run the code. Did this resolve the KeyError?

zodiac_elements["energy"] = "Not a Zodiac element"

# print(zodiac_elements["energy"])
# prints out ---> Not a Zodiac element