def solution(n,a,b):
    answer = 0
    A =a
    B = b
    for i in range(n):
        if A > 1 and B >1:
            A = round(A/2)
            B = round(B/2)
            answer +=1
            print(answer)
        else :
            if A == 1 and B !=1 :
                B = round(B/2)
                answer +=1
            if A !=1 and B ==1 :
                A = round(A/2)
                answer +1
            else :
                break
    return answer