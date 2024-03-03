#Day 12

"""
Question:
Write a program that prints all pairs from an array whose difference is equal to k.

Example:
Array: [9, 5, 6, 1, 2]
Difference: 4
Pairs: (9, 5), (5, 1), (6, 2)

Your Task:
Develop a program in your preferred programming language to find and print all pairs from an array whose difference is equal to k
"""

array1 = input("Enter a list of elements separated by spaces: ")

arr = list(map(int,array1.split()))

Diff = int(input("Enter the difference value: "))

pairs = []

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]-arr[j]==Diff:
            pairs.append((arr[i],arr[j]))

print("Array:",arr)
print("Difference:",Diff)
print("Pairs:",pairs)
