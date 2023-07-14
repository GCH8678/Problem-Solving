import sys
from collections import deque
m,n = map(int,sys.stdin.readline().split())

lst = []


# -1 토마토 없음
# 0 덜익은 토마토
# 1 다익은 토마토 => 주변으로 물들어감
# 2<= m,n <= 1,000

for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

visit = [[0]*m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            q.append([i,j])
            visit[i][j]=1
        elif lst[i][j] == -1:
            visit[i][j] = -1

#print(q)

di =[0,0,-1,1]
dj =[1,-1,0,0]
while q:
    i,j = q.popleft()
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni<n and 0<=nj<m: 
            if lst[ni][nj] == 0 and visit[ni][nj] == 0 and visit[ni][nj] != -1:
                visit[ni][nj] = visit[i][j]+1
                q.append([ni,nj])
#print(visit)

result = 0
for i in visit:
    if 0 in i:
        result = 0
        break
    result = max(result,max(i))

print(result-1)