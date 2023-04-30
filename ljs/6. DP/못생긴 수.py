n=int(input())
ugly=[0]*n

#2,3,5의 지수들을 index로 표현
i2,i3,i5=0,0,0

#가장 처음 못생긴 수는 1
ugly[0]=1

#2,3,5의 가장 작은 합성수
next2,next3,next5=2,3,5 

for i in range(1,n):
    ugly[i]=min(next2,next3,next5)
    if ugly[i]==next2:
        i2+=1
        next2=ugly[i2]*2
    if ugly[i]==next3:
        i3+=1
        next3=ugly[i3]*3  
    if ugly[i]==next5:
        i5+=1
        next5=ugly[i5]*5
print(ugly[n-1])  
