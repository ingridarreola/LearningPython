# DIJKSTRA'S ALGORITHM: PYTHON Exercise ---> Understanding Heapq (Heap Queue)

#### LESSON  
#--------- This breaks down how the algorithm works, since it uses heaps
#------- Heaps have two main methods that are used in this algorithm: 'heappush' & 'heappop'
#----- heappush in the beginnning adds the values
#----- heappop at the end returns the smallest values which have been added to the heap

## [Step 1]
####### There's code already provided .... at the top of the file place 'import heapq'

#Write Import Statement here
import heapq


heap = [(0, 'A')]
heapq.heappush(heap, (1, 'B'))
heapq.heappush(heap, (-5, 'D'))
heapq.heappush(heap, (4, 'E'))
heapq.heappush(heap, (2, 'C'))

print("The smallest values in the heap in ascending order are:\n")
while heap:
  print(heapq.heappop(heap))


## [Step 2]
####### Run the code to see the what happens

#------ it prints out the following

# The smallest values in the heap in ascending order are:
# 
# (-5, 'D')
# (0, 'A')
# (1, 'B')
# (2, 'C')
# (4, 'E')