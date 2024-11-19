list1=[]
list2=[]
list_size= int(input("enter the size of list:"))
print("enter the elements of list:")
for i in range(list_size):
    list1.append(int(input()))
list2_size=int(input("Enter the size of list 2:"))
print("enter the elements of list list 2:")
for i in range(list2_size):
    list2.append(int(input()))
print(list1,list2)
list3=list1+list2
print(list3)
even_list=[]
odd_list=[]
for i in list3:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
new_list=even_list+odd_list
print(new_list)
