file = open("D:\\CSE221 Lab\\Lab04\\input1a.txt", 'r')
file1 = file.read()
# print(file1)
Elem = file1.split()
# print(Elem)
V = int(Elem.pop(0))
E = int(Elem.pop(0))
# print(V, E)
G = [(int(Elem[i]), int(Elem[i+1]), int(Elem[i+2])) for i in range(0, len(Elem), 3)]
# print(G)
def adjacency_matrix(V, E):
    adj_matrix = [[0 for i in range(V+1)] for j in range(V+1)]
    # print(adj_matrix)
    for i in range(E):
        u, v, w = G[i]
        adj_matrix[u][v] = w
    return (adj_matrix)   

result = (adjacency_matrix(V, E))
fileWrite = open("D:\\CSE221 Lab\\Lab04\\output1a.txt", 'w')

for i in range(V+1):
    for j in range(V+1):
        fileWrite.write(str(result[i][j]) + " ")
    fileWrite.write("\n")

reader = open("D:\\CSE221 Lab\\Lab04\\output1a.txt", 'r')
read_file = reader.read()
print(read_file)