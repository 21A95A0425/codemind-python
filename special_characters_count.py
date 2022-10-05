z=list(input().split())
c=0
for i in range(len(z)):
    for j in z[i]:
        if j.isalpha():
            continue
        else:
            c+=1
print(c)