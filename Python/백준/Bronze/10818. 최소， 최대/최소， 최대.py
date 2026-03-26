import sys
input = sys.stdin.readline
"""
min(), max()
- 리스트의 최댓값과 최솟값을 구할 수 있는 내장함수
"""

N = int(input())
LIST = list(map(int, input().split()))

max_value = max(LIST)
min_value = min(LIST)
print(min_value, max_value)