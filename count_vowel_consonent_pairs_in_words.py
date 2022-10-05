z=list(input().split())
owl=["a","e","i","o","u","A","E","I","O","U"]
l=[]
k=[]
for i in z:
    if len(i)%2==1:
        o=len(i)//2
        for j in range(o):
            l.extend([[i[j],i[-j-1]]])
    else:
        o=len(i)//2
        for j in range(o):
            l.extend([[i[j],i[-j-1]]])
for i in l:
    n=[i[0]in owl and i[1] not in owl,i[1] in owl and i[0] not in owl]
    if any(n):
        k.append(i)
print(len(k))