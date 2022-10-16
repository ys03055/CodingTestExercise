import sys

from regex import B
# sys.stdin= open("input.txt", "rt")


#리스트 합치기
a = int(input())
n = list(map(int, input().split()))
b = int(input())
m = list(map(int, input().split()))
p1=p2= 0   # 포인터 설정해서 오름차순에 이용
c = []
while p1 < n  and p2 < m :
    if a[p1] <= a[p2] :
        c.append(a[p1])
        p1 +=1
    else :
        c.append(a[p2])
        p2 +=1
if p1 <n :
    c= c+a[p1:]
if p2 < n :
    c = c+a[p2:]
for x in c :
    print(x, end = ' ')  # 배열 원소 출력

