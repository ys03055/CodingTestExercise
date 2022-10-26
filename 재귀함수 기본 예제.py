import sys


# sys.stdin= open("input.txt", "rt")

#재귀함수 
# 재귀함수는 스택을 이용함
#LIFO

def DFS(x) :
    if x>0:
        DFS(x-1)
        print(x, end = ' ')

if __name__ == "__main__":
    n = int(input())
    DFS(n)
