'''
author=Alphonsa
version=1.0
Program to perform operations
'''
from datetime import datetime
current_time=datetime.now()
print(current_time.now())
format1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=current_time.strftime("%m,%d,%Y")
print(format2)
format3=current_time.strftime("%A,%B,%d,%Y")
print(format3)
format4=current_time.strftime("%A,%B,%d,%Y,%H:%S %p")
print(format4)
format5=current_time.strftime("%a-%b-d% %H:%m:%S IST 2024")
print(format5)
format6=current_time.strftime("%a-%b,%d %H:%M:%M IST %Y")
print(format6)
