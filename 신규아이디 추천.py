import re  

def solution(new_id):
    answer = ''
    step1 = new_id.lower()
    s= '1234567890abcdefghijklnmopqrstuvwxyz-_.'
    for i in step1 :
        if i not in s:
            step1 = step1.replace(i , "")
    step2 = list(step1)
    a = []
    for i in range(len(step2)) :
        if step2[i] != "." :
            a.append(step2[i])
        else :
            if a :
                if a[-1] == "." :
                    continue
                else :
                    a.append(step2[i])
            else :
                if step2[0] == "." :
                    a.append(step2[0])
                continue
    if a[0] == "." :
        if len(a) >1 :
            a = a[1:]
    if a[-1] == "." :
        if len(a) >1 :
            a = a[:-1]
        else :
            a = []
    if len(a) == 0 :
        a.append("a")
    if len(a) >= 16 :
        a = a[:15]
        if a[-1] == "." :
            a = a[:14]
    while len(a) <3 :
        a.append(a[-1])
        
    a = ''.join(a)
    return a
