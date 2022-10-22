from mmap import MAP_ANON
import sys

# sys.stdin= open("input.txt", "rt")

#중위표기식을 후위표기식으로 바꾸기
#stack --> LIFO

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
            while stack and (stack[-1] == '*' or stacl[-1]=='/') :
                res +=stack.pop()
            stack.append(x)
        elif x == '+' or x =='-' :
            while stack and stack[-1] != '(' :
                res+=stack.pop()
            stack.append(x)
        elif x == ')' :
            while stack and stack[-1] != '(' :
                res+=stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)
