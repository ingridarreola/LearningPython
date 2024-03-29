# A* Algorithm---> Pathway to A Star-dom --> 

#### LESSON  
#---------  Fixing the paths_and_distance function by looping through new_path
# In the for loop adding in something for the new_path -- so that its equal to the path of the current_vertex and the neighbor.name
# In the if loop adding something for new_path -- set the corresponding path equal to new_path
# Returning the path of the target ... at the end of it all

## [Step 0]
# Starting out with A* Algorithm. Our function is breaking when called because we went from tracking only distance to tracking distance AND a path.

from math import inf
from heapq import heappop, heappush

def a_star0(graph, start, target):
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

# A graph and vertices for us to play around with:
class graph_vertex:
  def __init__(self, name, x, y):
    self.name = name
    self.position = (x, y)

delhi = graph_vertex("New Delhi", 28.6448, 77.216721)
jaipur = graph_vertex("Jaipur", 26.92207, 75.778885)
varanasi = graph_vertex("Varanasi", 25.321684, 82.987289)
mumbai = graph_vertex("Mumbai", 19.07283, 72.88261)
chennai = graph_vertex("Chennai", 13.067439, 80.237617)
hyderabad = graph_vertex("Hyderabad", 17.387140, 78.491684)
kolkata = graph_vertex("Kolkata", 22.572645, 88.363892)
bengaluru = graph_vertex("Bengaluru", 12.972442, 77.580643)

cities_graph = {
  delhi: set([(jaipur, 2.243918), (varanasi, 6.65902), (mumbai, 10.507479), (chennai, 15.867576), (hyderabad, 11.329626), (kolkata, 12.693718), (bengaluru, 15.676582)]),
  jaipur: set([(mumbai, 8.366539), (delhi, 2.243918)]),
  varanasi: set([(delhi, 6.65902), (mumbai, 11.88077)]),
  mumbai: set([(delhi, 10.507479), (jaipur, 8.366539), (varanasi, 11.88077), (hyderabad, 5.856898), (kolkata, 15.87195), (bengaluru, 7.699756)]),
  chennai: set([(delhi, 15.867576), (kolkata, 12.50541), (hyderabad, 4.659195), (bengaluru, 2.658671)]),
  hyderabad: set([(delhi, 11.329626), (mumbai, 5.856898), (chennai, 4.659195), (bengaluru, 4.507721), (kolkata, 11.151231)]),
  kolkata: set([(delhi, 12.693718), (mumbai, 15.87195), (chennai, 12.50541), (hyderabad, 11.151231), (bengaluru, 14.437532)]),
  bengaluru: set([(delhi, 15.676582), (mumbai, 7.699756), (chennai, 2.658671), (hyderabad, 4.507721), (kolkata, 14.437532)])
}
a_star(cities_graph, delhi, varanasi)

## [Step 1]
####### Below your infinity-setting for loop, anywhere you see paths_and_distances[some_variable_name], change it to paths_and_distances[some_variable_name][0] 
# This way, you only set and get the distance for those instances. Do NOT change the line you changed in the for loop though.

def a_star1(graph, start, target):
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
  
  return paths_and_distances

## [Step 2]
####### Jump down to where you set new_distance. Add a new line below and set new_path equal to the path of current_vertex with the addition of neighbor.name

def a_star2(graph, start, target):
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name] #set it equal to vertex, to its start and the neighbor.name
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
  
  return paths_and_distances

## [Step 3]
####### Take a look at paths_and_distances[neighbor][0] = new_distance. You’ve set the distance for neighbor in paths_and_distances.
            # Add a new line below to set the corresponding path equal to new_path

def a_star(graph, start, target):
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
        paths_and_distances[neighbor][1] = new_path #set the corresponding path equal to new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
  
  return paths_and_distances[target][1] # Returning the path of the target ... at the end of it all 
  # [Step 4] Finally, change your return statement so that it returns the path of target