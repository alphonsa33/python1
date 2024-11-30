n=input("Enter the phone number:")
def phone_number():
    if len(n)==10 and n[0] in "789":
        print("THe given number is a valid mobile number")
    else:
        print("The given number is not valid")
phone_number()