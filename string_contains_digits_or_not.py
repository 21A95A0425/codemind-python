z=int(input())
for i in range(1,z+1):
    s=(input())
    a=True
    for k in s:
        if k.isdigit():
            a=False
    if a==True:
        print('No')
    else:
        print('Yes')