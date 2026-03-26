import sys
input = sys.stdin.readline
"""
.index()
- 배열에서 값의 위치를 찾아주는 함수.
- 중복된 값이 있으면 가장 최소의 위치를 return
"""

LIST = []
for i in range(9):
    LIST.append(int(input()))

max_value = max(LIST)
index = LIST.index(max_value) + 1

print(max_value)
print(index)