from itertools import chain, combinations

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
# This creates a sub-graph for each label from all the subsets of the powerset of the edge labels. G contains as "key" the label-sets that represents a sub-graph and the value of the key contains the vertices that the graph contains as well as the edges that comes within that subgraph.

def QueryALC(s,t,ls):
	return Query_For_ALC(s,t,ls,G)

def Query_For_ALC(s,t,ls,G):
	unique_subgraph = G[ls]
	status={}
	for vert in unique_subgraph[0]:
		status[vert]=False
	queue=[]
	queue.append(s)
	while q!=[]:
		u = q.pop(0)
		status[u]=True
		if u==t:
			return True
		for eg in unique_subgraph[1]:
			if eg[0]==u and status[eg[1]]==False:
				q.append(eg[1])
	return False

# The querying algo checks only the subgraph corresponing to the given label and then a BFS run is performed in that subgraph to find if the target vertex is there and is reachable by the source vertex.





		
