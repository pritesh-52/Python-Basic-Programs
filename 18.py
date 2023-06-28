#fibonaci series

#0,1,1,2,3

n=int(input("Enter Number"))
n1=0
n2=1
count=0
if n<=0:
    print("Enter postive ")
elif n==1:
    print("Fibonacri serses")
    print(n1)
else:
    print("Fibonaci series")
    while count<n:
        print(n1)
        num=n1+n2
        n1=n2
        n2=num
        count+=1