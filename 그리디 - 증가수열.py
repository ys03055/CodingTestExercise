import sys

# sys.stdin= open("input.txt", "rt")


#그리디 - 증가수열
#정렬 후 문제 해결

a = int(input())
b = list(map(int, input().split()))
lt = 0
rt = a-1
last = 0
res=""
tmp = []
while lt <=rt :
    if a[lt] > last :
        tmp.append((a[lt], 'L'))
    if a[rt] > last :
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) ==0:
        break
    else:
        res = res +tmp[0][1]   #위의 튜플 값에서 [0]이면 투플에서 앞의 값, [1]이면 뒤의 값
        last = tmp[0][0]
        if tmp[0][1] =='L' :
            lt+=1
        else :
            rt -=1
        tmp.clear()
print(len(res))
print(res)     
