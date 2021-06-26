from collections import Counter

global labels
#labels will be the list of all labels that we have

# We have to represent the graph using Adjacency List using a dictionary
Adjacency_List_For_Representation = {}

# To calculate the degree of each vertex, we use a 'dictionary' 
degree = {}

# 'vertices' is the list of all the vertices that we have 
for node in vertices:
	Adjacency_List_For_Representation[node] = []
	# Initializing each vertex with the value of an empty list to add the other node it is connected with

	degree[node] = 0

# 'edges' is the set of all the directed edges along with the labels that we have been given.
for (u,v,l) in edges:
	Adjacency_List_For_Representation[u].append((v,l))

	# The loop from lines 10&11 adds all the vertices that are directly connected to a given vertex/node along with their labels.
	# Here, the label could also be a set

	degree[u]+=1
	degree[v]+=1

	# Increment the degree of each vertex since each outgoing as well as incoming edge count towards the increase in degree of the vertex

def Landmark_Index_Plus(degree, Adjacency_List_For_Representation, k, b):
	degree_list = []
	#To store the vertices and their degrees in a list so that we can sort it later

	for key in degree.keys():
		degree_list.append((key,degree[key]))
	#Sorting keys and their degrees as a tuple in list.

	sorted_degree_list = sorted(degree_list, key=lambda x:x[1])
	#sorted_degree_list contains all the keys that are sorted on the basis of their values, that is, their degrees in our case.

	landmark_vertices=[]
	non_landmark_vertices=[]
	#List to store all the 'k' landmark vertices and the remaining non-landmark vertices

	while ((vertex,deg) in sorted_degree_list[::-1]) and k>0 :
		landmark_vertices.append(vertex)
		k-=1
	#The while loop from 40 to 42 helps us to store the 'k' landmark vertices with the highest degree.

	Indexed = {}
	for v in Adjacency_List_For_Representation.keys():
		Indexed[v]= False
	#Set the index of all the vertices to False to represent which vertices has been indexed and which one hasn't been
	L_ind={}
	NL_Ind={}
	Reachable_By = {}
	
	for i in landmark_vertices:
		L_Ind[i]=[]
		Reachable_By[i]=[]
		LabeledBFSPerLM_Plus(i)
	#L_Ind(i) will store all the (w,L)(in tuple form only) belonging to V*2^L , such that w is reachable to 'v' via the minimal labeled set 'L' using the procedure LabeledBFSPerLM_Plus. It is only for the landmark vertices.
	#Reachable_By(s) stores all the vertices reachable by vertex 's' along with the label that it has.

	for (vertex, deg) in sorted_degree_list[::-1][k:]:
		non_landmark_vertices.append(vertex)
	#By the help of this loop, we store all the non-landmark vertices of the graph.

	for i in non_landmark_vertices:
		NL_Ind[i] = []
		LabeledBFSPerNonLM(i, b)
			#NL_Ind(i) will store all the (w,L)(in tuple form only) belonging to V*2^L , such that w is reachable to 'v' via the minimal labeled set 'L' using the procedure LabeledBFSPerNonLM. It is only for the non-landmark vertices.




# The complete class that would implement the min-priority queue
class Node:
  
  def __init__(self, info, label):
    self.info = info
    self.label = label
    
# class for Priority queue 
class PriorityQueue:
  
  def __init__(self):
    self.queue = list()
    
  def insert(self, node):
    # if queue is empty
    if self.size() == 0:
      # add the new node
      self.queue.append(node)
    else:
      # traverse the queue to find the right place for new node
      for x in range(0, self.size()):
        # if the length of label of new node is greater
        if len(node.label) >= len(self.queue[x].label):
          # if we have traversed the complete queue
          if x == (self.size()-1):
            # add new node at the end
            self.queue.append(node)
          else:
            continue
        else:
          self.queue.insert(x, node)
          return True
  
  def delete(self):
    # remove the first node from the queue
    return self.queue.pop(0)
 
 #The checkInFirst function is used to check if the argument list b is subset of the argument list a. 
def checkInFirst(a, b):
     #getting count
    count_a = Counter(a)
    count_b = Counter(b)
  
    #checking if element exists in second list
    for key in count_b:
        if key not in  count_a:
            return False
        if count_b[key] > count_b[key]:
            return False
    return True

