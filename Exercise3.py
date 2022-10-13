a, b = map (int, input().split())
if a >= 0 and b >=45 :
    a= a
    b= b-45
    print(a,b)
elif a > 0 and b < 45 :
    a = a-1
    b = b -45 +60
    print(a,b)
else :
    a = a-1+24
    b = b-45+60 
    print(a,b)