def solution(s):
    a = []
    a = s.split(" ")
    answer = ''
    for i in a:
        answer += i.capitalize() +' '
    answer = answer[:-1]
        
    return answer  