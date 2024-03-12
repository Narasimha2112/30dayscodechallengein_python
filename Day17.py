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


def sum_subarray(arr):
    return sum(arr)

def main():
    arr1 = [5, 2, 3, 4, 1]
    result = []
    target = 10

    for i in range(len(arr1)):
        for j in range(i, len(arr1)):
            if target == sum_subarray(arr1[i:j+1]):
                result.append(arr1[i:j+1])

    print(result)

if __name__ == "__main__":
    main()
