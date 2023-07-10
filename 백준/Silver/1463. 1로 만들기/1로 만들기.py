
#X가 3으로 나누어 떨어지면, 3으로 나눈다.
#X가 2로 나누어 떨어지면, 2로 나눈다.
#1을 뺀다.

# x%3 == 0 : //3
# x%2 == 0 : //2
# 그 외 1을 뺀다

# 2->1 ( -1 or %2)
# 10 (%2)

import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(10**6+2)]
#dp[n] = min(dp[n//3],dp[n//2],dp[n-1])
dp[1],dp[2],dp[3] = 0,1,1

for i in range(3,n+1):
    if i%3==0 and i%2==0:
        dp[i] = min(dp[i//3]+1,dp[i//2]+1,dp[i-1]+1)
    elif i%3 ==0 :
        dp[i] = min(dp[i//3]+1,dp[i-1]+1)
    elif i%2 ==0:
        dp[i] = min(dp[i//2]+1,dp[i-1]+1)
    else:
        dp[i] = dp[i-1]+1
print(dp[n])