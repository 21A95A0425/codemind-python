z=input()
v=input()
f=False
c=0
for i in z:
    if v in i:
        f=True
        print(True)
        print(c)
        break
    c+=1
if f==False:
    print(False)