#Day 20

"""
Question:
Write a program that checks if a given string is a palindrome or not.

Example:
String: "racecar"
Output: Palindrome

Your Task:
Develop a program in your preferred programming language to determine whether a given string is a palindrome or not.
"""

str1 = input()

if (str1==str1[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")
