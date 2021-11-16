# Exercise on Queues in Python
# Now, we can use Python to build out a Queue class with those three essential queue methods:
# [1]  enqueue() which will allow us to add a new node to the tail of the queue
# [2]  dequeue() which will allow us to remove a node from the head of the queue and return its value
# [3]  peek() which will allow us to view the value of head of the queue without returning it


### Step 1: create a Queue class with an __init__() method. Inside the method:
# set an instance property head equal to None
# set another instance property tail equal to None

class Queue:
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail

# Step 2: Below __init__(), define another method peek() that returns the value of the stack’s head using the Node method get_value().
  def peek(self):
    return self.head.get_value()

###########
#########
##### the part below is editing what was done previously in class Queue
####
###
##

# Add a new parameter max_size to your __init__() method that has a default value of None. Inside the method:
###   create a max_size instance variable assigned to max_siz
###   create another instance variable size and set it equal to 0

class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

# Inside Queue define a new method get_size() that returns the size instance property.
  # Define get_size() and has_space() below:
  def get_size(self):
    return self.size

# Below get_size(), define another method has_space(). Inside the method, check if a self.max_size has been set.
##   If there’s no max_size set, then we will always have space in the queue, so we can return True
##   If so, return True if the max_size is greater than self.get_size()
  def has_space(self):
    if self.max_size == None: #if there's no max_size set we have space in the queue and we can return True
      return True
    else: #if so, return True if the max_size is greater than self.get_size()
      return self.max_size > self.get_size()

# Define another method is_empty for Queue. The method should return True if the queue is empty (if the size of the queue is 0).
  def is_empty(self):
    if self.size == 0:
      return True
    else:
      return False

# Now we’ll make sure we aren’t attempting to peek() on an empty queue. After all, a deli server can’t get an order from a line with no customers! At the top of your peek() method body, use get_size() to see if the queue is empty.
#### if so, the method should just print “Nothing to see here!
#### if not, peek() will perform the same as it did before
  #### peek method is inserted before the above ... just going to put the entire thing again to avaoid confusion
  #### final code below



class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

  def peek(self): #let's make sure we're not attempting to peek() on an empty queue
    if self.size > 0: #check to see if the queue is empty
      return self.head.get_value() #if not empty then perform as it did before
    else:
      print("Nothing to see here!") #if its empty print this

  def get_size(self): # Inside Queue define a new method get_size() that returns the size instance property.
    return self.size

  def has_space(self): # Below get_size(), define another method has_space(). Inside the method, check if a self.max_size has been set.
    if self.max_size == None: #if there's no max_size set we have space in the queue and we can return True
      return True
    else: #if so, return True if the max_size is greater than self.get_size()
      return self.max_size > self.get_size()
  
  def is_empty(self): # Define another method is_empty for Queue. The method should return True if the queue is empty (if the size of the queue is 0).
    if self.size == 0:
      return True
    else:
      return False
      