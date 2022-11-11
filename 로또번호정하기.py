def reward (correct) :
    if correct == 6 :
        return 1
    elif correct == 5 :
        return 2
    elif correct == 4 :
        return 3
    elif correct == 3 :
        return 4
    elif correct == 2 :
        return 5
    else :
        return 6
    
def solution(lottos, win_nums):
    answer = []
    correct_low = 0
    correct_high = 0
    zero_point = 0
    high = 0
    low = 0
    for i in range(len(lottos)) :
        if lottos[i] ==0:
            zero_point +=1
        for j in range(len(win_nums)) :
            if lottos[i] !=0 :
                if lottos[i] == win_nums[j] :
                    correct_low += 1
                    correct_high +=1  

    correct_high +=zero_point

    print (correct_high)
    print(correct_low)
    high = reward(correct_high)
    low = reward(correct_low)
    answer = [high, low]
    print(answer)
        

    return answer