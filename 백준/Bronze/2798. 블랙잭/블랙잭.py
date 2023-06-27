#2795.블랙잭

# 카드의 합이 21을 이하, 카드의 합 최대값
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# N M
# N장의 카드
# 3<=N<=100 , 10<=M<=300,000
# 3장의 카드 100 C 3 = > 10^6 미만

from sys import stdin

n,target = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))

# r : 선택 갯수
lst.sort()
def combination(lst,r):
    result = []
    if r > len(lst):
        return result
    if r == 1:
        for i in lst:
            result.append([i])
    elif r>1:
        for i in range(len(lst)-r+1):
            for j in combination(lst[i+1:],r-1):
                result.append([lst[i]]+j)
    return result

distance = 300_000
for a,b,c in combination(lst,3):
    if a+b+c > target:
        continue
    distance = min(distance,target-a-b-c)

print(target-distance)

