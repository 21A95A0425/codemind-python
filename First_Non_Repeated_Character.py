for _ in range(int(input())):
    a=int(input())
    b=input()
    c=[]
    for i in b:
        if b.count(i)==1:
            c.append(i)
            break
    if len(c)>0:
        print(c[0])
    else:
        print("-1")