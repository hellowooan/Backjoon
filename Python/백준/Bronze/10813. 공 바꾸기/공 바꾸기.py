import sys
input = sys.stdin.readline
"""
리스트에서 값 교환
a, b = b, a
- 파이썬 내부적으로는 우변의 값들을 Tuple로 묶었다가
좌변의 변수들에 각각 할당하는 방식을 취한다.
(메모리 상에 임시로 두 값이 저장)
- 즉, 우변이 완전히 계산된 후에 할당이 시작된다.
- C에서는 반드시 temp 변수가 필요하지만, 파이썬에선 괜찮다.
"""

N, M = map(int, input().split())
baskets = [x for x in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split())
    # i번 바구니와 j번 바구니에 있는 공을 교환
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]
    
print(*baskets)
