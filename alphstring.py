'''
author=Alphonsa
version=1.0
Program to perform operations
'''
first_name=input("enter the first name")
last_name=input("enter the last name")
full_name=first_name+" "+last_name
print(full_name)
length=len(first_name)
extracted_last_name=full_name[length+1:]
print(extracted_last_name)