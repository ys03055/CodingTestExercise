def solution(k, dungeons):
    cnt = 0
    answer = -1
    a = len(dungeons)
    for i in range(len(dungeons)) :
        if k >=dungeons[i][0] :
            k -=dungeons[i][1]
            cnt +=1
        else :
            continue
    print(cnt)
    return answer