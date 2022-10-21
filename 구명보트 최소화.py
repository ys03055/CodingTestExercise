import sys

# sys.stdin= open("input.txt", "rt")


#그리디 - 구멍보트 최소갯수 구하기
#정렬 후 문제 해결

a ,b = map(int, input().split())
c = list(map(int, input().split()))
c.sort()

cnt = 0

#for문만 생각하지 말고 while문도 생각하자 ㅠㅠㅠ
while c:    #이렇게 조건 걸면 배열 c가 비어있으면 거짓, 비어 있지 않으면 참
    if len(c) ==1 :   #한명이 남았을 때, 논리적 오류가 발생하므로 조건문 추가.
        cnt+=1
        break
    if c[0] + c[-1] > b :
        c.pop()    #pop()을 하면 맨 뒤에 있는 수가 빠짐
        cnt+=1
    else :
        c.pop(0)
        c.pop()
        cnt+=1
print(cnt)
