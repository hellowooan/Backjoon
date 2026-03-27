import sys
input = sys.stdin.readline
"""
- ''.join(s for s in S[::-1])는 사실 S[::-1]와 동일한 결과를 낸다.
- 긴 문자열은 전체를 복사하지 않고 양 끝에서부터 문자를 비교하는 게 효율적.
"""

S = input().strip()
# S_reverse = ''.join(s for s in S[::-1])
S_reverse = S[::-1]
# print(1) if S==S_reverse else print(0)
# print(1 if S==S_reverse else 0)
is_palindrome = 1
for i in range(len(S)//2):
    if S[i] != S_reverse[i]:
        is_palindrome = 0
        break
print(is_palindrome)