# A* Algorithm---> Creating A* --> Modifying Dijkstra's algorithm ... with the heuristic

#### LESSON  
#--------- We modified Dijkstra's algorithm from the previous exercises with important things. We've made changes: included a target to find (in the a_start function). 
# Renamed all distances to paths_and_distances .. the variable will keep track of each path now. 
# Finally, inside the for loop, changed the value mapped to vertex to a list ... with inf (distance) and start.name (path)

## [Step 0]
# Starting out with Dijkstra’s algorithm (previous python exercises)

## [Step 1]
####### Add target as the final parameter for a_star(). Make sure to run this code before moving onto the next checkpoint.

from math import inf
from heapq import heappop, heappush

def a_star1(graph, start, target):
  distances = {}
  for vertex in graph:
    distances[vertex] = inf
  
  distances[start] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
  
  return distances

## [Step 2]
####### Rename ALL instances of distances within a_star() to paths_and_distances. We’ll use this variable to keep track of each path too now.

def a_star2(graph, start, target):
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = inf
  
  paths_and_distances[start] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < paths_and_distances[neighbor]:
        paths_and_distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
  
  return paths_and_distances

  ## [Step 3]
####### Inside the for vertex in graph loop, change the value mapped to vertex to a list of: 
        # - inf (This will be the distance.) 
        # - a list containing start.name (This will be the path, starting with the first vertex.)

def a_star3(graph, start, target):
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < paths_and_distances[neighbor]:
        paths_and_distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
  
  return paths_and_distances