file = open("D:\\CSE221 Lab\\Lab05\\input2.txt", 'r')
lines = file.read().split()

N = int(lines.pop(0))
M = int(lines.pop(0))
T = int(lines.pop(-1))
S = int(lines.pop(-1))

tuple_elem = [(int(lines[i]), int(lines[i+1]), int(lines[i+2])) for i in range(0, len(lines), 3)]
def adjacency_list(N, tuple_elem):
    graph = {i:[] for i in range(1, N+1)}
    for u, v, w in tuple_elem:
        graph[u].append((v, w))
    return graph
graph = (adjacency_list(N, tuple_elem))

def dijkstra(graph, start, N):
    inf = float('inf')
    dist = [inf]*(N+1)
    dist[start] = 0
    processed = [False]*(N+1)
    
    pq = [(0, start)]
    
    while pq:
        pq.sort()
        d, u = pq.pop(0)
        
        if processed[u]:
            continue
        processed[u] = True
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.append((dist[v], v))
    return dist
alice = dijkstra(graph, S, N)
bob = dijkstra(graph, T, N)

minimum_time = float('inf')
meet_node = -1

for i in range(1, N+1):
    if alice[i] != float('inf') and bob[i] != float('inf'):
        if alice[i] + bob[i] < minimum_time:
            max_time = max(alice[i], bob[i])
            if max_time < minimum_time:
                minimum_time = max_time
                meet_node = i

file2 = open("D:\\CSE221 Lab\\Lab05\\output2.txt", 'w')
for i in range(1, N+1):
    if meet_node == -1:
        file2.write("IMPOSSIBLE")
        break
    else:
        file2.write(f"Time:{minimum_time}\nNode:{meet_node}")
        break
    
file2.close()
file_reader = open("D:\\CSE221 Lab\\Lab05\\output2.txt", 'r')
print(file_reader.read())