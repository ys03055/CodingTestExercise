def solution(numbers, hand):
    answer = ''
    LLocation = 0
    RLocation = 0
    for i in range(len(numbers)) :
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7 :
            answer += "L"
            LLocation = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9 :
            answer += "R"
            RLocation = numbers[i]
        else :
            if abs(numbers[i]-LLocation) > abs(numbers[i]-RLocation) :
                answer += "R"
                RLocation = numbers[i]
            elif abs(numbers[i]-LLocation) < abs(numbers[i]-RLocation) :
                answer += "L"
                LLocation = numbers[i]
            else :
                if hand == 'left' :
                    answer +="L"
                    LLocation = numbers[i]
                else :
                    answer +="R"
                    RLocation = numbers[i]
    print (answer)
    
    return answer