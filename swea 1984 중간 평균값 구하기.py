T = int(input())
for tc in range(1, T+1) :
    n= list(map(int, input().split()))
    n.sort(reverse = True)
    n.pop()
    n.pop(0)
    ave = 0
    for i in range(len(n)) :
        ave +=n[i]
    ave = round(ave /len(n))
    print('#{} {}'.format(tc, ave))