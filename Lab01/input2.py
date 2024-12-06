file = open("CSE221 LAB\Lab01\input2Text.txt", "r")
file1 = file.read()
# print(file1)

fileList = file1.split()

fileElems = [int(x) for x in fileList]
length = fileElems.pop(0)


# print(length, fileElems)

def bubble(arr):
    for i in range(length):
        flag = False
        for j in range(i+1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                flag = True
        if not flag:
            break
    return arr
bubble(fileElems)

file2 = open("CSE221 LAB\Lab01\output2Text.txt", "w")

for i in range(length):
    file2.write(str(fileElems[i]) + " ")
file2.close()

file3 = open("CSE221 LAB\Lab01\output2Text.txt", "r")
fileReader = file3.read()
print(fileReader)