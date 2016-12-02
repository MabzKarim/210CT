def add_edge(graph,vertx1,vertx2):
    """ function to add a node onto the graph """
    if vertx1 in graph:
        graph[vertx1].append(vertx2)
        graph[vertx2].append(vertx1)
        #it will create an edge between the two vertex's already on the graph
    else:
        graph[vertx1] = [vertx2]
        graph[vertx2].append(vertx1)
        #if not already in graph, it will created a new edge on the graph for the new vertexs

def add_vertx(graph, vertx):
    """ function to add an edge onto the graph """
    if vertx not in graph:
        graph[vertx] = []
        #creates a new vertex in the graph within an empty stack

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
#will create a new vertex of 7, and connect between vertex 3

print (graph)


