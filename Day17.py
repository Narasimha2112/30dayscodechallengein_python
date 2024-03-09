#Day 17

"""
Question:
Write a program that prints the sum of all subarrays whose sum is equal to k.

Example:
Array: [5, 2, 3, 4, 1]
Target Sum: 10
Subarrays with Sum 8:
[5, 2, 3]
[2, 3, 4, 1]

Your Task:
Develop a program to print the sum of all subarrays whose sum is equal to k.
"""


arr1 = [5, 2, 3, 4, 1]

print("array",arr1)
result = []
target = int(input("Enter the target sum: "))



for i in range(len(arr1)):
    for j in range(i, len(arr1)):
        if target == sum_subarray(arr1[i:j+1]):
            result.append(arr1[i:j+1])


print("Subarrays with sum ",target,":",result)

