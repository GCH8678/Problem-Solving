# N: 사람 수
# 1<=N<=1000
# P[] : 각 사람이 돈을 인출하는데 걸리는 시간 P_i

# print : 각 사람이 돈을 인출하는데 필요한 시간의 합의 최소값

import sys
n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))

p.sort()
lst = []
result = 0
for i in p:
    result +=i
    lst.append(result)

print(sum(lst))