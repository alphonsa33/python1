'''
Author:Alph
Date:22-08-2024
Version:1.0
Program to input three numbers and find the largest
'''
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num1>num2 and num1>num3:
    print("The largest number is:",num1)
elif num2>num1 and num2>num3:
    print("The largest number is:",num2)
else:
    print("The largest number is:",num3)