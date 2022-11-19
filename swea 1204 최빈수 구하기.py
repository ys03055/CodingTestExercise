T = int(input())
for tc in range(1,T+1) :
    tc_num=int(input())
    lists = list(map(int, input().split()))
    cnt = []
    maxi = []
    for i in range(0,101) :
        cnt.append(lists.count(i))
    maxNum = max(cnt)
    for x in range(len(cnt)) :
        if cnt[x] == maxNum :
            maxi.append(x)
    maxi.sort(reverse = True)
    print('#{} {}'.format(tc_num, maxi[0]))