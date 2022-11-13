def solution(array, commands):
    arr = []
    answer = []
    for i in range(len(commands)) :
        value = 0
        if commands[i][0] == commands[i][1] :
            arr = array[commands[i][0]-1]
            value = arr
        else :
            arr = array[commands[i][0]-1:commands[i][1]]
            arr.sort()
            value = arr[commands[i][-1]-1]
        answer.append(value)  
    
    return answer