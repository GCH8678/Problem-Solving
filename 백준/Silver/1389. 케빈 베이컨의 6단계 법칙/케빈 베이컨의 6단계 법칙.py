import sys
from collections import deque,defaultdict

answer = 0

n,m = map(int,sys.stdin.readline().split())

dic = defaultdict(list)
# 여러 줄 받기
for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        if a!=b:
            dic[a].append(b)
            dic[b].append(a)
#print(dic)

lst = []

for i in range(1,n+1):
    q=deque([i])
    check = [0 for _ in range(n+1)]
    check[i] = 0
    while q:
        v = q.popleft()
        for j in dic[v]:
            if check[j] == 0 and j != i:
                q.append(j)
                check[j] = check[v]+1
    lst.append(check)
least = 100*100
for i in range(n):
    if sum(lst[i])<least:
        least = sum(lst[i])
        answer = i+1
#print(lst)

print(answer)
