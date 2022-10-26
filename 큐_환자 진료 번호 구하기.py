import sys
from collections import deque

# sys.stdin= open("input.txt", "rt")

#큐_환자 진료 번호 구하기

n, m = (map(int, input().split()))
q = [(pos, Val) for pos, Val in enumerate(list(map(int, input().split())))]
#리스트 받고 [index, index_Value] 처럼 튜플형태로 변경
q = deque(q)
cnt = 0
while True:
    cur=q.popleft()    #cur[0] --> index 값, cur[1] --> index_value 값
    if any(cur[1]<x[1] for x in q) :   #x는 튜플값
        q.append(cur)
    else :
        cnt+=1
        if cur[0] ==m :
            break
print(cnt) 
