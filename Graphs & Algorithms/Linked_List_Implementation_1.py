# With the Node in hand, we can start building the actual linked list. Depending on the end-use of the linked list, a variety of methods can be defined.

#For our use, we want to be able to: get the head node of the list (it’s like peeking at the first item in line)
###   add a new node to the beginning of the list
###   print out the list values in order
###   remove a node that has a particular value

# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Create your LinkedList class below:
# create an empty LinkedList class.
# Define an .__init__() method for the LinkedList. We want to be able to instantiate a LinkedList with a head node, so .__init__() should take value as an argument. Make sure value defaults to None if no value is provided. 
### Inside the .__init__() method, set self.head_node equal to a new Node with value as its value.

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
# Define a .get_head_node() method that helps us peek at the first node in the list.
  def get_head_node(self):
    return self.head_node

# So far we can:
##  create a new LinkedList using .__init__()
##  get the head node of the list using .get_head_node()
#------
###### Next up, we’ll define methods for our LinkedList class that allow us to:
#######   insert a new head node
#######   return all the nodes in the list as a string so we can print them out in the terminal!

#[1] Define an .insert_beginning() method which takes new_value as an argument.
# -Inside the method, instantiate a Node with new_value. Name this new_node.
# -Now, link new_node to the existing head_node.
# -Finally, replace the current head_node with new_node.

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node) 
    self.head_node = new_node

# [2] Define a .stringify_list() method we can use to print out a string representation of a list’s nodes’ values.
# The method should traverse the list, beginning at the head node, and collect each node’s value in a string. Once the end of the list has been reached, the method should return the string.
# You can use str() to convert integers to strings! 
# Be sure to add "\n" between values so that each value prints on a new line.

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

# [3] Test your code by uncommenting the print statement at the bottom of script.py — did your list print what you expected?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

#Nice! Now we have a bunch of helpful LinkedList methods under our belt.
# The final use case we mentioned was the ability to remove an arbitrary node with a particular value. This is slightly more complex, since a couple of special cases need to be handled.

# [1] At the bottom of script.py, add a .remove_node() method to LinkedList. It should take value_to_remove as a parameter. We’ll be looking for a node with this value to remove.
# In the body of .remove_node(), set a new variable current_node equal to the head_node of the list.
# We’ll use current_node to keep track of the node we are currently looking at as we traverse the list.
def remove_node(self, value_to_remove):
  current_node = self.get_head_node()
# [2] Still inside the method body, use an if statement to check whether the list’s head_node has a value that is the same as value_to_remove. If it does, we’ve found the node we’re looking for and we need to adjust the list’s pointer to head_node. Inside the if clause, set self.head_node equal to the second node in the linked list.
  if current_node.get_value() == value_to_remove:
    self.head_node = current_node.get_next_node()
# [3] Add an else clause. Within the else clause: **Traverse the list until current_node.get_next_node().get_value() is the value_to_remove. **(Just like with stringify_list you can traverse the list using a while loop that checks whether current_node exists.)
# ** When value_to_remove is found, adjust the links in the list so that current_node is linked to next_node.get_next_node(). 
# ** After you remove the node with a value of value_to_remove, make sure to set current_node to None so that you exit the loop.
  else:
    while current_node: #traverse the list with while loop that checks whether current_node exists
      next_node = current_node.get_next_node()
      if next_node.get_value() == value_to_remove: #when value_to_remove is found, adjust the links in list so current_node is linked
        current_node.set_next_node(next_node.get_next_node())
        current_node = None #after removing the node with a value of value_to_remove, set current_node to None to exit the loop
      else:
        current_node = next_node

# Here are some ideas:

#Create a few nodes and adding them to a new linked list
#Print your linked list out by using your stringify_list() method
#Remove your linked list’s head node
#Print your list again — was your original head node removed?
#So far you’ve built a method to remove the first occurrence of a given value. How do you think you would remove all nodes that have a specific value? Try building a method to do that!
