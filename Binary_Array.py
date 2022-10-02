z=int(input())
m=list(map(int,input().strip().split()))
for i in range(len(m)):
    if m[i]==0 or m[i]==1:
        flag=True
    else:
        flag=False
        print("False")
        break
if flag==True:
    print("True")
    
