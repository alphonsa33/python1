lst=[12,24,25,17,25]
lst2=[]
for number in lst:
    if number not in lst2:
        lst2.append(number)
print("The original list is",lst)
print(lst2)


