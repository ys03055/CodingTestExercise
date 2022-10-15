import sys
# sys.stdin= open("input.txt", "rt")

#소수 갯수 구하기 - 에라토스테네스 체

n = int(input())
a = [0] * n+1
b = 0
for i in range(2, n+1) :
    if a[i] == 0 :
        b +=1
        for j in range(i, n+1 , i) :
            a[j] = 1
print(b)




