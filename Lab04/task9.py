file = open("D:\\CSE221 Lab\\Lab04\\input9.txt", "r")
reader = file.read().split()
N = int(reader.pop(0))
M = int(reader.pop(0))
edges = [(int(reader[i]), int(reader[i+1])) for i in range(0, len(reader), 2)]

def adjacency_list(N, edges):
    adj = {i:[] for i in range(1, N+1)}
    for u, v in edges:
        adj[u].append(v)
    return adj

def topological_sort_dfs(N):
    graph = adjacency_list(N, edges)
    visited = [0]*(N+1)
    stack = []
    is_possible = True
    
    def dfs(nodes):
        nonlocal is_possible
        if visited[nodes] == 1:
            is_possible = False
            return
        if visited[nodes] == 0:
            visited[nodes] = 1
            for i in graph[nodes]:
                dfs(i)
            visited[nodes] = 2
            stack.append(nodes)
    
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            
    if not is_possible:
        return "IMPOSSIBLE"
    return stack[::-1]

result = topological_sort_dfs(N)
file2 = open("D:\\CSE221 Lab\\Lab04\\output9.txt", "w")
for i in result:
    file2.write(str(i) + " ")
file2.close()