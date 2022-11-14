def solution(answers):
    person1 = [1, 2, 3, 4, 5]*2000
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    person1_cnt = 0
    person2_cnt = 0
    person3_cnt = 0
    answer = []
    max_cnt = []
    
    for i in range(len(answers)):
        if answers[i] == person1[i] :
            person1_cnt += 1
        if answers[i] == person2[i] :
            person2_cnt += 1
        if answers[i] == person3[i] :
            person3_cnt += 1

    max_cnt.append(person1_cnt) 
    max_cnt.append(person2_cnt)
    max_cnt.append(person3_cnt)

    if max(max_cnt) == person1_cnt :
        answer.append(1)
    if max(max_cnt) == person2_cnt :
        answer.append(2)
    if max(max_cnt) == person3_cnt :
        answer.append(3)

    return answer