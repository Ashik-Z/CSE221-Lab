file = open("D:\\CSE221 Lab\\Lab03\\input6.txt", "r")
file1 = file.read()
# print(file1.split())
fileElem = file1.split()
# print(fileElem)
N = int(fileElem.pop(0))
# print(N, fileElem)
M = [int(x) for x in fileElem[:N]]
# print(M, fileElem[N:])
fileElem2 = [int(x) for x in fileElem[N:]]
# print(fileElem2)
N2 = fileElem2.pop(0)
M2 = fileElem2
# print(N2, M2)

def partitioning(arr, left, right):
    pivot = arr[left]
    i, j = left, right
    
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_select(arr, left, right, k):
    pivot_index = partitioning(arr, left, right)
    
    if pivot_index == k:
        return arr[pivot_index]
    elif pivot_index < k:
        return quick_select(arr, pivot_index+1, right, k)
    else:
        return quick_select(arr, left, pivot_index-1, k)
    
result = []
for i in range(N2):
    result.append(quick_select(M, 0, N-1, M2[i]-1))
# print(result)

file2 = open("D:\\CSE221 Lab\\Lab03\\output6.txt", "w")
file2.write("\n".join(str(x) for x in result))
file2.close()
file_reader = open("D:\\CSE221 Lab\\Lab03\\output6.txt", "r")
read_file = file_reader.read()
print(read_file)