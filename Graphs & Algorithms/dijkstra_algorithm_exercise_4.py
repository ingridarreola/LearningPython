# DIJKSTRA'S ALGORITHM: PYTHON Exercise ---> Finishing Dijkstra's Algorithm

#### LESSON  
#--------- setup a while loop to check if there were unexplored vertices remaining then assigned current_distance & current_vertex equal to heappop(vertices_to_explore), the vertex with the minum distance from start
#------- next inside that same while loop created a  for loop...to iterate over each neighbor and cost of the current_vertex in the graph. New_Distance is our heuristic (i.e. cost + current distance)
#----- Finally inside the while loop .. for loop .. created an if statement to check if the new_distance was less than the distance recorded for the neighbor. Neighbor was added to the empty dictionary.
#----- 

#####-------------------------------------------------------------
###----------------------------------------------------
####### There's code already provided .... need to define the algorithm
## [Step 1]
############# Below where you set vertices_to_explore but before the return statement:
#### - Set up a while loop that runs as long as vertices_to_explore is truthy (i.e., there are unexplored vertices remaining).
#### - Inside the while loop, use multiple assignment to set current_distance and current_vertex equal to heappop(vertices_to_explore) — this will always be the vertex with the minimum distance from start.

from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }

def dijkstras(graph, start):
  distances = {} 
  for vertex in graph:
    distances[vertex] = inf 
  distances[start] = 0 
  vertices_to_explore = [(0, start)] 
  # Finish dijkstras() below:
 while vertices_to_explore: #while loop that runs as long as vertices_to_explore is truthy (i.e., there are unexplored vertices remaining)
    current_distance, current_vertex = heappop(vertices_to_explore)
  return distances

distances_from_a = dijkstras(graph, 'A')
print("\n\nShortest Distances: {0".format(distances_from_a))

## [Step 2]
### In the while loop, below where you set current_distance and current_vertex:
###    - Create a for loop to iterate over each neighbor and edge_weight of current_vertex in graph.
###    - In the for loop, set new_distance equal to the sum of current_distance and the edge_weight to neighbor.

 while vertices_to_explore: 
    current_distance, current_vertex = heappop(vertices_to_explore)
    # Finish dijkstras() below:
    for neighbor, edge_weight in graph[current_vertex]: ## for loop to iterate over each neighbor and edge_weight of current_vertex in graph
      new_distance = current_distance + edge_weight ## set new_distance equal to the sum of current_distance and the edge_weight to neighbor
        
  return distances

 ## [Step 3]
### inside the for loop, create an if statement that checks if the new_distance is less than the distance recorded for that neighbor in the distances dictionary
###    - Set distances[neighbor] equal to new_distance
###    - IUse heappush() to push a tuple of new_distance and neighbor onto vertices_to_explore

 while vertices_to_explore: 
    current_distance, current_vertex = heappop(vertices_to_explore)
    # Finish dijkstras() below:
    for neighbor, edge_weight in graph[current_vertex]: 
      new_distance = current_distance + edge_weight 
      if new_distance < distances[neighbor]: #if statement that checks if the new_distance is less than the distance recorded for that neighbor in the distances dictionary
        distances[neighbor] = new_distance # creating neighbor in the dictionary, setting it equal to the new distance
        heappush(vertices_to_explore, (new_distance, neighbor)) # push a tuple of new_distance and neighbor onto vertices_to_explore
  return distances


  ############ FINAL BELOW
  ##########
  from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
  distances = {}
  for vertex in graph:
    distances[vertex] = inf
  distances[start] = 0
  vertices_to_explore = [(0, start)]
  
  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    # Finish dijkstras() below:
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
        
  return distances
        
distances_from_a = dijkstras(graph, 'A')
print("\n\nShortest Distances: {0}".format(distances_from_a))

####### Run the code to see the what happens

#------ it prints out the following
# Shortest Distances: {'A': 0, 'C': 3, 'D': inf, 'E': inf, 'B': 10}