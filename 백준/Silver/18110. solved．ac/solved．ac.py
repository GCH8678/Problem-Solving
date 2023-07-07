# 파이썬 round 방식으로 풀면 안풀림
import sys

n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()

def round45(num):
    return int(num)+[0,1][num-int(num)>=0.5]


excep = round45(n*0.15)
s = sum(lst[excep:n-excep])
m = n-excep*2



if n==0:
    print(0)
else:
    print(round45(s/m))