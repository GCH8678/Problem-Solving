# i~ j 까지 합
# 수의 갯수 n
# 합을 구해야하는 횟수 m
# 1<=n<=100,000
# 1<=m<=100,000
#1<=i<=j<=n

import sys

n,m = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))
sumLst = [0,lst[0]]

for i in range(1,n):
    sumLst.append(sumLst[i]+lst[i])

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    print(sumLst[j]-sumLst[i-1])

