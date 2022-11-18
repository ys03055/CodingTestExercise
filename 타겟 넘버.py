from collections import deque
def solution(numbers, target):
    answer = 0
    dQ = deque()
    length = len(numbers)
    dQ.append([-numbers[0],0])
    dQ.append([numbers[0], 0])
    
    while dQ :
        num, i = dQ.popleft()
        if i + 1 == length :
            if num == target : 
                answer += 1
        else :
            dQ.append([num - numbers[i + 1], i + 1])
            dQ.append([num + numbers[i + 1], i + 1])        
    return answer