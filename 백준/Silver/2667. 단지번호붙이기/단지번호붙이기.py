import sys
from collections import deque
#지도 크기 (n*n)
n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(list(sys.stdin.readline().rstrip()))



dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(lst,x,y):
    cnt = 1
    q=deque([[x,y]])
    lst[y][x] = "0"
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if lst[ny][nx] =="1":
                    cnt+=1

                    lst[ny][nx] ="0"
                    q.append([nx,ny])
    return cnt
#print(lst)
result =[]
for y in range(n):
    for x in range(n):
        if lst[y][x] == "1":
            result.append(bfs(lst,x,y))
print(len(result))
result.sort()
for i in result:
    print(i)