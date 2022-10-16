import sys
# sys.stdin= open("input.txt", "rt")


#숫자 뽑아내기
n = input()
a = 0
b=0
for i in n :
    if i.isdecimal() :
        a = a*10+int(i)

for i in range(1, a+1) :
    if a % i ==0:
        b+=1
print(a)
print(b)











