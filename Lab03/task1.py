file = open("D:\\CSE221 Lab\\Lab03\\input1.txt", "r")
file1 = file.read()
fileElem = file1.split()
N = int(fileElem.pop(0))
M = [int(x) for x in fileElem]

def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

sortedArr = (mergeSort(M))

fileWrite = open("D:\\CSE221 Lab\\Lab03\\output1.txt", "w")
for i in range(N):
    fileWrite.write(str(sortedArr[i]) + " ")
fileWrite.close()
fileOpen = open("D:\\CSE221 Lab\\Lab03\\output1.txt", "r")
fileReader = fileOpen.read()
print(fileReader)