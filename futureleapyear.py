year1=int(input("enter the current year:"))
year2=int(input("enter the last year:"))
print("leap years are:")
for year in range (year1,year2):
    if(year%4==0)and(year%100!=0):
        print(year)