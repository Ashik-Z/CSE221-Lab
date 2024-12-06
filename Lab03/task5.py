file = open("D:\\CSE221 Lab\\Lab03\\input5.txt", 'r')
file1 = file.read()
# print(file1)
fileElem = file1.split()
# print(fileElem)
N = int(fileElem.pop(0))
# print(N)
M = [int(x) for x in fileElem]
print(M, N)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right
    
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            # arr[i], arr[j] = arr[j], arr[i]
            swap(arr, i, j)
        else:
            break
    # arr[left], arr[j] = arr[j], arr[left]
    swap(arr, left, j)
    
    return j

def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)
    return arr

sorted_result = (quick_sort(M, 0, N-1))
file2 = open("D:\\CSE221 Lab\\Lab03\\output5.txt", 'w')
file_writer = file2.write(str(sorted_result))
file2.close()

file3 = open("D:\\CSE221 Lab\\Lab03\\output5.txt", 'r')
file_reader = file3.read()
print(file_reader)