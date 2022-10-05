z=list(input().split())
c=0
for i in z:
    if i.lower()==i.lower()[::-1]:
        c+=1
print(c)