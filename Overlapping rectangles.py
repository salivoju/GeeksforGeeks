t=int(input())
for i in range(t):
    n=list(map(int,input().rstrip().split()))
    m=list(map(int,input().rstrip().split()))
    if((n[0] > m[2])or(n[2] < m[0])or(n[1] < m[3])or(n[3] > m[1])):
        print('0')
    else:
        print('1')
    
