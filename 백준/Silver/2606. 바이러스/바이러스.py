
# n : node
# e : edge

# 1번 컴퓨터를 통해 감염되는 컴퓨터의 수는?

import sys
from collections import defaultdict,deque
n = int(sys.stdin.readline())
e = int(sys.stdin.readline())

dic=defaultdict(list)

for _ in range(e):
    a,b = map(int,sys.stdin.readline().split())
    #print(a,b)
    dic[a].append(b)
    dic[b].append(a)

cnt = -1
q = deque([1])
visit = set()
while q:
    node = q.popleft()
    if node not in visit:
        cnt +=1
        visit.add(node)
        q.extend(dic[node])
        #print(node)
# 본인은 미포함 해야 하므로
print(cnt)