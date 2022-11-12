def solution(s):
    a = []
    b = 0
    c = 0
    a =s.split(" ")
    int_a= list(map(int,a))
    int_a.sort()
    b = max(int_a)
    b = str(b)
    c = min(int_a)
    c = str(c)

    answer = ''
    answer =  c+ " " + b
    return answer