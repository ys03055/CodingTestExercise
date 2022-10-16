import sys
# sys.stdin= open("input.txt", "rt")


# 앞 뒤가 똑같은 문자열
n = int(input())

for i in range(n):
    a = input()
    a= a.upper()  #대문자로 바꾸기
    size = len(a)
    for j in range(size//2) :    #2개씩 비교하므로
        if a[j] == a[-1-j] :    # 양 끝 비교  (배열 첫번째 -> 0 , 배열 맨 끝 -> -1)
            print('#%d YES' %(i+1))
        else :
            print('#%d No' %(i+1))

     # if s==s[::-1] :        
     # print("#%d Yes" %(i+1))
     # else:
     # print("#%d No" %(i+1))       








