#Day 28

"""
Write a program that checks whether two strings are equal without using any inbuilt methods.

Example:
String 1: "hello"
String 2: "hello"
Output: Equal

Your Task:
Develop a program to check whether two strings are equal without using any inbuilt methods.
"""

def are_strings_equal(str1, str2):   
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):  
        if str1[i] != str2[i]:
            return False
    return True

string1 = "hello"
string2 = "hello"
if are_strings_equal(string1, string2):
    print("Equal")
else:
    print("Not equal")
