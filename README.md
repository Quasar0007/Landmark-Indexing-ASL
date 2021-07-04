# Landmark-Indexing-ASL
This repository contains the entire code for Landmark Indexing currently and soon will have the clean code for the ASL algorithm.

How to run this code?
Download the code and run it on any text editor(lets say Sublime Text) following the steps below:-
- Open the command terminal and get relocated to the directory containing the file 'LI_Plus.py'
- On the command terminal, run the command 'python Li_plus.py'.
- Input on the first line should be the number of vertices(n), number of edges(m) and the number of labels(l) separated with spaces.
- The next n lines would contain the index of vertices namely 1,2,3.....
- The next m lines would contain the edges with each line having the index of source vertex, index of target vertex and the set of labels associated with the edge.
- The next l lines would contain all the label names , one in each line.

Example : - For a graph with 2 vertices namely 1 and 2 with a directed edge from 2 to 1 having the label ["follow", "friend"] from a set of labels ["follow", "friend", "connection"] will be provided as input in the following way:-

2 1 3
1
2
2 1 follow friend
follow
friend
connection




