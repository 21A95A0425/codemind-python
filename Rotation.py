for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    if b>a:b=b%a
    g=c[:-b]
    h=c[-b:]
    print(*h+g)