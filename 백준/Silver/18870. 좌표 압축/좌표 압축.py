#첫 째 줄 n
# 둘쨰 줄 x1,x2,x3,...,xn 
import sys

n = int(sys.stdin.readline())

lst = list(map(list,enumerate(map(int,sys.stdin.readline().split()))))

# lst 값 순으로 정렬
lst.sort(key=lambda x: x[1])
num = lst[0][1]
# result에 가장 작은 값을 가진 idx 넣기
# result => (갯수, idx)
result = [[0,lst[0][0]]]
#lst => (idx, x)
for i in lst[1:]:
    if i[1]>num:
        num = i[1]
        result.append([result[-1][0]+1,i[0]])
    else:
        result.append([result[-1][0],i[0]])
result.sort(key=lambda x: x[1])

print(*[i[0] for i in result])