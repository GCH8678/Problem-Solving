import sys
from collections import deque
t = int(sys.stdin.readline())


def check(i,j,arr):
    dx =[0,0,-1,1]
    dy = [-1,1,0,0]
    q = deque([[i,j]])
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i+dy[d]
            nj = j+dx[d]
            if (ni>=0 and nj>=0 and ni< len(arr) and nj<len(arr[0])):
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    q.append([ni,nj])
    
for _ in range(t):
    # m : 가로길이, n:세로길이
    m,n,k = map(int,sys.stdin.readline().split())
    arr = [[0]*m for _ in range(n)]
    chk = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        arr[y][x] = 1
    result =0
    #2500개 배회
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                arr[i][j] = 1
                result+=1
                check(i,j,arr)
                
    print(result)

