file = open("D:\\CSE221 Lab\\Lab03\\input3.txt", "r")
file1 = file.read()
# print(file1)
fileElem = file1.split()
# print(fileElem)
N = int(fileElem.pop(0))
# print(N, fileElem)
M = [int(i) for i in fileElem]
# print(M)


def mergeAndCount(arr, mid, l, r):
    left = arr[l:mid + 1]
    right = arr[mid + 1:r + 1]
    
    i, j, k = 0, 0, l
    res = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (len(left) - i)
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return res


def countInv(arr, l, r):
    res = 0
    if l < r:
        m = (l + r) // 2

        res += countInv(arr, l, m)
        res += countInv(arr, m + 1, r)

        res += mergeAndCount(arr, m, l, r)
    return res


def inversionCount(arr):
    return countInv(arr, 0, len(arr) - 1)



result = inversionCount(M)
file2 = open("D:\\CSE221 Lab\\Lab03\\output3.txt", "w")
file2.write(str(result))
file2.close()

fileReader = open("D:\\CSE221 Lab\\Lab03\\output3.txt", "r")
fileReader1 = fileReader.read()
print(fileReader1)