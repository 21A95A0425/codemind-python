n=int(input())
for i in range(1,n+1):
    x,y=map(int,input().split())
    s=input()
    k=""
    p=s[:y]
    q=s[y:]
    q=q[::-1]
    q=q+p[0]
    for i in range(1,y):
        k=p[::-1]
        q=q+k[0]
        p=k[:y-i]
    print(q[::-1])