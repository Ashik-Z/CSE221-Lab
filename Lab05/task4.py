file = open("D:\\CSE221 Lab\\Lab05\\input4.txt", 'r')
lines = file.read().split()

N = int(lines.pop(0))
K = int(lines.pop(0))
queries = [(int(lines[i]), int(lines[i+1])) for i in range(0, 2*K, 2)]

def initialize(N):
    parent = [i for i in range(N+1)]
    size = [1]*(N+1)
    return parent, size

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]

def get_circle_size(parent, size, x):
    root_x = find(parent, x)
    return size[root_x]

parent, size = initialize(N)

result = []
for A, B in queries:
    union(parent, size, A, B)
    result.append(get_circle_size(parent, size, A))

file2 = open("D:\\CSE221 Lab\\Lab05\\output4.txt", 'w')
for res in result:
    file2.write(str(res) + '\n')
file2.close()
reader = open("D:\\CSE221 Lab\\Lab05\\output4.txt", 'r')
print(reader.read())