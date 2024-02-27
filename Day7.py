#Day 7

"""
Question:
Write a program that takes an integer n as input and checks if it is a palindrome number.

Example:
Input: 12321
Output: Palindrome

Your Task:
Develop a program determine whether a given number is a palindrome or not.
"""

#Takes input from user
n = int(input("Enter a integer: "))

#convert integer value to string datatype
num = str(n)

#Palindrome condtion using if statement

if (num==num[::-1]):
    print("Palindrome.")
else:
    print("Not a Palindrome")
