import sys

# sys.stdin= open("input.txt", "rt")


#그리디 - 역수열
#정렬 후 문제 해결
#첫 배열 오름차순으로 생각하고 문제 풀기

a= int(input())
l = list(map(int, input().split()))
l.insert(0,0) # 맨 앞에 0을 대입해서 뒤로 밀어서 0번째가 아닌 1번째부터 값을 사용하도록 함. 
seq = [0]*a

for i in range(1, n+1) :
    for j in range(a) :
        if l[i] == 0 and seq[j] ==0 :    #l[i]==0 <--자기 앞 빈공간을 확보했기 때문에 자리에 들어가도 된다는 뜻
            seq[j] = i   #seq 자리가 0이 아니면 자리가 찬 것 이므로 다음 0인 값에 넣어하는 뜻
            break
        elif seq[j] ==0:
            l[i]-=1
for x in seq:
    print(x, end = ' ')
