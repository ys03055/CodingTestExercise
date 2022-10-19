import sys
sys.stdin=open("input.txt", "r")
def Count(len):     #배열 차이 구하는 함수
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()     #문제에 따라 오름차순 정렬.
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2    #이분 검색 사용
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
