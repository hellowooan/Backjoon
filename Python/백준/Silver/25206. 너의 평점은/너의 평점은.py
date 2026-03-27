import sys
input = sys.stdin.readline
"""
continue
- 현재 진행 중인 루프의 남은 코드를 실행하지 않고,
- 즉시 다음 Iteration으로 넘어감
"""

# 20줄에 걸쳐 과목명/학점/등급이 주어짐
credit_count   = 0.0
gpa_sum         = 0.0

GPA_PER_GRADE = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F' :0.0
}

for i in range(20):
    lecture, credit, grade = input().strip().split()
    credit = float(credit)
    if grade == 'P':
        continue
    else:
        credit_count += credit
        gpa_sum += credit*GPA_PER_GRADE[grade]

gpa_avg = format(gpa_sum/credit_count,".6f")
print(gpa_avg)