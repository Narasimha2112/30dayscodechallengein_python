#Day 18

"""
Question:
Write a program that prints the largest subarray whose sum is equal to k.

Example:
Array: [1, 2, 3, 4, 5]
Target Sum: 9
Largest Subarray with Sum 9: [2, 3, 4]

Your Task:
Develop a program in your preferred programming language to print the largest subarray whose sum is equal to k
"""

array = [1, 2, 3, 4, 5]
target_sum = 9

start, end = -1, -1
max_length = 0
current_sum = 0
sum_dict = {0: -1}

for i, num in enumerate(array):
    current_sum += num

    if current_sum - target_sum in sum_dict and i - sum_dict[current_sum - target_sum] > max_length:
        start = sum_dict[current_sum - target_sum] + 1
        end = i
        max_length = i - sum_dict[current_sum - target_sum]

    if current_sum not in sum_dict:
        sum_dict[current_sum] = i

result = array[start:end + 1]

print("Array:", array)
print("Target Sum:", target_sum)
print("Largest Subarray with Sum", target_sum, ":", result)

