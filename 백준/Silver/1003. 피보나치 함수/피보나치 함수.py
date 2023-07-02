import sys

t = int(sys.stdin.readline())

dp = [0 for _ in range(42)]
def fib(n,dp):
    if (n<=1):
        return n
    else:
        if dp[n]>0:
            return dp[n]
        dp[n] = fib(n-1,dp)+fib(n-2,dp)
        return dp[n]
fib(40,dp)
dp[1] = 1
dp[-1] = 1
for _ in range(t):
    n= int(sys.stdin.readline())
    print(dp[n-1],dp[n])


