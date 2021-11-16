# A* Algorithm- ---> Euclidean heuristic Build

#### LESSON  
#--------- Not all vertices are on a grid and sometimes the shortest distance is closer to a direct diagonal line between two points. For these situations, a Manhattan heuristic would overestimate the total distance, making it inadmissible; the Euclidean heuristic would be a better fit.
            #what we are finding is essentially a hypotenuse of a right triangle; the other two sides would be the x-distance and the y-distance
            ## However, there are trade-offs for the more exact calculation. The Euclidean heuristic’s square root calculation slows the runtime.

## [Step 0]
####### Starting with the code below

from math import inf, sqrt
from heapq import heappop, heappush
from euclidean_graph import euclidean_graph, bengaluru, jaipur

# Change heuristic() below:
def heuristic0(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return x_distance + y_distance

def a_star0(graph, start, target):
  print("Starting A* algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]
  while vertices_to_explore and paths_and_distances[target][0] == inf:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight + heuristic(neighbor, target)
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]

# Call a_star() on euclidean_graph to find the best route
# from jaipur to bengaluru:


## [Step 1]
####### Go to heuristic() and change the return statement so that x_distance and y_distance are each squared.
# Make sure you run your code before moving on to the next checkpoint.

