import sys

def add(s:set,x:int):
    if x not in s:
        s.add(x)

def remove(s:set,x:int):
    if x in s:
        s.remove(x)

def check(s:set,x:int):
    if x in s:
        print(1)
    else:
        print(0)

def toggle(s:set,x:int):
    if x in s:
        s.remove(x)
    else:
        s.add(x)

def all():
    return set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def empty():
    return set()


m = int(sys.stdin.readline())
s=set()
for _ in range(m):
    fn = list(sys.stdin.readline().split())

    if fn[0] == "add":
        add(s,int(fn[1]))
    elif fn[0]=="remove":
        remove(s,int(fn[1]))
    elif fn[0]=="check":
        check(s,int(fn[1]))
    elif fn[0]=="toggle":
        toggle(s,int(fn[1]))
    elif fn[0]=="all":
        s=all()
    else:
        s=empty()
