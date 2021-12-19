# Intro to Classes ---> Methods --> Creating a Class and Methods

## [Step 1]
####### Create a Rules class, n order for your code to run, you have to have something in your class — For now, make the body of your class pass. This will allow your code to run without error.

class Rules:
  pass

## [Step 2]
####### Give Rules a method washing_brushes that returns the string ---> "Point bristles towards the basin while washing your brushes." Since we’ve now given this class a method, we can remove the pass that we added in the previous step.

class Rules:
    def washing_brushes(self):
        return("Point bristles towards the basin while washing your brushes.")