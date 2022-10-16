import sys
# sys.stdin= open("input.txt", "rt")


#숫자 뽑아내기
n = input()
a = 0
b=0
for i in n :
    if i.isdecimal() :         # isdigit ==> 숫자 형태 다 뻡기
        a = a*10+int(i)        # isdecimal ==> 0~9 숫자 뽑기

for i in range(1, a+1) :
    if a % i ==0:
        b+=1
print(a)
print(b)











