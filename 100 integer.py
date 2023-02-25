list=[]
n= int(input("enter the limit:"))
for i in range(0,n):
    element=int(input("enter the element:"))
    list.append(element)
print(list)

result=[]
for i in list:
    if i>100:
        result.append('over')
    else:
        result.append(i)
print(result)
