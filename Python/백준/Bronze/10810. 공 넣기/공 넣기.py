import sys
input = sys.stdin.readline
"""
배열 범위(Slicing)에 값을 할당하기.
파이썬에서 리스트의 범위를 지정해 값을 바꿀 때는
오른쪽에 반드시 반복 가능한 객체 (iterable)
(e.g., List, Tuple)가 와야 한다.
- 잘못된 예시: LIST[i:j] = k
- 올바른 예시: LIST[i:j] = [k]*(j-i)
"""

N, M = map(int, input().split())
baskets = [0]*N     # 공이 들어있지 않은 바구니는 0을 출력.
for m in range(M):
    i, j, k = map(int, input().split())
    # i번 바구니부터 j번 바구니까지 k번 공을 넣음
    baskets[i-1:j] = [k]*(j-(i-1))
print(*baskets)