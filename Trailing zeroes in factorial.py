t=int(input())
for i in range(t):
    n=int(input())
    s=0
    while(n>0):
        s=s+n//5;
        n=n//5
    print(s)
