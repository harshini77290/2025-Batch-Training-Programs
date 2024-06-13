'''
Graph: Non-linear datastructure,connects real life entities
->used to represent relations between pairs of objects
->nodes-vertices,links-edges
TYPES:
    1. Undirected Graph
    2. Directed Graph
    3. Weighted Graph
    4. Unweighted Graph
    5. Simple Graph
    6. Non-simple Graph(self loop)
    7. Cyclic Graph
    8. Acyclic Graph

Graphs ->Adjacency Matrix
       ->Adjacency List

Traversals:
    BFS(Breadth first search)
    DFS(Depth first search)
'''

n=int(input("Enter no. of test cases:"))
x=int(input("Enter no. of boxes:"))
for i in range(1,x+1):
    a=list(map(int,input().split()))
    #print(a)
