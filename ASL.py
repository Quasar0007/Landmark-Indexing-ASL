from collections import defaultdict
from itertools import chain, combinations

vertices = int(input())
# This input takes the number of vertices, 0-based vertex indexing is followed.

edges=[]
for _ in range(int(input())):
    s,t,lab = map(str,input().split())
    s=int(s)
    t=int(t)
    edges.append((s,t,lab))
# The edges variable contains all the edges along with the label in the main Graph.

labels=[]
for _ in range(int(input())):
    labels.append(input())
# The labels variable stores all the labels in the mainGraph 

z=int(input())
#z is the number of landmark vertices that a subset should have.

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
# The powerset function returns all the subset of the list of elements in the iterable variable passed into it as an argument

subs = set(powerset(labels))
subs.remove(())
# subs contains all the (2**l-1) elements that are a subset of the the list of labels, the one excluded is the empty set

def sub_graph(subs, edges):
    # print(subs,edges)
    G={}
    for sub_labels in subs:
        vert_in_subgraph=[]
        edg_in_subgraph=[]
        for edge in edges:
            if edge[2] in sub_labels:
                vert_in_subgraph.append(edge[0])
                vert_in_subgraph.append(edge[1])
                edg_in_subgraph.append(edge)
        if len(sub_labels)==1:
            G[sub_labels[0]]=[list(set(vert_in_subgraph)),edg_in_subgraph]
        else:
            G[sub_labels]=[list(set(vert_in_subgraph)),edg_in_subgraph]
    # print(G['b'])
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
    degrees={}
    iden={}
    g = Graph(vertices)
    # print(G[sub_lab][1])

    for i in range(len(G[sub_lab][1])):
        g.addEdge(G[sub_lab][1][i][0], G[sub_lab][1][i][1])

    SCC = g.printSCCs()
    # print(SCC)

    new_vert=[]
    for i in range(len(SCC)):
        for j in SCC[i]:
            iden[j] = i
        new_vert.append(i)
        degrees[i]=0
    d={}
    for edge_labels in G[sub_lab][1]:
        # print(edge_labels)

        if iden[edge_labels[0]]!=iden[edge_labels[1]]:
            if iden[edge_labels[0]] in d.keys():
                d[iden[edge_labels[0]]].append(iden[edge_labels[1]])
            else:
                d[iden[edge_labels[0]]]=[iden[edge_labels[1]]]
            degrees[iden[edge_labels[0]]]+=1
    # print(d,new_vert,iden)

    return d,new_vert,iden,degrees
#Constructed a sub-graph of the sub-graph that was created during the ALC implementation, each SCC is named as a vertex and all the vertices that are a part of that SCC has been assigned an id that is equal to the vertex that the SCC has been named. The vertex indexing starts

# No need for indexing algorithm, dictionary handles it .

def Landmark_Query(id_of_s,id_of_t,dct):
	if id_of_s==id_of_t:
		return True
	if id_of_s not in dct.keys():
		return False
	else:
		for w in dct[id_of_s]:
			if w==id_of_t:
				return True
		return False

def Query_ASL(s,t,L):
    global Indexed
    global subs
    global edges
    global vertices
    global z
    G=sub_graph(subs, edges)
    #G is the subgraph that was constructed in the ALC part.

    dct, new_vertices, identities, degs = constructing_SCC_subgraph(vertices, G, L)
    for v in new_vertices:
        if v not in dct.keys():
            dct[v]=[]
    # print(dct, identities)

    deg_list=[]
    for i in new_vertices:
        deg_list.append((i,degs[i]))
    sorted_deg_list = sorted(deg_list, key=lambda x:x[1])
    #sorted_deg_list contains all the keys that are sorted on the basis of their values, that is, their degrees in our case.

    landmark_vertices=[]
    Indexed={}
    for (vertex,deg) in sorted_deg_list[::-1]:
        if z>0:
            landmark_vertices.append(vertex)
            Indexed[vertex]=True
            z-=1
        else:
            break
    #This loop chooses 'z' landmark vertices out of all the vertices in a sub-graph with a given label and returs true as there indexing.
    # print(Indexed)

    id_of_s = identities[s]
    id_of_t = identities[t]
    if id_of_s in Indexed.keys():
        return Landmark_Query(id_of_s,id_of_t,dct)
    status={}
    for vert in new_vertices:
        status[vert]=False
    q = []
    q.append(id_of_s)
    while q!=[]:
        u = q.pop(0)
        status[u]=True
        if u==id_of_t:
            return True
        if u in Indexed.keys():
            return Landmark_Query(u,id_of_t,dct)
        for w in dct[u]:
            if status[w]==False:
                q.append(w)
    return False

source_vertex = int(input())  #The vertex should be indexed on the basis of 0-indexing.
target_vertex = int(input())  #The vertex should be indexed on the basis of 0-indexing.

label_between_vertices= tuple(map(str,input().split()))

if len(label_between_vertices)==1:
    label_between_vertices=label_between_vertices[0]
# print(label_between_vertices)

print(Query_ASL(source_vertex,target_vertex,label_between_vertices))