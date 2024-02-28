#Day 8

"""
Question:
Write a program that calculates the sum of all elements present in an array.

Example:
Array: [1, 2, 3, 4, 5]
Sum: 15

Your Task:
Develop a program to compute the sum of all elements present in an array,
"""

arr = [1,2,3,4,5]

sum = 0

for i in arr:
    sum = sum+i
print("Total sum:",sum)
