#Day 11

"""
Question:
Write a program that prints all the pairs in an array.

Example:
Array: [1, 2, 3, 4, 5]
Pairs: (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)

Your Task:
Develop a program to print all the pairs present in an array.
"""

arr = [1,2,3,4,5]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        print((arr[i],arr[j]),end=" ")
