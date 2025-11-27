dict1={ }
l=int(input("enter the limit:"))
for i in range(l):
       k=input("enter the key:")
       val=int(input("enter the value:"))
       dict1[k]=val
print(dict(sorted(dict1.items())))
print(dict(sorted(dict1.items(),reverse=True)))
