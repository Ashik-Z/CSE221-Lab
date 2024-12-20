file = open("D:\\CSE221 Lab\\Lab04\\input4.txt", 'r')
file1 = file.read()
# print(file1)
elem = file1.split()
# print(elem)
V = int(elem.pop(0))
E = int(elem.pop(0))
# print(V, E)
G = [(int(elem[i]), int(elem[i+1])) for i in range(0, len(elem), 2)]
# print(G)
def adjacency_list(V, E):
    adj_list = {i:[] for i in range(0, V+1)}
    for u, v in G:
        adj_list[u].append(v)
    return adj_list
adj_lst = (adjacency_list(V, E))

def dfs(G, s):
    visited = [False]*len(G)
    stack = [s]
    dfs_order = []
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            dfs_order.append(node)
            stack.extend([i for i in G[node] if not visited[i]])
    return dfs_order

print(dfs(adj_lst, 1))