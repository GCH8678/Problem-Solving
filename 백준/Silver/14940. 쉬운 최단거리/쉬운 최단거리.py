import sys
from collections import deque
#세로 n, 가로 m -> lst[n][m]
n,m = map(int,sys.stdin.readline().split())


lst=[]
visit =  [[-1]*m for _ in range(n)]

start=(0,0)
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
    if int(2) in lst[i]:
        start=[i,lst[i].index(2)]

visit[start[0]][start[1]]=0
dn=[0,0,-1,1]
dm=[1,-1,0,0]


def dfs(start:list):
    q = deque([start])
    while q:
        node = q.popleft()
        for i in range(4):
            nn = node[0]+dn[i]
            nm = node[1]+dm[i]
            if 0<=nn <n and 0<=nm<m:
                if lst[nn][nm] == 1:
                    lst[nn][nm]=0
                    q.append((nn,nm))
                    visit[nn][nm] = visit[node[0]][node[1]]+1
    

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0 and visit[i][j]==-1:
            visit[i][j]=0
        elif lst[i][j] == 2:
            dfs([i,j])


            

for i in range(n):
    print(*visit[i])