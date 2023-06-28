#Python Program to Find Numbers Divisible by Another Number


number=[12, 65, 54, 39, 102, 339, 221]

ans=list(filter(lambda x:(x%13)==0,number))    #filter function used to filter out the element
print(ans)

