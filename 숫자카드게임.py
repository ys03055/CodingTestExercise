n ,m= map(int,input().split())
l = []
for i in range(n):
    s = list(map(int,input().split()))
    l.append(s)
result = min(l[0])
for j in range(n) :
    if min(l[j]) > result :
        result = min(l[j])
    else :
        continue
print(result)
