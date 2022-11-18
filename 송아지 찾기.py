import sys
from collections import deque
sys.stdin=open("input.txt" , "r")
MAX = 10000
cnt = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m=map(int, input().split())
cnt[n] = 1
dis[n] = [0]
dQ = deque()
dQ.append(n)
while dQ :
    now = dQ.popleft()
    if now == m :
        break
    for next in (now-1,now+1,now+5) :
        if 0<next<MAX+1 :
            if cnt[next] == 0:
                dQ.append(next)
                cnt[next] =1
                dis[next] = dis[now]+1
print(dis[m])
