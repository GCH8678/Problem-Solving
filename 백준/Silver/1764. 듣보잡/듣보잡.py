import sys

# 듣못 사람 수 N
# 보못 사람 수 M


n,m = map(int,sys.stdin.readline().split())

nlist=set()
mlist=set()

for _ in range(n):
    nlist.add(sys.stdin.readline().rstrip())
for _ in range(m):
    mlist.add(sys.stdin.readline().rstrip())
    

result =[]

for i in nlist:
    if i in mlist:
        result.append(i)

print(len(result))
result.sort()
for i in result:
    print(i)