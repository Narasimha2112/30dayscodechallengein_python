#Day 27

"""
Question:
Write a program that prints all the substrings of a given string.

Example:
String: "abc"
Substrings: "a", "ab", "abc", "b", "bc", "c"

Your Task:
Develop a program to print all the substrings of a given string.
"""

str1 = input()
substrings = []

for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        substrings.append(str1[i:j])

print("String:",str1)
print("Substrings:",substrings)
