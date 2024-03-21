#Day 30

"""
Question:
Write a program that prints the occurrence of each character in a given string.

Example:
Input: "mississippi"
Output: m - 1, i - 4, s - 4, p - 2

Your Task:
Develop a program to print the occurrence of each character in a given string.
"""

def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        print(f"{char} - {count}")

input_string = "mississippi"
count_characters(input_string)
