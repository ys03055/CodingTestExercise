import sys
from collections import deque

# sys.stdin= open("input.txt", "rt")

#해쉬_단어찾기
#dictionary 자료구조는 알파벳이나 단어를 index 번호로 사용가능.

n = int(input())
c = dict()
for i in range(n) :
    word =input()
    c[word] =1
for i in range(n-1):
    word=input()
    c[word]=0
for key, val in c.items():
    if val ==1:
        print(key)
        break
