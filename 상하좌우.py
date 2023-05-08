n = int(input())
p = input().split()
x = 1
y = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
direction = ["L","R","U","D"]

for i in p :
    for j in range(4) :
        if i == direction[j] :
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
    else :
        print(nx, ny)
        x = nx
        y = ny

print(x,y)
        
