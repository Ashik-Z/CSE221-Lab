file = open("D:\\CSE221 Lab\\Lab03\\input4.txt")
file1 = file.read()
# print(file1)
fileElem = file1.split()
# print(fileElem)
N = int(fileElem.pop(0))
# print(N, fileElem)
M = [int(x) for x in fileElem]
# print(N, M)

import math

def divider(arr):
    if len(arr) == 1:
        return [arr[0], -math.inf]
    
    if len(arr) == 2:
        first_max = (max(arr))
        second_max = abs(min(arr))
        return first_max, second_max
    
    mid = len(arr) // 2
    left_max, left_second_max = divider(arr[:mid])
    right_max, right_second_max = divider(arr[mid:])
    
    candidates = [left_max, left_second_max, right_max, right_second_max]
    # candidates = merge(candidates)
    candidates = sorted(candidates, reverse=True)
    return candidates[0], abs(candidates[1])

processor = divider(M)
print(processor)
processsed = (processor[0]+processor[1]**2)

file2 = open("D:\\CSE221 Lab\\Lab03\\output4.txt", "w")
file2.write(str(processsed))
file2.close()

file_reader = open("D:\\CSE221 Lab\\Lab03\\output4.txt", "r")
read_file = file_reader.read()
print(read_file)