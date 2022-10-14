import sys
sys.stdin= open("input.txt", "rt")

#대표값 구하기 알고리즘

a = int(input())
b = list(map(int, input().split()))
avg = round(sum(b)/a)   # 소수점 반올림 -> round 함수
min = 2147000000

for studentNum , x in enumerate(b) :
    tmp = abs(x-avg)
    if tmp<min :
        min = tmp
        score=x
        res=studentNum+1
    elif tmp==min:
        if x>score:
            score = x
            res=studentNum+1