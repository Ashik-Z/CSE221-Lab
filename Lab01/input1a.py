# print("Hello World!")

file = open("CSE221 Lab\Lab01\input1aText.txt", "r")
file1 = file.read()
# print(file1)

temp = file1.split("\n")
# print(temp)

rangeLim = int(temp.pop(0))
# print(rangeLim)

fileElems = [int(x) for x in temp]
print(fileElems)
print(rangeLim)

file2 = open("CSE221 Lab\Lab01\output1aText.txt", "w")

for i in range(rangeLim):
    if fileElems[i] % 2 == 0:
        file2.write(f"{fileElems[i]} is an Even number.\n")
    if fileElems[i] % 2 == 1:
        file2.write(f"{fileElems[i]} is an Odd number.\n")
file2.close()

file3 = open("CSE221 Lab\Lab01\output1aText.txt", "r")
file4 = file3.read()
print(file4)