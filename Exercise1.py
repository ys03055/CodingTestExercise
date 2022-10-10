import sys
sys.stdin = open("input1.txt", "rt")

n,k = map(int, input().split())

a = 0
for i in range(1, n+1) :
    if n % i == 0 :
        a +=1
    if a == k :
        print(i)
        break
else :
    print("-1")    
      