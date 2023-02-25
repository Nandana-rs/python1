list=[]
n=int(input("enter the size of the list"))
for i in range(0,n):
    e=int(input("enter the element of list:"))
    list.append(e)
print("positive numbers in",list,"are:")
for i in list:
    if i>=0:
     print(i)
