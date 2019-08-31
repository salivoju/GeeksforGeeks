t=int(input())
for i in range(t):
    lst=[]
    n=int(input())
    for i in range(2,n):
        count=0;
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count==2):
            lst.append(i)
    found=False
    for k in range(len(lst)):
        if found:
            break;
        for g in range(k,len(lst)):
            if((lst[k]+lst[g])==n):
                print(lst[k],end=" ")
                print(lst[g]);
                found=True;
                break
