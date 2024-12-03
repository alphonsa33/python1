n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
print(gcd(n1,n2))