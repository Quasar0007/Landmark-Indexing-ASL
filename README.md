# Landmark-Indexing-ASL
The entire code for Landmark Indexing and ASL algorithm is present here.

How to run the code for LI_Plus algorithm? </br>
Download the code and run it on any text editor(lets say Sublime Text) following the steps below:-
- Open the command terminal and get relocated to the directory containing the file 'LI_Plus.py'
- On the command terminal, run the command 'python Li_plus.py'.
- Input on the first line should be the number of vertices(n), number of edges(m) and the number of labels(l) separated with spaces.
- The next n lines would contain the index of vertices namely 1,2,3.....
- The next m lines would contain the edges with each line having the index of source vertex, index of target vertex and the set of labels associated with the edge.
- The next l lines would contain all the label names , one in each line.

**Landmark-Indexing-Plus Example** </br>
Example : - For a graph with 2 vertices namely 1 and 2 with a directed edge from 2 to 1 having the label ["follow", "friend"] from a set of labels ["follow", "friend", "connection"] will be provided as input in the following way:-

- 2 1 3
- 1
- 2
- 2 1 follow friend
- follow
- friend
- connection

How to run the code for ASL algorithm? </br>
Download the code and run it on any text editor(lets say Sublime Text) following the steps below:-
- Open the command terminal and get relocated to the directory containing the file 'ASL.py'
- On the command terminal, run the command 'python ASL.py'.
- Input on the first line should be the number of vertices(n).
- The second line should be the number of edges(m).
- The next m lines would contain the edges with three input items in each line separated by spaces, respectively the source vertex, the target vertex and the label.
- The next line would contain the number of labels(l).
- The next l lines would contain all the label names , one in each line.
- The next line contains the number of landmark vertices.
- The third last, second last and last line takes the source vertex, target vertex and the label as input respectively.(The input label should be separated by spaces if there are more than one labels.

**ASL-Example** </br>
![image](https://user-images.githubusercontent.com/66168933/129321351-0d7e4bbb-fa50-4617-9f2e-cc01b32c2d7e.png)

Lets say we need to find the query that vertex '6' reaches to vertex '4' constrained to the labels ['a','b']. </br>
The vertices are indexed from '0' instead of 1, so vertex '3' is given as input '2'.
The input in this case would be:-

- 10 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #*Number of vertices*
- 15 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #*Number of edges and next 15 lines represent the edges.*
- 0 1 a  
- 0 2 b
- 1 2 c
- 2 3 b
- 2 9 b
- 3 0 b
- 4 2 a
- 5 4 a
- 6 8 b
- 6 5 c
- 7 4 c
- 7 9 a
- 7 6 b
- 8 5 c
- 8 7 b
- 3 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #*Number of labels and next 3 lines represent the labels.*
- a    
- b    
- c
- 2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #*Number of lnadmark vertices*
- 5 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #*Source vertex*
- 3 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #*Target vertex*
- a b &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;#*Labels.*

![Screenshot (125)](https://user-images.githubusercontent.com/66168933/129329966-a21597cf-3341-4ac2-8f09-2e49d687e0f9.png)






 


