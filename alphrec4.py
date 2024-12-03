n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
def mul_numbers(n1,n2):
    if n2==1:
        return n1
    else:
       return  n1+mul_numbers(n1,n2-1)
print(mul_numbers(n1,n2))