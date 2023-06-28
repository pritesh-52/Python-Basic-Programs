#prime number
a=int(input("Enter Number"))
flag=False

if(a==1):
    print("Not a Prime Number")

elif a>1:
    for i in range(2,a):
        if(a%i)==0:
            flag=True
            break
    if(flag):
        print("Not a prime number")
    else:
        print("Prime number")

