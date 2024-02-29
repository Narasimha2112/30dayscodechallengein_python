#Day 9 

"""
Question:
Write a program that finds the largest element present in an array.

Example:
Array: [5, 10, 3, 8, 15]
Largest Element: 15

Your Task:
Develop a program to determine the largest element present in an array, 
"""

arr = [5, 10, 22, 25, 15]

largest_element = arr[0]

for i in arr:
    if i > largest_element:
        largest_element = i

print("Array:", arr)
print("Largest Element:", largest_element)
