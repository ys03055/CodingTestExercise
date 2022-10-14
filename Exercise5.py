import sys
sys.stdin= open("input.txt", "rt")

a, b = map(int, input().split())
c = list(map(int, input().split()))
d = set() #set은 중복인 수 제거 기능 있음
for i in range(a) :
    for j in range(i+1, a) :
        for m in range (j+1, a) :
            d.add(c[i]+c[j]+c[m])  # set은 append가 아니라 add임
d = list(d)   #set은 sort기능이 없으므로 리스트화 해야함
d.sort(reverse=True) #내림차순
print(d[b-1])