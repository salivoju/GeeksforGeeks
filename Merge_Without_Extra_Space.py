#code
t=int(input())
for i in range(t):
    m,n=map(int,input().split());
    arr1=list(map(int,input().rstrip().split()))
    arr2=list(map(int,input().rstrip().split()))
    arr1.extend(arr2)
    arr1.sort()
    str1 = ' '.join(str(e) for e in arr1)
    print(str1)
