
import sys
import collections


def dfs(start,dic):
    visit = []
    stack = [start]
    
    while stack:
        x=stack.pop()
        if x not in visit:
            visit.append(x)
            stack.extend(sorted(dic[x])[::-1])
    return visit

def bfs(start,dic):
    visit = [start]
    q = collections.deque([start])
    while q:
        x = q.popleft()
        for i in sorted(dic[x]):
            if i not in visit:
                visit.append(i)
                q.append(i)
    return visit

# n : 정점 갯수, m : 간선 갯수, v : 시작 정점 번호
n,m,v = map(int,sys.stdin.readline().split())

dic = collections.defaultdict(list)
for _ in range(m):
    v1,v2 = map(int,sys.stdin.readline().split())
    dic[v1].append(v2)
    dic[v2].append(v1)

print(*dfs(v,dic))
print(*bfs(v,dic))