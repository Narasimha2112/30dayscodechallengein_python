#Day 26

"""
Question:
Write a program that prints the last index of a given character in a given string.

Example:
String: ""hello world""
Character: 'o'
Last Index: 7

Your Task:
Develop a program to print the last index of a given character in a given string.
"""

str1 = input()

character = input()

lastindex = -1

for i in range(len(str1)):
    if str1[i]==character:
        lastindex=i


print("String:",str1)
print("Character:",character)
print("LastIndex:",lastindex)
