a=input()
b=["0","1","2","3","4","5","6","7","8","9"]
c=0
for i in a:
    if i in b:
        c+=1
if c!=0:
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")