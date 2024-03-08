#Day 16

"""
Question:
Write a program that prints all the subarrays of an array.

Example:
Array: [1, 2, 3]
Subarrays:
[1]
[1, 2]
[1, 2, 3]
[2]
[2, 3]
[3]

Your Task:
Develop a program to print all the subarrays of a given array.
"""

arr = [1,2,3]

print("Array:",arr)
print("Subarrays")

for i in range(len(arr)):
    for j in range(i,len(arr)):
        subarray = arr[i:j+1]
        print(subarray)
