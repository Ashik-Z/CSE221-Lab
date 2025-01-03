file = open("D:\\CSE221 Lab\\Lab04\\input6.txt", 'r')
reader = file.read().split()

N = int(reader.pop(0))
M = int(reader.pop(0))

visited = [[False for _ in range(M)] for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    visited[x][y] = True
    diamond_count = 1 if reader[x][y] == "D" else 0
    
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and reader[nx][ny] != "#":
            diamond_count += dfs(nx, ny)
    return diamond_count

max_diamond = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and reader[i][j] != "#":
            max_diamond = max(max_diamond, dfs(i, j))
result = (max_diamond)

file1 = open("D:\\CSE221 Lab\\Lab04\\output6.txt", "w")
writer = file1.write(str(result))
file1.close()

file_reader = open("D:\\CSE221 Lab\\Lab04\\output6.txt", "r")
print(file_reader.read())