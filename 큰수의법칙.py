n,m,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse=True)
first = l[0]
second = l[1]
result = 0
while True :
    for i in range(k) :
        if m ==0 :
            break
        else :
            result +=first
            m -=1
    if m == 0:
        break
    result +=second
    m-=1
print(result)

