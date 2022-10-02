z=int(input())
m=str(z)
a=len(m)
c=0
f=True
if a==10:
    for i in m:
        if c==0:
            if "0" in i:
                print("Invalid")
                f=False
                break
        c+=1
    if f==True:
        print("Valid")
else:
    print("Invalid")