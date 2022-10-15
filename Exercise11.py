import sys

from sqlalchemy import false
# sys.stdin= open("input.txt", "rt")

#뒤집은후 소수화


def reverse(x) :
    res = 0
    while x > 0:
        t = x%10
        res= res*10+t
        x=x//10
    return res

# 114 예시
# t = 4  --> res = 4 --> x --> 11
# t = 1 -->  res = 41 --> x --> 1
# t = 1 --> res = 411 --> x --> 0
#break
#res = 411

def isPrime(x) :
    if x == 1:
        return False
    for i in range(2,x//2+1):
        if x%1 ==0 :
            return False
    else :
        return True




n = int(input())
a = list(map(int, input().split()))

for x in a :
    tmp = reverse(x)
    if isPrime(tmp) :
        print(tmp, end = ' ')







