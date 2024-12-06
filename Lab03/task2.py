file = open("D:\\CSE221 Lab\\Lab03\\input2.txt", "r")
file1 = file.read()
# print(file1)
fileElem = file1.split()
# print(fileElem)
N = int(fileElem.pop(0))
# print(N)
M = [int(x) for x in fileElem]
# print(M)

# def merge(a, b):
#     c = []
#     i, j = 0, 0
#     while i < len(a) and j < len(b):

def findMax(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left = findMax(arr[mid:])
        right = findMax(arr[:mid])
        
        # if right < left:
        #     return left
        # else:
        #     return right
        return left if left > right else right

maxElem = (findMax(M))
filewrite = open("D:\\CSE221 Lab\\Lab03\\output2.txt", "w")
filewrite.write(str(maxElem))
filewrite.close()

fileReader = open("D:\\CSE221 Lab\\Lab03\\output2.txt", "r")
fileReader1 = fileReader.read()
print(fileReader1)