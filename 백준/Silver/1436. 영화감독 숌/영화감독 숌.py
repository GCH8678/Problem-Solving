import sys

n = int(sys.stdin.readline())

#N 번째 영화의 재목

count = 1
result = 666
while count<n:
    result+=1
    if "666" in str(result):
        count+=1
print(result)