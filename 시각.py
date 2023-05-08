n = int(input())
result = 0
for i in range(0,n+1) :
    for j in range(0,60) :       
        for k in range(0,60) :
            if i // 10 == 3 or j // 10 ==3 or k // 10 ==3 or i %10 == 3 or j %10 == 3 or k %10 ==3 :
                result +=1
            

print(result)