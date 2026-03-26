import sys
input = sys.stdin.readline
"""
정수를 str처럼 분해 후 .join으로 합쳐서 해결하는 사례.
"""

A, B = input().strip().split()
# 서로 다른 세 자리 수, 0이 포함되지 않음

A_read = ''.join(a for a in A[::-1])
B_read = ''.join(b for b in B[::-1])
print(max(A_read, B_read))