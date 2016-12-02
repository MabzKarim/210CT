def depth_first_search(graph, initial):
    """ This functions visits each vertex in turn, finds the first edge and follows to reach unvisited vertex """
    seen = []
    #all the vertxs that have been visited
    stack = [initial, ]
    #placed the first node within the stack

    while stack:
        vertx = stack.pop()
        #takes the first item within the vertex

        if vertx not in seen:
            seen.append(vertx)
            stack.extend([x for x in graph[vertx] if x not in seen])
            #if the vertex is not visited, then it will return
    return seen
    # returns the visited vertexs

def breadth_first_search(graph, initial):
    """ this functions searchs every edge in order to move onto the next vertex """
    seen = []
    #all the vertxs that have been visited
    list = [initial, ]
    #placed the first node within the list

    while list:
        vertx = list.pop(0)

        if vertx not in seen:
            seen.append(vertx)
            list.extend([x for x in graph[vertx] if x not in seen])
    return seen
# returns the visited vertexs, shortest path

def add_edge(graph,vertx1,vertx2):
    if vertx1 in graph:
        graph[vertx1].append(vertx2)
        graph[vertx2].append(vertx1)
    else:
        graph[vertx1] = [vertx2]
        graph[vertx2].append(vertx1)
        
def add_vertx(graph, vertx):
    if vertx not in graph:
        graph[vertx] = []

graph = {0: [1,2,5],
         1: [2,3,4,5],
         2: [0,1,5],
         3: [1,4,6],
         4: [1,3],
         5: [0,1,2,6],
         6: [3,5]
}

add_vertx(graph,7)
add_edge(graph,7,3)

print(depth_first_search(graph,0))
print(breadth_first_search(graph,0))


