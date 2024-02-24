#Day4

"""
Question:
Write a program that takes two integers, n1 and n2, as input and prints the common factors of n1 and n2.

Example:
Input: n1 = 12, n2 = 18
Output: 1, 2, 3, 6

Your Task:
Develop a program in your preferred programming language to find and print the common factors of n1 and n2,
"""

n1 = eval(input("Enter your 1st number:"))
n2 = eval(input("Enter your 2nd number:"))

def x():
    Common_factors=[]

    for i in range(1,min(n1,n2)+1):
        if (n1%i)==0 and (n2%i)==0:
            Common_factors.append(i)

    print(Common_factors)
    
x()
