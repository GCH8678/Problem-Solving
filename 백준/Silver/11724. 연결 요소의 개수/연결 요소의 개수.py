
# 연결 요소의 갯수를 구하라
# n : 정점 갯수
# m : 간선 갯수
# m개의 줄에 간선의 양 끝점 u,v 주어짐

import sys
from collections import defaultdict,deque
n,m = map(int,sys.stdin.readline().split())

dic = defaultdict(list)
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    dic[u].append(v)
    dic[v].append(u)

cnt = 0
visit = defaultdict(int)
for i in range(1,n+1):
    if i not in visit:
        cnt+=1
        q = deque([i])

        while q:
            node = q.popleft()
            if node not in visit:
                visit[node] = 1
                q.extend(dic[node])
#print(visit)
print(cnt)


