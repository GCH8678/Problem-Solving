import sys
# 길이가 짧은것 부터
# 길이가 같으면 사전순

n = int(sys.stdin.readline())
lst = list({input() for _ in range(n)})

lst.sort()
lst.sort(key= lambda x: len(x))

for word in lst:
    print(word)