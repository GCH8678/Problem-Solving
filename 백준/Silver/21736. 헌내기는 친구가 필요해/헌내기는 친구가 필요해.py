import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

lst = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# 도연이가 만날수 있는 사람의 수를 출력하라

q = deque()
visit = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lst[i][j] == "I":
            q.append([i,j])

di = [0,0,-1,1]
dj = [-1,1,0,0]
cnt = 0
while q:
    i,j = q.popleft()
    if not visit[i][j] :
        visit[i][j] =True
        if lst[i][j] == "P":
            cnt +=1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<n and 0<=nj<m and lst[ni][nj] != "X":
                q.append([ni,nj])

print(cnt) if cnt>0 else print("TT")