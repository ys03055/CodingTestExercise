from mmap import MAP_ANON
import sys

# sys.stdin= open("input.txt", "rt")

#큰수 찾기
#stack --> LIFO

n, m = map(int, input().split())
n = list(map(int, str(n)))   #스트링으로 리스트화
stack = []
for x in n :
    while stack and m >0 and stack[-1] < x:    #그냥 stack이라 쓰면 비어있으면 거짓이 되어 break됨.
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack = stack[:-m]
for x in stack:
    print(x,end='')
