from mmap import MAP_ANON
import sys

# sys.stdin= open("input.txt", "rt")

#쇠막대기 배치하기
#stack --> LIFO
#stack은 구덩이처럼 새워서 대입하면 보기 쉬움

s = input()
stack = []
cnt = 0
for i in range(len(S)):
    if s[i] == '(' :
        stack.append(s[i])
    else :
        if s[i-1] == '(' :    # ')' 일때 바로 앞이 '(' 이면 레이저이므로 확인
            stack.pop()
            cnt+=len(stack)
        else :
            stack.pop()
            cnt+=1
print(cnt)