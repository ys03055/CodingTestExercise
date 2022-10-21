import sys

# sys.stdin= open("input.txt", "rt")


#그리디 - 회의시간 정하기

n = int(input())
meeting = []
for i in range(n):
    s ,e = map(int, input().split())
    meeting.append((s,e))   #튜플형태로 저장
meeting.sort(key=lambda x : (x[1], x[0]))  #끝나는 시간으로 정렬함
endtime = 0
cnt = 0
for s , e in meeting :
    if s >=endtime :
        endtime =e
        cnt+=1
print(cnt)
