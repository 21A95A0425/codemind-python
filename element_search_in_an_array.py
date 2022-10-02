z=int(input())
m=list(map(int,input().strip().split()))
a=int(input())
for i in range(len(m)):
    if m[i]==a:
        print("True")
        break
if m[i]!=a:
    print("False")