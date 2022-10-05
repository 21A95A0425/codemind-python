z=list(input().split())
owl=["a","e","i","o","u","A","E","I","O","U"]
c=0
for i in z:
    if i[0] in owl and i[-1] not in owl:
        c+=1
print(c)