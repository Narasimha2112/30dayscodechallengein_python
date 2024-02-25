#Day 5

"""
Write a program that takes two integers, n1 and n2, as input and prints the first y common multiples of n1 and n2.

Example:
Input: n1 = 3, n2 = 5, y = 4
Output: 15, 30, 45, 60

Your Task:
Develop a program in to find and print the first y common multiples of n1 and n2.
"""
def comm_mutli():
    n1 = eval(input("Enter your first number: "))
    n2 = eval(input("Enter your second number: "))

    y = int(input("Enter the number to print how many Comm_multi of n1 & n2: "))

    for i in range(1,y+1):
        if(n1==n2):
            print(n1*i," ")
        else:
            print(n1*n2*i," ")
            
comm_mutli()
