t=int(input())
for j in range(t):
    n=int(input())
    s=0
    for i in range(1,n+1):
        s=s+i
        if(s==n):
            print('1')
            break
        elif(s>n):
            print('0')
            break;
