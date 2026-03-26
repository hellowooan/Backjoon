import sys
input = sys.stdin.readline
"""
.count()
매개변수로 입력된 값이 리스트 안에 몇개 있는지 세어 반환
"""

N = int(input())    # 1 <= N <= 100
LIST = list(map(int, input().split()))
V = int(input())    # -100 <= V <= 100

count = LIST.count(V)
print(count)