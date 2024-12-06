file = open("CSE221 LAB\Lab01\input1b.txt", "r")
file1 = file.read()
# print(file1)

temp = file1.split("\n")

rangeLim = int(temp.pop(0))
# print(temp, rangeLim)
file2 = open("CSE221 LAB\Lab01\output1b.txt", "w")

for i in range(rangeLim):
    sign = temp[i].split(" ")
    # print(sign)
    if sign[2] == "+":
        file2.write(f'The result of {sign[1]} + {sign[3]} is {int(sign[1])+int(sign[3])}\n')
    if sign[2] == "-":
        file2.write(f'The result of {sign[1]} - {sign[3]} is {int(sign[1])-int(sign[3])}\n')
    if sign[2] == "*":
        file2.write(f'The result of {sign[1]} * {sign[3]} is {int(sign[1])*int(sign[3])}\n')
    if sign[2] == "/":
        file2.write(f'The result of {sign[1]} / {sign[3]} is {int(sign[1])/int(sign[3])}\n')
file2.close()

file3 = open("CSE221 LAB\Lab01\output1b.txt", "r")
file3.read()
print(file3)