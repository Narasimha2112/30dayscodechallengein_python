#Day 13

"""
Question:
Write a program that prints the largest repeating element in a sorted array.

Example:
Input:
Array: [1, 1, 1, 2, 3, 3, 5, 5, 5]
Output:
5

Your Task:
Develop a program to print the occurrences of all elements in an array.
"""

arr = [1,1,1,2,3,3,5,5,5]

element = arr[0]

count =1

for i in range(1,len(arr)):
    if arr[i] == element:
        count += 1
    else:
        element = arr[i]
        count = 1

print(element)
