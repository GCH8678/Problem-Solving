import sys

s = sys.stdin.readline()

r=s.split('-')

m = list(map(list,[i.split('+') for i in r]))


lst = []
for i in m:
    sum = 0
    for j in i:
        sum+=int(j)
    lst.append(sum)

answer = lst[0]
for i in range(1,len(lst)):
    answer -=lst[i]

print(answer)