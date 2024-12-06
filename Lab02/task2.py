file = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\input2.txt", "r")
file1 = file.read()
# print(file1)
fileList = file1.split("\n")
# print(fileList)
rangeLim = int(fileList.pop(0))+int(fileList.pop(1))
# print(fileList)
unsorted1, unsorted2 = [int(x) for x in fileList[0].split()], [int(x) for x in fileList[1].split()]
# print(unsorted1, unsorted2)
sortedArr = []
i, j = 0, 0
while i < len(unsorted1) and j < len(unsorted2):
    if unsorted1[i] < unsorted2[j]:
        sortedArr.append(unsorted1[i])
        i += 1
    else:
        sortedArr.append(unsorted2[j])
        j += 1
while i < len(unsorted1):
    sortedArr.append(unsorted1[i])
    i += 1
while j < len(unsorted2):
    sortedArr.append(unsorted2[j])
    j += 1
print(sortedArr)
# print(rangeLim)
elems = [int(x) for x in fileList.pop(0).split()] + [int(x) for x in fileList.pop(0).split()]
# print(elems)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        sortedList = [0]*len(arr)
        i, j, k = 0, 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sortedList[k] = left[i]
                i += 1
            else:
                sortedList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            sortedList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            sortedList[k] = right[j]
            j += 1
            k += 1
        return sortedList
resultSorted = mergeSort(elems)

file2 = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\output2.txt", "w")
for i in range(rangeLim):
    file2.write(str(resultSorted[i]) + " ")
file3 = open("C:\\Users\\zaman\\OneDrive\\Desktop\\CSE221 Lab\\Lab02\\output2.txt", "r")
fileRead = file3.read()
print(fileRead)