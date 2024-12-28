file = open("D:\\CSE221 Lab\\Lab05\\input1.txt", 'r')
file_reader = file.read()
elem = file_reader.split()
N = int(elem.pop(0))
M = int(elem.pop(0))
S = int(elem.pop(-1))
weighted_edges = [(int(elem[i]), int(elem[i+1]), int(elem[i+2])) for i in range(0, len(elem), 3)]

def adjacency_list(N, weighted_edges):
    graph = {i:[] for i in range(1, N+1)}
    for u, v, w in weighted_edges:
        graph[u].append((v, w))
    return graph
graph = adjacency_list(N, weighted_edges)

def dijkstra(graph, start, N):
    inf = float('inf')
    dist = [inf] * (N+1)
    dist[start] = 0
    processed = [False] * (N+1)
    
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
    return [dist[i] if dist[i] != inf else -1 for i in range(1, N + 1)]
result = (dijkstra(graph, S, N))

file2 = open("D:\\CSE221 Lab\\Lab05\\output1.txt", 'w')
for i in range(len(result)):
    file2.write(str(result[i]) + ' ')
file2.close()
file_reader = open("D:\\CSE221 Lab\\Lab05\\output1.txt", 'r')
read_file = file_reader.read()
print(read_file)