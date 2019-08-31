t=int(input())
for k in range(t):
    n=int(input())
    print('1',end=" ")
    for i in range(1,n+1):
        for j in range(2,i+1):
                if(i%j)==0:
                    print(j,end=" ")
                    break;
    print()
