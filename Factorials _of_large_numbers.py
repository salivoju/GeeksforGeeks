t=int(input())
while(t):
    fact=1
    n=int(input())
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    t-=1
