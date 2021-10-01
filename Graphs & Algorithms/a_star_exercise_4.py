# A* Algorithm- ---> Heuristic Build

#### LESSON  
#--------- we’ll start with the Manhattan heuristic. This heuristic is only considered admissible — meaning that it never overestimates the distance in reaching the target — in a grid system in which the search can only move up, down, left, or right.
# To get the heuristic estimate we need to:
        # Measure the distance between the two vertices’ x positional values and between their y positional values.
        # Return the sum of the x distance and y distance together.

## [Step 0]
####### Starting with the code below
from math import inf
from heapq import heappop, heappush
from manhattan_graph import manhattan_graph, penn_station, grand_central_station


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
      new_distance = current_distance + edge_weight
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]

# Call a_star() on manhattan_graph to find the best route
# from penn_station to grand_central_station:

## [Step 1]
### Define a function heuristic() with two parameters: start and target.

# Define heuristic below:
def heuristic1(start, target):

def a_star1(graph, start, target):
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
      new_distance = current_distance + edge_weight
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]

## [Step 2]
#### In the function body, create a variable x_distance and set it equal to the absolute value of the target’s x value subtracted from start‘s x value.
        # Create a variable y_distance in the same way.

def heuristic2(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])


## [Step 3]
#### Return the sum of x_distance and y_distance from the function.
def heuristic3(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return x_distance + y_distance

## [Step 4]
#### Time to add the heuristic into a_star() so that distance is factored in!
###    Go to the line of a_star() where new_distance is defined. Set new_distance equal to the sum of:
            ## current_distance
            ## edge_weight
            ## an invocation of heuristic() with neighbor and target as arguments (this estimates the distance between neighbor and target)

def heuristic4(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return x_distance + y_distance

def a_star4(graph, start, target):
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
      new_distance = current_distance + edge_weight + heuristic(neighbor, target) #adding heuristic in here, to estimate distance between neighbor and target
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]

## [Step 5]
#### Congrats! You’ve implemented A* using the Manhattan heuristic. 
        # Try calling the function on the graph provided find the best path from Penn Station to Grand Central Station in Manhattan!

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
      new_distance = current_distance + edge_weight + heuristic(neighbor, target) #adding heuristic in here, to estimate distance between neighbor and target
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]

  # Call a_star() on manhattan_graph to find the best route
# from penn_station to grand_central_station:

a_star(manhattan_graph, penn_station, grand_central_station)


#------ it prints out the following for a_star
#Starting A* algorithm!

#At 34th Street and 7th Avenue

#At 34th Street and 7th Avenue

#At Manhattan Mall

#At Manhattan Mall

#At Macy's

#At Herald Square

#At Herald Square

#At 33rd Street and 5th Avenue

#At 36th Street and 7th Avenue

#At 35th Street and 6th Avenue

#At 35th Street and 6th Avenue

#At Empire State Building

#At 33rd Street and Madison Avenue

#At 36th Street and 6th Avenue

#At 36th Street and 6th Avenue

#At CUNY Graduate Center

#At 34th Street and Madison Avenue

#At 37th Street and 6th Avenue

#At 37th Street and 6th Avenue

#At 36th Street and 5th Avenue

#At 35th Street and Madison Avenue

#At 38th Street and Sixth Avenue

#At 38th Street and Sixth Avenue

#At 37th Street and 5th Avenue

#At 36th Street and Madison Avenue

#At 39th Street and Sixth Avenue

#At 39th Street and Sixth Avenue

#At 38th Street and Fifth Avenue

#At Times Square

#At Morgan Library and Museum

#At Morgan Library and Museum

#At 39th Street and Fifth Avenue

#At Times Square - North

#At 38th Street and Madison Avenue

#At Bryant Park North

#At Mexican Consulate General

#At New York Public Library

#At 41st Street and Madison Avenue

#At 41st Street and Madison Avenue
#Found a path from Penn Station to Grand Central Station in 39 steps:  ['Penn Station', '34th Street and 7th Avenue', "Macy's", '36th Street and 7th Avenue', '37th Street and 7th Avenue', '38th Street and Seventh Avenue', '39th Street and Seventh Avenue', 'Times Square - South', 'Times Square', 'Times Square - North', 'Bryant Park North', 'New York Public Library', 'Grand Central Station']