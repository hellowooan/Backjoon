import sys
input = sys.stdin.readline
"""
x for x in 문자열
- list의 index처럼 각 문자를 꺼내옴.

sum(), min(), max(), join(), any(), all() 등...
- iterable를 인자로 받을 수 있는 함수이다.
- (ex) max(len(s) for s in strings)
- (ex) any(x>10 for x in nums)
- (ex) "".join(str(x) for x in nums)
"""

N = int(input())
NUMBERS = input().strip()

total_sum = sum(int(num) for num in NUMBERS)
print(total_sum)