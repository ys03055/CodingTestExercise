import sys

# sys.stdin= open("input.txt", "rt")


#그리디 - 씨름 선수 선발
#정렬 후 문제 해결

a = int(input())
b = []
for i in range(a):
    l,k = map(int, input().split())
    b.append((l,k))
b.sort(reverse=True) #내림차순 정렬 ---> reverse = True 대입하면됨.
#만약 키가 아닌 몸무게로 정렬하려면 b.sort(key = lambda x : (x[1], x[0]))
cnt = 0
max_k = 0
for l , k in b :
    if k >= max_k :
        max_k = i
        cnt +=1
        #어차피 키는 정렬되어 있으니 상관안써도 되자나용
    
print(cnt)
