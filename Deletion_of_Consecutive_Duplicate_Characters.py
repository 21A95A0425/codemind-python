for _ in range(int(input())):
    a=input()
    b=len(a)
    s=0
    for i in range(0,b-1):
        if a[i]==a[i+1]:
            s+=1
    print(s)