import sys

# sys.stdin= open("input.txt", "rt")


#그리디 - 창고 물품 쌓기
#정렬 후 문제 해결

a = int(input())
b = list(map(int, input().split()))
c = int(input())
b.sort()

for _ in range(c) :
    b[0]+=1
    b[a-1]-=1
    b.sort()
d = 0
d = b[a-1] - b [0]
print(d)
