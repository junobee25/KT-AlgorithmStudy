n =int(input())
t = []
p =[]
dp = [0]*(n+1)
max_val = 0

for i in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

for j in range(n-1,-1,-1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i]+dp[time], max_val)
        max_val = dp[i]

    else :
        dp[i] =max_val

print(max_val)