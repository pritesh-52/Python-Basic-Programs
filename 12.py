#check leap year or not
year=int(input("Enter Number"))

if(year%4==0 or year%400==0):
    print("Leap Year")
else:
    print("Not a leap year")