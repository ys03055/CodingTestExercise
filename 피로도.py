def solution(k, dungeons):
    answer = -1
    for i in range(len(dungeons)):
        cnt = 0
        for j in range(len(dungeons)) :
            if k >=dungeons[i][0] :
                k -=dungeons[i][1]
                cnt +=1
            else :
                continue
            print(k)
            print(cnt)
    return answer