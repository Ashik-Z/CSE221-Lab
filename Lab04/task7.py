file = open("D:\\CSE221 Lab\\Lab04\\input7.txt", 'r')
reader = file.read().split()

N = int(reader.pop(0))
edges = [(int(reader[i]), int(reader[i+1])) for i in range(0, len(reader), 2)]

def adjacency_list(arr):
    adj_lst = {i:[] for i in range(1, N+1)}
    for u, v in arr:
        adj_lst[u].append(v)
        adj_lst[v].append(u)
    return adj_lst

def find_furthest_node(N, graph, start):
    visited = [False]*(N+1)
    dist = [0]*(N+1)
    queue = [start]
    visited[start] = True
    
    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[current]+1
                queue.append(neighbor)
    farthest_node = dist.index(max(dist))
    return farthest_node, max(dist)

def find_longest_path(N, graph):
    start = 1
    
    node_a, _ = find_furthest_node(N, graph, start)
    node_b, _ = find_furthest_node(N, graph, node_a)
    
    return node_a, node_b


graph = adjacency_list(edges)
dest_a, dest_b = find_longest_path(N, graph)
result = (dest_a, dest_b)

file1 = open("D:\\CSE221 Lab\\Lab04\\output7.txt", 'w')
for i in range(len(result)):
    file1.write(str(result[i]) + " ")
file1.close()

