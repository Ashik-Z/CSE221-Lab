file = open("D:\\CSE221 Lab\\Lab05\\input5.txt", 'r')
lines = file.read().split()
N = int(lines.pop(0))
M = int(lines.pop(0))
weighted_edges = [(int(lines[i]), int(lines[i+1]), int(lines[i+2])) for i in range(0, len(lines), 3)]

def initialize(N):
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    return parent, rank

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        if parent[root_x] < parent[root_y]:
            parent[root_x] = root_y
        elif parent[root_x] > parent[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        
    
def kruskal(N, edges):
    edges.sort(key=lambda x: x[2])
    parent, rank = initialize(N)
    mst_cost = 0
    mst_edge = 0
    
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += w
            mst_edge += 1
            
            if mst_edge == N-1:
                break
    if mst_edge != N-1:
        return "impossible"
    return mst_cost

result = kruskal(N, weighted_edges)
file2 = open("D:\\CSE221 Lab\\Lab05\\output5.txt", 'w')
file2.write(str(result))
reader = open("D:\\CSE221 Lab\\Lab05\\output5.txt", 'r')
print(reader.read())