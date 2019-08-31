#code
ugly=[0]*10001
# def uglyNumber(N):
    # ugly=[0]*N
ugly[0]=1
    # ugly.append(1)
i2,i3,i5=[0]*3
next_2=2
next_3=3
next_5=5
    # ugly[i]=1
for i in range(1,10001):
    ugly[i]=min(next_2,next_3,next_5)
    
    # ugly.append(ugly[i])
    if ugly[i]==next_2:
        i2+=1
        next_2=ugly[i2]*2
    if ugly[i]==next_3:
        i3+=1
        next_3=ugly[i3]*3
    if ugly[i]==next_5:
        i5+=1
        next_5=ugly[i5]*5

        


for t in range(int(input())):
    x=int(input())
    print(ugly[x-1])
