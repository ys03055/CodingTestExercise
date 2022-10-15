import sys
# sys.stdin= open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x) :
    sum = 0
    for i in str(x) :
        sum += int(i)
    return sum

max = -2147000000
for i in a :
    if digit_sum(i) >max :
        max = digit_sum(i)
        res = i
print(res)




