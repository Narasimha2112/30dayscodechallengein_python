#Day 22

"""
Question:
Write a program that removes all the special characters from a given string.

Example:
String: "Hello! @World#"
Output: "HelloWorld"

Your Task:
Develop a program in your preferred programming language to remove all the special characters from a given string.
"""

str1 = input()
str_output = ''

for i in str1:
    if i.isalnum():
        str_output += i

print(str_output)
        

