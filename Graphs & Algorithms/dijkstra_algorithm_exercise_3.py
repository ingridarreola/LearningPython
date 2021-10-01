# DIJKSTRA'S ALGORITHM: PYTHON Exercise ---> Initializing Dijkstra's Algorithm

#### LESSON  
#--------- This breaks down how the algorithm works, creating the function dijkstras which takes two parameters: 'graph' & 'start'
#------- We use an empty dictionary at the beginning: 'distance'
#----- We use a for loop to loop through each vertex in the graph, and then we add keys to the empty dictionary in the process 
#----- Finally we add a tuple, which represents the start vertex

#####-------------------------------------------------------------
###----------------------------------------------------
####### There's code already provided .... need to define the algorithm
## [Step 1]

###### Define a function dijkstras() with two parameters: graph (the graph in question) and start (the start vertex).
#            - Inside the function body, define distances as an empty dictionary. We will keep track of all the shortest distances in this
#            - Return distances. We’ll build out the rest of the function body between these two lines.

from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }


# Define dijkstras() below:
def dijkstras(graph, start):
  return distances


## [Step 2]
# Above your return statement: 
#     - Loop through each vertex in graph and set its corresponding value within distances equal to inf. 
#     - Set distances[start] equal to 0 because the distance from the start vertex to the start vertex is 0

def dijkstras(graph, start):
  distances = {} # empty dictionary, we'll keep track of all the shortest distances in this
  for vertex in graph:
    distances[vertex] = inf #adding in the [key]=value to the empty dictionary
  distances[start] = 0 #adding the [key]=value to the empty dictionary
  return distances

## [Step 3]
# Still above the return statement, create a variable vertices_to_explore and assign to it a list with one element inside: a tuple of 0 and start. 
# This tuple represents the start vertex within the min-heap list.

def dijkstras(graph, start):
  distances = {} # empty dictionary, we'll keep track of all the shortest distances in this
  for vertex in graph:
    distances[vertex] = inf #adding in the [key]=value to the empty dictionary
  distances[start] = 0 #adding the [key]=value to the empty dictionary
  vertices_to_explore = [(0, start)] #create a variable and assign to it a list with one element inside: a tuple of 0 and start. The tuple represents the start vertex within the min-heap list
  return distances