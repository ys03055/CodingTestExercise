import sys

# sys.stdin= open("input.txt", "rt")


#곳감 문제
#현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 
# 현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
#그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 
# 그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다. 
# 만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.


n= int(input())
a= [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h,t,k = map(int, input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))   #h행 1번째열 값을 마지막으로 옮김
    else :
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop(0))   #h행 1번째열 값에 대입
res = 0
s= 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i < n//2:
        s+=1
        e-=1
    else :
        s-=1
        e+=1
print(res)            

