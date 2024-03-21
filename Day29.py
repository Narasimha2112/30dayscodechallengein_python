#Day 29

"""
Question:
Write a program that prints a given string in reverse order, while keeping each word intact.

Example:
Input: "Welcome to TAP Academy"
Output: "emocleW ot PAT ymedacA"

Your Task:
Develop a program to print a given string in reverse order.
"""

def reverse_string(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

input_string = "Welcome to TAP Academy"
output_string = reverse_string(input_string)
print(output_string)
