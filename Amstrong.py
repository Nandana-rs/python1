num=int(input("enter the number:"))
temp=num
rem=0
x=0
new=0
while(num!=0):
    rem=num%10
    rem=rem*rem*rem
    new=new+rem
    num//=10
if(temp==new):
    print(new,"is Amstrong")
else:
    print("not Amstrong")