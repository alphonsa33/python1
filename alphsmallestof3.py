'''
Python program to find the larger of two numbers
author-alph
'''
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num1<num2 and num2<num3:
    print("num1 is smallest")
elif num2<num1 and num2<num3:
    print("num2 is smallest")
else:
    print("num3 is smallest")
