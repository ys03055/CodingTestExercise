def fullGrade(a,b,c) :
    midterm = int(a) *0.35
    finalterm = int(b) *0.45
    homework = int(c)*0.20
    return midterm + finalterm + homework


T = int(input())
for tc in range(1,T+1):  
    n, k = map(int, input().split())
    grade = []
    grade2 = []
    k_grade = 0
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(1,n+1) :
        grade.append(list(input().split()))
    for x in range(len(grade)) :
        a = grade[x][0]
        b = grade[x][1]
        c = grade[x][2]
        grade2.append(fullGrade(a,b,c))
    k_grade = grade2[k-1]
    grade2.sort(reverse = True)
    k_grade_index = grade2.index(k_grade)
    div = n //10
    answer = grades[k_grade_index//div]
    print('#{} {}'.format(tc, answer))