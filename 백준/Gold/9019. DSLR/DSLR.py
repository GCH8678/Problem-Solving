# DSLR

# D : n을 두배로 9999보다 큰경우 %10000 (2n mod 10000)
# S : n-1 (n이 0이라면 9999)
# L : rotate 왼
# R : rotate 오

# 입력
# T : 테스트케이스 갯수
# A->B 로 변하기 위한 최소한의 명령어 나열
import sys
from collections import deque

t = int(sys.stdin.readline())

fn =["D","S","L","R"]
for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    q = deque([[a,""]])
    visit = [False]*10000
    while q:
        n,wd = q.popleft()
        if n == b:
            print(wd)
            break
        rstd = (n*2)%10000
        rsts = n-1
        if rsts<0:
            rsts =9999
        rstl = (n% 1000)*10+(n//1000)
        rstr = (n%10)*1000+(n//10)

        if not visit[n]:
            visit[n] = True
            q.append([rstd,wd+fn[0]])
            q.append([rsts,wd+fn[1]])
            q.append([rstl,wd+fn[2]])
            q.append([rstr,wd+fn[3]])


# def d(n):
#     return (n*2) % 10000
# def s(n):
#     if n==0:
#         return 9999
#     else:
#         return n-1
# def l(n):
#     front = n%1000
#     back = n//1000
#     return front*10+back
# def r(n):
#     back = n//10
#     front = n%10
#     return front*1000+back

# fn =[[d,"D"],[s,"S"],[l,"L"],[r,"R"]]
# for _ in range(t):
#     a,b = map(int,sys.stdin.readline().split())
#     q = deque([[a,""]])
#     visit = dict()
#     while q:
#         n,wd = q.popleft()
#         if n == b:
#             print(wd)
#             break
#         if n not in visit:
#             visit[n] = 1
#             for i in range(4):
#                 rst = fn[i][0](n)
#                 if rst not in visit:
#                     q.append([rst,wd+fn[i][1]])
        
        #print(q)