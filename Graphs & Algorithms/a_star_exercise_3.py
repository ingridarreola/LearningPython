# A* Algorithm- ---> Heuristic Time

#### LESSON  
#--------- So far we've just modified Dijkstra's algorithm that has a target and returns the path to the target. 
# To make this algorithm truly ~~a star~~ A*, you’ll need to add a ***heuristic*** that **estimates the distance from a given vertex to the target**.

## [Step 0]
####### Starting with the code below
from math import inf
from heapq import heappop, heappush
from manhattan_graph import manhattan_graph, thirty_sixth_and_sixth, grand_central_station

def modified_dijkstras(graph, start, target):
  print("Starting Dijkstra's algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
  print("Found a path in {0} steps: ".format(count), paths_and_distances[target][1])
  return paths_and_distances[target][1]

def heuristic(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return x_distance + y_distance

def a_star(graph, start, target):
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
        
  print("Found a path in {0} steps: ".format(count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]

## [Step 1] Scroll down to the bottom of the file and uncomment the code. Run it to see how Dijkstra’s path-finds in all directions, while A* uses its heuristic to focus the search in a particular direction.

modified_dijkstras(manhattan_graph, thirty_sixth_and_sixth, grand_central_station)

a_star(manhattan_graph, thirty_sixth_and_sixth, grand_central_station)


#------ it prints out the following for modified_dijkstras
#At 39th Street and Seventh Avenue

#At Penn Station

#At Morgan Library and Museum

#At Morgan Library and Museum

#At 34th Street and Madison Avenue

#At 33rd Street and Madison Avenue

#At 33rd Street and Madison Avenue

#At 40th Street and Madison Avenue

#At Bryant Park South

#At Kinokuniya

#At Kinokuniya

#At Grand Central Station
#Found a path in 39 steps:  ['36th Street and 6th Avenue', '37th Street and 6th Avenue', '37th Street and 5th Avenue', '38th Street and Fifth Avenue', '39th Street and Fifth Avenue', '40th Street and Fifth Avenue', '40th Street and Madison Avenue', '41st Street and Madison Avenue', 'Grand Central Station']

#------ it prints out the following for a_star
#Starting A* algorithm!

#At 36th Street and 7th Avenue

#At 36th Street and 5th Avenue

#At 35th Street and 6th Avenue

#At 37th Street and 6th Avenue

#At 35th Street and 6th Avenue

#At 35th Street and 6th Avenue

#At 36th Street and 5th Avenue

#At 36th Street and 5th Avenue

#At 36th Street and 5th Avenue

#At 36th Street and 7th Avenue

#At 36th Street and 7th Avenue

#At 36th Street and Madison Avenue

#At 36th Street and Madison Avenue

#At 37th Street and 7th Avenue

#At CUNY Graduate Center

#At CUNY Graduate Center

#At 38th Street and Fifth Avenue

#At 38th Street and Fifth Avenue

#At Macy's

#At Macy's

#At Macy's

#At 38th Street and Seventh Avenue

#At 39th Street and Fifth Avenue

#At Empire State Building

#At Empire State Building

#At Empire State Building

#At 38th Street and Madison Avenue

#At Manhattan Mall

#At Manhattan Mall

#At 39th Street and Seventh Avenue

#At Mexican Consulate General

#At 39th Street and Sixth Avenue

#At 41st Street and Madison Avenue

#At Bryant Park South

#At Bryant Park South
#Found a path in 35 steps:  ['36th Street and 6th Avenue', '37th Street and 6th Avenue', '37th Street and 5th Avenue', '38th Street and Fifth Avenue', '39th Street and Fifth Avenue', '40th Street and Fifth Avenue', '40th Street and Madison Avenue', '41st Street and Madison Avenue', 'Grand Central Station']