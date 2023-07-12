import sys

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    start,end = map(int,sys.stdin.readline().split())
    lst.append([start,end])

lst.sort(key=lambda x: x[0])
lst.sort(key= lambda x: x[1])
max = lst[-1][1]

cnt = 0
time = -1
for m in lst:
    if m[0]>=time:
        time = m[1]
        cnt+=1
print(cnt)
