#Day 15

"""
Question:
Write a program that prints the unique elements in a sorted array.

Example:
Sorted Array: [1, 2, 2, 3, 4, 5, 5, 5]
Unique Elements: 1, 3, 4

Your Task:
Develop a program to print the unique elements in a sorted array.
"""

arr = [1,2,2,3,4,5,5,5]

count = 1

for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        count += 1
    elif count ==1:
        print(arr[i],end=" ")
    else:
        count=1
        
if count==1:
    print(arr[-1])
