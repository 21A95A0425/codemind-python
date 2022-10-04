z=input()
v=["a",'e','i','o','u']
u=['A','E','I','O','U']
a=[]
for i in z:
    if i in v:
        v.remove(i)
    if i in u:
        u.remove(i)
if len(v)==0 or len(u)==0:
    print(True)
else:
    print(False)