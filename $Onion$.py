str=input("enter the string=")
print("orginal string is",str)
r=str[0]
str=str.replace(r,"$")
str=r+str[1:]
print("after replacing",str)