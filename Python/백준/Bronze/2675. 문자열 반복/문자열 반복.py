import sys
input = sys.stdin.readline
"""
.join
- 리스트의 요소들을 하나의 문자열로 합칠 때
- 흩어져 있는 문자열 데이터를 정돈된 하나의 텍스트로 만들 때

[Recap]
sum(), min(), max(), join(), any(), all() 등...
- iterable를 인자로 받을 수 있는 함수이다.
- (ex) max(len(s) for s in strings)
- (ex) any(x>10 for x in nums)
- (ex) "".join(str(x) for x in nums)
"""

T = int(input())
for t in range(T):
    data = input().split()
    R, S = int(data[0]), data[1]
    P = ''.join(s*R for s in S)
    print(P)