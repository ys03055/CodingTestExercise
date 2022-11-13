def solution(citations):
    answer = 0
    cnt = 0
    max = len(citations)
    a = []
    b = 0
    while max >0:
        for i in range(len(citations)) :
            if citations[i] >= max :
                cnt +=1
            if cnt == max :
                b = cnt
        max -=1
        cnt = 0
        a.append(b)
        a.sort()
        answer = a[-1]
    print(answer)
        

     
    return answer