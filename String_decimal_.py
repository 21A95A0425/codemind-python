for c in range(int(input())):
    a=input()
    b=['0','1','2','3','4','5','6','7','8','9']
    cnt=0
    for i in a:
        if i not in b:
            cnt=1
    if cnt==1:print('False')
    else:print(True)