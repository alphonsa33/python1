n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
print(add_numbers(n1,n2))