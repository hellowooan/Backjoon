import sys
input = sys.stdin.readline
"""
파이썬에서 리스트의 요소를 정수로 나누려면
List Comprehension나 map을 사용하는 게 효율적이다.
"""

N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
new_scores = [s*100/M for s in scores]

print(sum(new_scores)/len(new_scores))

"""
import numpy as np
print(np.mean(new_scores))
"""