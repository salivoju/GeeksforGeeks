t= int(input())
while(t):
    n=input()
    dec=int(n,2)
    if(dec%3==0):
        print('1')
    else:
        print('0')
    t-=1
