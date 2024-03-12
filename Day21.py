#Day 21

"""
Question:
Write a program that prints the number of vowels in a given string.

Example:
String: "Hello World"
Number of Vowels: 3

Your Task:
Develop a program in your preferred programming language to count the number of vowels in a given string.
"""

str1 = input()

vowels = "AEIOUaeiou"

count = 0

for i in str1:
    if i.lower() in vowels:
        count += 1

print("String:",str1)
print("Number of Vowels:",count)
