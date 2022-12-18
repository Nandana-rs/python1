#To enter name,marks of 5 subjects and calculate total and percentage for each students
#Enter the mark of first student
a=input("Enter the name of the first student:")
m1=int(input("Enter the marks of first subject:"))
m2=int(input("Enter the marks of second subject:"))
m3=int(input("Enter the marks of third subject:"))
m4=int(input("Enter the marks of fourth subject:"))
m5=int(input("Enter the marks of fifth subject:"))

#Let's consider the total as S1
S1=m1+m2+m3+m4+m5
#Let's consider the percentage as P1
P1=S1/500*100

print("The total marks of the first student:",S1)
print("The percentage mark of first student:",P1)

#Enter the mark of second student
b=input("Enter the name of the second student:")
n1=int(input("Enter the marks of first subject:"))
n2=int(input("Enter the marks of second subject:"))
n3=int(input("Enter the marks of third subject:"))
n4=int(input("Enter the marks of fourth subject:"))
n5=int(input("Enter the marks of fifth subject:"))

#Let's consider the total as S2
S2=n1+n2+n3+n4+n5
#Let's consider the percentage as P2
P2=S2/500*100

print("The total marks of the second student:",S2)
print("The percentage mark of second student:",P2)

