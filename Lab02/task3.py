file = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\input3.txt", "r")
file1 = file.read()
# print(file1)
fileList = file1.split("\n")
# print(fileList)
rangeLim = int(fileList.pop(0))
# print(rangeLim)
jobs = []
for i in range(rangeLim):
    jobDuration = fileList[i].split(" ")
    jobs.append((int(jobDuration[0]), int(jobDuration[1])))
# print(jobs)
jobs.sort(key = lambda x:x[1])

def doGreedy(arr):
    doable = []
    lastEndTime = 0
    for i in range(len(arr)):
        start, end = arr[i]
        if start >= lastEndTime:
            doable.append(arr[i])
            lastEndTime = end
    return doable
doables = (doGreedy(jobs))

file2 = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\output3.txt", "w")
file2.write(str(len(doables)) + "\n")
for i in range(len(doables)):
    file2.write(str(doables[i][0]) + " " + str(doables[i][1]) + "\n")
file3 = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\output3.txt", "r")
fileReader = file3.read()
print(fileReader)