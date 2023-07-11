# 도감에 수록되어 포켓몬의 개수 N 
# 내가 맞춰야 하는 문제의 개수 M
# 1<= N,M <= 100,000

# 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력
# 일부 포켓몬은 마지막 문자만 대문자. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2. 

# 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력
# 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고
# 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력

# 1<= 입력으로 들어오는 숫자 <= N
# 문자는 반드시 도감에 있음

import sys

n,m = map(int,sys.stdin.readline().split())


lst = {}
cnt = 1
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    lst[name] = str(cnt)
    lst[str(cnt)] = name
    cnt+=1
for _ in range(m):
    problem = sys.stdin.readline().rstrip()
    #print(problem)
    print(lst.get(problem))
