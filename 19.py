#check number is armstrong number


n=int(input("Enter Number"))

temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

print(digit)
print(temp)
if(n==sum):
    print("Armstrong Number")
else:
    print("Not a armstrong number")








