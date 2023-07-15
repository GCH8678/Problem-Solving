import sys



m = int(sys.stdin.readline())
#s=set()
s=[False]*20
allS = [True]*20
emptyS = [False]*20
for _ in range(m):
    fn = sys.stdin.readline().split()

    if fn[0] == "add":
        s[int(fn[1])-1] = True
    elif fn[0]=="remove":
        s[int(fn[1])-1] = False
    elif fn[0]=="check":
        if s[int(fn[1])-1]:
            print(1)
        else:
            print(0)
    elif fn[0]=="toggle":
        s[int(fn[1])-1] = not s[int(fn[1])-1]
    elif fn[0]=="all":
        s=allS
    else:
        s=emptyS
