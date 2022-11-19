def solution(number, k):
    answer = ""
    stack = [number[0]]
    for i in number[1:] :
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -=1
        stack.append(i)
    for x in range(len(stack)) :
        answer += stack[x]
    return answer if k == 0 else "".join(stack[:-k])