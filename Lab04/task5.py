file = open("D:\\CSE221 Lab\\Lab04\\input5.txt", 'r')
file1 = file.read()
elem = file1.split()
N = int(elem.pop(0))
M = int(elem.pop(0))
D = int(elem.pop(0))
G = [(int(elem[x]), int(elem[x+1])) for x in range(0, len(elem), 2)]

def adjacency_list(N, M):
    adj_lst = {i:[] for i in range(1, N+1)}
    for u, v in G:
        adj_lst[u].append(v)
        adj_lst[v].append(u)
    return adj_lst
represent_graph = adjacency_list(N, M)

from collections import deque
def det_shortest_path(represent_graph, d, roads):
    queue = deque([1])
    visited = {1}
    parent = {1: None}
    distance = {1:0}
    
    while queue:
        node = queue.popleft()
        
        if node == d:
            break
        
        for i in represent_graph[node]:
            if i not in visited:
                visited.add(i)
                parent[i] = node
                distance[i] = distance[node] + 1
                queue.append(i)
    path = []
    current = d
    while current:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

short_path = (det_shortest_path(represent_graph, D, G))
string = [str(i) for i in short_path]

file2 = open("D:\\CSE221 Lab\\Lab04\\output5.txt", 'w')
file2.write(" ".join(string))
file2.close()
reader = open("D:\\CSE221 Lab\\Lab04\\output5.txt", 'r')
print(reader.read())