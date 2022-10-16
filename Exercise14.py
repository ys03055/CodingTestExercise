import sys
# sys.stdin= open("input.txt", "rt")


#카드 역배치
n = list(range(21))  #0~20까지 배열 생성
for _ in range(10) :
    a, b = map(int, input().split())
    for i in range((b-a+1)//2) :
        n[a+i] , n[b-i] = n[b-i] , n[a+i]   #서로 값 바꾸기
a.pop(0)  #0번째 값 0 제거
for i in n:  # 콤마 제거
    print(i , end = ' ')















