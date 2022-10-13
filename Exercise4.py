import sys
sys.stdin= open("input.txt", "rt")

a, b = map(int, input().split())
c = list(map(int, input().split()))
d = []
for i in range(a) :
    if c[i] > c[i+1]