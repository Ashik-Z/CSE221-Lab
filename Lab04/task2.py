file = open("D:\\CSE221 Lab\\Lab04\\input2.txt", 'r')
file1 = file.read()
# print(file1)
elem = file1.split()
V = int(elem.pop(0))
E = int(elem.pop(0))
# print(V, E)
G = [(int(elem[i]), int(elem[i+1])) for i in range(0, len(elem), 2)]
# print(G)
def adjacency_list(V, E):
    adj_list = {i:[] for i in range(0, V+1)}
    for u, v in G:
        adj_list[u].append((v))
    return adj_list
adj_lst = adjacency_list(V, E)

from collections import deque
def bfs(adj_lst, source):
    visited = [False]*(len(adj_lst))
    queue = deque([source])
    visited[source] = True
    bfs_order = []
    
    while queue:
        u = queue.popleft()
        bfs_order.append(u)
        
        for v in adj_lst[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
    return bfs_order
result = (bfs(adj_lst, 1))
file2 = open("D:\\CSE221 Lab\\Lab04\\output2.txt", 'w')
for i in range(len(result)):
    file2.write(str(result[i]) + ' ')
file_read = open("D:\\CSE221 Lab\\Lab04\\output2.txt", 'r')
reader = file_read.read()
print(reader)