#The powerset method helps us to extract all the subsets from a list of elements.
def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]


global Ind
Ind={}

def TryInsert(s, (v,L)):  #s and v are vertices and L is the label set
	if v==s:
		return True

	#If there is a subset of L that already exists in the Ind[s] that helps it to reach v , we return False as we can't insert (v,L) because of the criteria that Ind[s] should only contain the minimal label set
	for subL in list(powerset(L)):
		if (v,subL) in Ind[s]:
			return False

	# if there is some other label for v present in Ind[s] that is a superset of the label L, we remove that superset label to maintain the criteria of minimal label set
	for (v,l) in Ind[s]:
		if checkInFirst(l, L) :
			Ind[s].remove(v,l)
	Ind[s].append(v,L)
	Ind[s]=sorted(ind[s], key=lambda x:x[0]) #Replace this with binary search
	return True

# This function is used to expand the index of s using the Ind[v] which also is a landmark vertex
def ForwardProp(s, (v,L)):
	for (w,l) in Ind[v]:
		TryInsert(s,(w,list(set(L+l))))




#'s' is a landmark vertex here
def LabeledBFSPerLM_Plus(s):

	q=PriorityQueue()
	node = Node(s, [])
	q.insert(node)
	# Initializing a min-priority queue using the created class Priority Queue

	while q!=[]:
		v, L = q.delete()
		#This provides us the vertex and the label of the set that has the least length of all the labels present in the min-priority-queue.

		if TryInsert(s, (v,L)) == False:
			continue
		#Trying to insert (v,L) into s using this procedure

		for i in Reachable_By[s] :
			if i[1] == L :
				i[0]= i[0].append(v)
			elif len(L)<= len(labels)//4 + 1:
				Reachable_By[s].append(([v],L))
				#Reachable_By[s] will store all its elements in the tuple form. 


		if Indexed[v] == True:
			ForwardProp(s, (v,L))
			continue
		#If we have already indexed the landmark vertex v, we run the ForwardProp to expand the Ind[s] using the Ind[v]

		for (w,l) in Adjacency_List_For_Representation[v]:
			node = Node(w, list(set(L+l)))
			q.insert(node)
		# For every edge starting from v as the source vertex, we push the node to the queue, we reach here iff (v,L) is inserted to s and v has not been indexed yet.

	for i in Reachable_By[s]:
		if i[1]==L:
			for j in Reachable_By[s]:
				if checkInFirst(i[0],j[0]):
					j[0]=i[0]




	Indexed[s]=True
	#We mark the vertex as indexed once it has been processed and all the reachable vertices with their corresponding labels are inserted.



# The query algorithm

def QueryLandmark(s,t,L):
	for i in Ind[s]:
		if i[0]==t:
			if checkInFirst(L,i[i]):
				return True
				#We check if the label given to check is a superset of all the labels stored in the Ind[s] with 't' as the target vertex, if it is so, then we return as True since if we can reach s to t by some subset of a label-set , we can surely reach 's' to 't' using the powerset of that sub-set of labels. 

	return False

Marked={}

def query(s,t,L):
	if s in landmark_vertices:
		return QueryLandmark(s,t,L)
		#If 's' is a landmark vertex, we directly use the QueryLandmark method to output the result of the query since we have already created indices for the landmark vertices.

	for v in Adjacency_List_For_Representation.keys():
		Marked[v]=False
	#We keep the visited record for the vertex as if it has been visited or not.

	q=[]
	q.append(s)
	while q!=[]:
		v=l.pop()
		Marked[v]=True
		if v==t:
			return True
		#The queue 'q' here contains all the nodes that are reached using 's', if the popped out node is 't' itself, then 't' is reached by 's' and that's what the first 'if' statement says.
		
		if v in landmark_vertices:
			if QueryLandmark(v,t,L)==True:
				return True
			continue
		#If v is a landmark vertex that's reachable from 's' , we see if the target vertex 't' is reachable from that landmark vertex 'v', if it is , we return True, else we return to the for loop to pop out other vertex from the queue.

		for (w,l) in Adjacency_List_For_Representation[v]:
			if Marked[w]==False:
				if checkInFirst(L,l):
					q.append(w)
		#We add all the vertices that is reachable from 'v' with the condition that the edge label between them should be the subset of the Query Label given.

	return False








