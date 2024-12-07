file = open("D:\\CSE221 Lab\\Lab04\\input1b.txt", "r")
file1 = file.read()
# print(file1)
Elem = file1.split()
# print(Elem)
V = int(Elem.pop(0))
E = int(Elem.pop(0))
# print(V, E)
G = [(int(Elem[i]), int(Elem[i+1]), int(Elem[i+2])) for i in range(0, len(Elem), 3)]
# print(G)

def adjacency_list(V, E):
    adj_list = {i:[] for i in range(0, V+1)}
    for u, v, w in G:
        adj_list[u].append((v, w))
    return adj_list

result = (adjacency_list(V, E))
file2 = open("D:\\CSE221 Lab\\Lab04\\output1b.txt", 'w')
for i in range(0, V+1):
    file2.write(str(i) + " : " + str(result[i]) + '\n')
file2.close()
file_read = open("D:\\CSE221 Lab\\Lab04\\output1b.txt", 'r')
reader = file_read.read()
print(reader)