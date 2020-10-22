#import default dictionaries
from collections import defaultdict
#import the heap functions
from heapq import *

#define the function
def dij_algo(edges, begin_vertex, ending_vertix):
    #create empty dict
    dict_list = defaultdict(list)
    #Fill the empty dict with edges, vertices and distance
    for a,b,c in edges:
        dict_list[a].append((c,b))

    #Start with initial distance
    begin_distance = [(0,begin_vertex,())]
    #Create emtpy set for checked veritces
    checked = set()
    #find minimum initial distance
    min_distance = {begin_vertex: 0}
    
    #keep running until heap is done for
    while (begin_distance):
        #pop the distance from the heap and set it to the list
        (path_distance,vertex_1,vertex_path) = heappop(begin_distance)
        #if the vertex is already not in the checked list keep doing stuff
        if (vertex_1 not in checked):
            #add the vertex to the checked list
            checked.add(vertex_1)
            #update the vertex path
            vertex_path = vertex_path + (vertex_1, )
            #if the vertex is the same as the ending vertex, than we have found the shortest path and return it 
            if (vertex_1 == ending_vertix): 
                return (path_distance, vertex_path)
            #If the vertex is not the same as the ending vertex, do this for loop
            for adj_dist, vertex_2 in dict_list.get(vertex_1, ()):
                #if the vertex is already in the checked list then skip it
                if (vertex_2 in checked):
                     continue
                #set the previous distnace
                prev_distance = min_distance.get(vertex_2, None)
                #set the next distance
                next_distance = path_distance + adj_dist
                #update the min_distance and update the heap
                if (prev_distance is None or next_distance < prev_distance):
                    min_distance[vertex_2] = next_distance
                    heappush(begin_distance, (next_distance, vertex_2, vertex_path))
    return float("inf")

container = []
file_path =  input("Please enter file or file path:")
try:
    file_object = open(file_path,"r")
except:
    print("Please enter valid file or path name")
contents = file_object.readlines()
counter = 0
for i in contents:
    if(counter < 1):
        counter = counter + 1
        continue
    else:
        container.append((i.split()[0],i.split()[1],int(i.split()[2])))


output = dij_algo(container, "A", "B")
print(output[0])
result_string = ""
for i in output[1]:
    result_string = result_string + i + " "
print(result_string)
