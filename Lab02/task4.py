file = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\input4.txt", "r")
file1 = file.read()
# print(file1)
fileList = file1.split('\n')
# print(fileList)
elemLim, peep = fileList.pop(0).split()
# print(elemLim, peep)
N, M = int(elemLim), int(peep)
jobs = []
for i in range(N):
    var = fileList[i].split()
    jobs.append((int(var[0]), int(var[1])))
# print(jobs)
jobs.sort(key = lambda x:x[1])
# print(jobs)
def max_tasks_o_n2(N, M, tasks):
    tasks.sort(key = lambda x:x[1])
    people = [0] * M
    count = 0
    
    for start, end in tasks:
        for i in range(M):
            if people[i] <= start:
                people[i] = end
                count += 1
                break
    
    return count
output = max_tasks_o_n2(N, M, jobs)
# print(output)
file2 = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\output4.txt", "w")
file2.write(str(output))
file3 = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\output4.txt", "r")
print(file3.read())