import sys

class Graph:

    def __init__(self): #initialize set of nodes, and dictionary of edges#
        self.nodes = set()
        self.edges = {}

    def addNode(self, value): #add nodes to set#
        self.nodes.add(value)
        if value not in self.edges: #if not already in edges, create a new (empty) entry in the dictionary for it#
            self.edges[value] = []

    def addEdge(self, from_node, to_node, weight): #add edges and their respective weights to the dictionary, e.g. ('A':['B',5]) and ('B': ['A',5])
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

    def djikstraAlgorithm(self, start_node, end_node):
        unvisited_dict = {node: sys.maxsize for node in self.nodes} #initializes dictionary containing nodes as keys and infinity
        unvisited_dict[start_node] = 0                              #as tentative distance value to each node, excluding start_node#
        visited_nodes = {}
        current_node = start_node

        while unvisited_dict: #loop while unvisited dictionary is not empty#
            min_node = min(unvisited_dict, key=unvisited_dict.get) #finds the node with the smallest distance in unvisited dictionary#

            if min_node == sys.maxsize: #if the minimum tentative distance is still infinity, break as there are no valid paths left#
                break

            current_node = min_node
            current_weight = unvisited_dict[current_node]
            del unvisited_dict[current_node] #remove current node from unvisited list#

            for neighbor, weight in self.edges[current_node]:

                if neighbor in visited_nodes: #if neighbor has already been visited, ignore it#
                    continue 
                
                tentative_distance = current_weight + weight 
                if tentative_distance < unvisited_dict[neighbor]: #if the current tentative distance for that node is less than its 
                    unvisited_dict[neighbor] = tentative_distance #previous value, update the prev value to the current one#

            visited_nodes[current_node] = current_weight

        path = [] #initialize empty path list#

        if end_node in visited_nodes: #iterates backwards through shortest path and appends each node to the path list#
            while end_node != start_node:

                path.insert(0, end_node)

                #checks neighbors of current node and if they match the weight when subtracted from the current node#
                for neighbor, weight in self.edges[end_node]:
                    if neighbor in visited_nodes and visited_nodes[end_node] - visited_nodes[neighbor] == weight:

                        end_node = neighbor
                        break
            
            path.insert(0, start_node) #completes path list and returns it#
            return path
