def solution(n, lost, reserve):
    answer = 0
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            if lost[i] == reserve[j]+1 or lost[i] == reserve[j]-1:
                answer +=1
                lost[i] =123
                reserve[j] = 123
            if lost[i] == reserve[j] :
                lost[i] =123
                reserve[j] = 123
    answer += (n-len(lost))
    return answer