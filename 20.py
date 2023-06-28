#print the interval an armstrong number

lowe=100
upper=500

for i  in range(lowe,upper+1):
    order=len(str(i))
    sum=0
    temp=i


    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if(i==sum):
        print(i)
