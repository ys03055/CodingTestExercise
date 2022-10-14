import sys
sys.stdin= open("input.txt", "rt")

#대표값 구하기 알고리즘

a = int(input())
b = list(map(int, input().split()))
avg = round(sum(b)/a)   # 소수점 반올림 -> round 함수

for i in range(a) :
    avg += b[i]
    avg = avg / a