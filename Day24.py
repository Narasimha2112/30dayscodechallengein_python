#Day 24

"""
Question:
Write a program that converts a given string according to the following rules and prints the output:

Place '#' before vowels in the string.
Example:
Input: "Tap Academy"
Output: "T#ap #Ac#ad#emy"

Your Task:
Develop a program to convert the given string based on the provided rules and print the output.
"""

str1 = input()
vowels = 'aeiouAEIOU'
output_str1 = ''

for i in str1:
    if i in vowels:
        output_str1 += '#'+i
    else:
        output_str1 += i

print(output_str1)
