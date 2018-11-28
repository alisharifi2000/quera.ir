n = int(input(''))

for i in range(1,n+1):
    for j in range(1,n+1):
        if j!=n:
            print(str(i*j)+' ',end='')
        else:
            print(str(i*j),end='')
    if i!=n:
       print('')
