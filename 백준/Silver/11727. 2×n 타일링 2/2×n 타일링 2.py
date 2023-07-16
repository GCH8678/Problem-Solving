import sys

dp = [1,3,5]

n = int(sys.stdin.readline())

for i in range(3,n):
    dp.append(dp[i-1] + 2*dp[i-2])

print(dp[n-1]%10007)