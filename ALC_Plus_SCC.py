from collections import defaultdict
from itertools import chain, combinations

#Vertex indexing from '0'.

vertices = int(input())
# This input takes the number of vertices 

edges=[]
for _ in range(int(input())):
    s,t,lab = map(int,input().split())
    edges.append((s,t,lab))
# The edges variable contains all the edges along with the label in the main Graph.

labels=[]
for _ in range(int(input())):
    labels.append(input())
# The labels variable stores all the labels in the mainGraph 

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
# The powerset function returns all the subset of the list of elements in the iterable variable passed into it as an argument

subs = set(powerset(labels))
subs.remove(())
# subs contains all the (2**l-1) elements that are a subset of the the list of labels, the one excluded is the empty set

def sub_graph(subs, edges):
    G={}
    for sub_labels in subs:
        vert_in_subgraph=[]
        edg_in_subgraph=[]
        for edge in edges:
            if edge[2] in sub_labels:
                vert_in_subgraph.append(edge[0])
                vert_in_subgraph.append(edge[1])
                edg_in_subgraph.append(edge)
        G[sub_labels]=[vert_in_subgraph,edg_in_subgraph]
    return G


   
#This class represents a directed graph using adjacency list representation
class Graph:
   
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
   
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
   
    # A function used by DFS
    def DFSUtil(self,v,visited, lst):
        # Mark the current node as visited and print it
        visited[v]= True
        lst.append(v)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited, lst)
  
  
    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited 
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
      
  
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
  
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
  
   
   
    # The main function that finds and prints all strongly
    # connected components
    def printSCCs(self):
        xor=[]
          
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
  
        # Create a reversed graph
        gr = self.getTranspose()
           
         # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)
  
         # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i]==False:
                c=[]
                gr.DFSUtil(i, visited, c)
            xor.append(c)
        return xor

                

                

def constructing_SCC_subgraph(vertices, G, sub_lab):
    iden={}
    g = Graph(vertices)
    for i in range(len(G[sub_lab][1])):
        g.addEdge(i[0], i[1])
    SCC = g.printSCCs()
    new_vert=[]
    for i in range(len(SCC)):
        for j in SCC[i]:
            iden[j] = i
        new_vert.append(i)
    d={}
    for edge_labels in G[sub_lab][1]:
        if iden[edge_labels[0]]!=iden[edge_labels[1]]:
            if iden[edge_labels[0]] in d.keys():
                d[iden[edge_labels[0]]].append(edge_labels[1])
            else:
                d[iden[edge_labels[0]]]=[edge_labels[1]]
    return d,new_vert,iden
#Created a sub-graph of the sub-graph that was created during the ALC implementation, each SCC is named as a vertex and all the vertices that are a part of that SCC has been assigned an id that is equal to the vertex that the SCC has been named.

def Query_ALC_Plus_SCC(s,t,l,G):
    global vertices
    dct, new_vertices, identities = constructing_SCC_subgraph(vertices, G, l)
    if identities[s]==identities[t]:
        return True
    if identities[s] not in d.keys():
        return False
    #This means there is no outgoing edges from the SCC that contains the vertex 's' and hence it won't be able to connect to 't'.
    status={}
    for vart in range(vertices):
        status[vart]=False
    queue=[]
    queue.append(s)
    while q!=[]:
        u = q.pop(0)
        status[u]=True
        if u==t:
            return True
        for eg in G[l][1]:
            if eg[0]==u and status[eg[1]]==False:
                q.append(eg[1])
    return False

# The querying algo constructs the subgraph of the subgraph and sees if the identities of the two vertices are same or not that is if they are part of the same SCC, else a normal BFS run is performed




    








