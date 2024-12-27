file = open("D:\\CSE221 Lab\\Lab05\\input3.txt", 'r')
lines = file.read().split()

N = int(lines.pop(0))
M = int(lines.pop(0))
G = [(int(lines[i]), int(lines[i+1]), int(lines[i+2])) for i in range(0, len(lines), 3)]

def adjacency_list(N, G):
    graph = {i:[] for i in range(1, N+1)}
    for u, v, w in G:
        graph[u].append((v, w))
    return graph
graph = (adjacency_list(N, G))

def safest_path(graph, start, end, N):
    inf = float('inf')
    max_danger = [inf] * (N+1)
    max_danger[start] = 0
    processed = [False]*(N+1)
    pq = [(0, start)]
    
    while pq:
        pq.sort()
        danger, u = pq.pop(0)
        if processed[u]:
            continue
        processed[u] = True
        for v, w in graph[u]:
            new_danger = max(danger, w)
            if new_danger < max_danger[v]:
                max_danger[v] = new_danger
                pq.append((new_danger, v))
    return max_danger[end] if max_danger[end] != inf else "Impossible"

result = (safest_path(graph, 1, N, N))
file2 = open("D:\\CSE221 Lab\\Lab05\\output3.txt", 'w')
file2.write(str(result))
file2.close()
file_reader = open("D:\\CSE221 Lab\\Lab05\\output3.txt", 'r')
print(file_reader.read())