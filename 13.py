#find the largest number
a=int(input("Enter Number"))
b=int(input("Enter Number"))
c=int(input("Enter Number"))

if(a>b and a>c):
    if(b>c):
        print("First is max",a)
elif (b>c):
    print("B is max")
else:
    print("C is max")