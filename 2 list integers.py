list1=[]
n1=int(input("enter the limit:"))
for i in range(0,n1):
    element1=int(input("enter the element:"))
    list1.append(element1)

list2=[]
n2=int(input("enter the limit:"))
for i in range(0,n2):
    element2=int(input("enter the element:"))
    list2.append(element2)

print(list1)
print(list2)

# lists are same length
print("length of list1",list1)
print("length of list2",list2)
if len(list1)==len(list2):
    print("two lists are of same length")
else:
    print("not same length")
#sums to same value
total = sum(list1)
print ("sum of list1 is",total)
total = sum(list2)
print("sum of list2 is",total)
if sum(list1)==sum(list2):
    print("two lists are of same length")
# any value occur in both
print("value occur in both:")
for i in list1:
 if i in list2:
     print(i)