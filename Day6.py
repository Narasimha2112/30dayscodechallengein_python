#Day 6

"""
Question:
Write a program to find the Highest Common Factor (HCF) of two numbers.

Example:
Numbers: 24, 36
HCF: 12

Your Task:
Develop a program to calculate the Highest Common Factor (HCF) of two given numbers,
"""

m = eval(input("Enter your 1st number: "))
n = eval(input("Enter your 2nd number: "))

hcf = 1

for i in range(1,min(m,n)+1):
    if (m%i)==0 and (n%i)==0:
        hcf = i
        
print("The highest common factor of two numbers is ",hcf)
