n=int(input())
k=True
q=True
while n!=0:
    r=n%10
    if r%2==0:
        k=False
    else:
        q=False
    n=n//10
if k==False and q==True:
    print("Even")
elif k==True and q==False:
    print("Odd")
else:
    print("Mixed")