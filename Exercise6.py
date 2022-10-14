import sys
sys.stdin= open("input.txt", "rt")

#최소값 구하기 알고리즘

arr= [5,7,432,234,65,34,324]
arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin :
        arrMin = arr[i]
print(arrMin)
