z=input()
b="aeiouAEIOU"
k,s=[],0
for i in z:
    if i in b:
        s+=1
    else:
        k.append(s)
        s=0
k.append(s)
print(max(k))