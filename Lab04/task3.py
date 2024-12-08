file = open("D:\\CSE221 Lab\\Lab04\\input3.txt", 'r')
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
        adj_list[u].append((v))
    return adj_list
adj_lst = (adjacency_list(V, E))

def dfs(G, source):
    visited = [False]*len(G)
    stack = [source]
    dfs_order = []
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            dfs_order.append(node)
            for u in G[node]:
                if not visited[u]:
                    stack.append(u)
    
    return dfs_order

result = (dfs(adj_lst, 1))
file2 = open("D:\\CSE221 Lab\\Lab04\\output3.txt", 'w')
for i in range(len(result)):
    file2.write(str(result[i]) + " ")
file2.close()
reader = open("D:\\CSE221 Lab\\Lab04\\output3.txt", 'r')
read_file = reader.read()
print(read_file)