file = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\input1.txt", "r")
file1 = file.read()
# print(file1)
fileList = file1.split("\n")
print(fileList)
limRange, target = (fileList.pop(0)).split()
limRange, target = int(limRange), int(target)
# print(limRange, target)
fileElem = [int(x) for x in fileList.pop(0).split()]
# print(fileElem)
def findPair1(arr, tar):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == tar:
                return i+1, j+1
    return "IMPOSSIBLE"
result1 = findPair1(fileElem, target)

def findPair2(arr, tar):
    dc = {}
    for i in range(len(arr)):
        diff = tar-arr[i]
        if diff in dc:
            return dc[diff]+1, i+1
        dc[arr[i]] = i
    return "IMPOSSIBLE"
result2 = findPair2(fileElem, target)

print(result2)
file2 = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\output1.txt", "w")
for i in range(len(result1)):
    file2.write(f"{result1[i]} ")
file3 = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\output1.txt", "r")
fileRead = file3.read()
print(fileRead)