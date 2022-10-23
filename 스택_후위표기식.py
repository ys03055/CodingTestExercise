from mmap import MAP_ANON
import sys

# sys.stdin= open("input.txt", "rt")

#중위표기식을 후위표기식으로 바꾸기
#stack --> LIFO
#조건문 세분화

a = input()
stack = []
res = ''
for x in a :
    if x .isdecimal():
        res+=x
    else :
        if x =='(' :
            stack.append(x)
        elif x == '*' or x =='/':
            while stack and (stack[-1] == '*' or stack[-1]=='/') :
                res +=stack.pop()
            stack.append(x)
        elif x == '+' or x =='-' :
            while stack and stack[-1] != '(' :
                res+=stack.pop()
            stack.append(x)
        elif x == ')' :     #괄호 안 수식부터 처리해야함
            while stack and stack[-1] != '(' :
                res+=stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)
