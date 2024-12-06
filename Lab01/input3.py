file = open("CSE221 LAB/Lab01/input3Text.txt", "r")
file1 = file.read()
# print(file1)

fileList = file1.split("\n")
# print(fileList)
testCase = int(fileList.pop(0))
# print(testCase, fileList)

listOfId = [int(x) for x in fileList[0].split()]
listOfMarks = [int(x) for x in fileList[1].split()]
# print(listOfId, listOfMarks)

listOfTuple = []
for i in range(testCase):
    # listOfTuple.append((f"ID: {listOfId[i]} Mark: {listOfMarks[i]}"))
    listOfTuple.append((listOfId[i], listOfMarks[i]))
# print(listOfTuple)

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j][1] < key[1]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
insertion(listOfTuple)
# print(listOfTuple)

file2 = open("CSE221 LAB/Lab01/output3Text.txt", "w")

for i in range(testCase):
    file2.write(f"ID: {listOfTuple[i][0]} Mark: {listOfTuple[i][1]}\n")
file2.close()

file3 = open("CSE221 LAB/Lab01/output3Text.txt", "r")
fileRead = file3.read()
print(fileRead)