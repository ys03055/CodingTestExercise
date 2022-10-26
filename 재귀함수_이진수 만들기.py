import sys


# sys.stdin= open("input.txt", "rt")

#재귀함수_이진수
# 재귀함수는 스택을 이용함
#LIFO

def DFS(x):
    if x==0:
        return
    else :
        #print(x%2, end = ' ') ---> 여기에 프린트 넣으면 1101
        DFS(x//2)
        print(x%2, end = ' ') # --> 여기에 프린트 넣으면 반대로 1011 나옴 ###스택 성질 이용###

if __name__ == "__main__":
    n = int(input())
    DFS(n)
    