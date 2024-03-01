#Day 10

"""
Question:
Write a program that counts the occurrences of an element in an array.

Example:
Array: [1, 2, 3, 2, 2, 4, 5]
Element to Count: 2
Occurrences: 3

Your Task:
Develop a program to count the occurrences of a given element in an array.
"""

arr = [1,2,3,2,2,4,5]

element = int(input("Element to count: "))

occurrences = 0
for num in arr:
    if num == element:
        occurrences += 1
        
print("Array",arr)
print("Element to count:",element)
print("Occurrences:",occurrences)
