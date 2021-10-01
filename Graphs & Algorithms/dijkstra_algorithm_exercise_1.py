# DIJKSTRA'S ALGORITHM: PYTHON Exercise ---> Understanding graphs in Python

#### LESSON  
#--------- This basically is the concept that we can use a dictionary to store nodes and costs ... which is very helpful
#------- Dictionary {key:value} ---> {node (i.e. vertices): cost} in the example below

## [Step 1]
####### There's code already provided

graph = {
  'A': [('B', 10), ('C', 3)],
  'B': [('C', 3), ('D', 2)],
  'C': [('D', 2)],
  'D': [('E', 10)],
  'E': [('B', 15)],
}


for vertex in graph:
  print("\n\nVertex {0} connects to: ".format(vertex))
  for edge in graph[vertex]:
    print("vertex {0} with a weight of {1}".format(edge[0], edge[1]))


## [Step 2]
####### Run the code to see the different vertices and edges of the graph. Try adding and removing edges and see how it effects the graph!

#------ it prints out the following
# Vertex A connects to:
# vertex B with a weight of 10
# vertex C with a weight of 3


#Vertex B connects to:
#vertex C with a weight of 3


#Vertex C connects to:
#vertex D with a weight of 2


#Vertex D connects to:
#vertex E with a weight of 10


#Vertex E connects to:
#vertex B with a weight of 15