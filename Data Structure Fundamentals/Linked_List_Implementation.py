#Let’s implement a linked list in Python. As you might recall, each linked list is a sequential chain of nodes. So before we start building out the LinkedList itself, we want to build up a Node class in Python that we can use to build our data containers. Remember that a node contains two elements:
##   data
##   a link to the next node#

# Define your Node class below:
class Node:
  def __init__(self,value, next_node=None):
    self.value = value
    self.next_node = next_node

#define .get_value() and .get_next_node() methods ... they should return the coresponding values from self 

  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node

#define .set_next_node() method that takes self and next_node as parameters and allows you to update the link to the next node

  def set_next_node(self,next_node):
    self.next_node = next_node

#Outside the Node class, create an instance of Node called my_node with a value of 44 & use .get_value() to print the value of my_node

my_node = Node(44)
print((my_node))