#Day 14

"""
Question:
Write a program that prints the occurrences of all elements in a sorted array.

Example:
Array: [1, 1, 1, 2, 3, 3, 5, 5, 5, 6]
Occurrences:
1 - 3 
2 - 1 
3 - 2 
5 - 3
6 - 1

Your Task:
Develop a program in your preferred programming language to print the occurrences of all elements in an array
"""

arr = [1,1,1,2,3,3,5,5,5,6]

element = None

count = 0

for i in arr:
    if i == element:
        count += 1
    else:
        if element is not None:
            print(element,"-",count)
        element = i
        count = 1
        
print(element,"-",count)
