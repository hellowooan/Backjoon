import sys
input = sys.stdin.readline
"""
배열을 Slicing해서 역순으로 할 때
[start:stop:step]
- 0번 인덱스를 포함할 때는 인덱스 숫자를 생략하는 게 표준
- -1번 인덱스를 포함하면 결과가 유효하지 않음

i-1부터 j까지의 범위를 역순([::-1])으로 뒤집어서 다시 대입
baskets[i-1:j] = baskets[i-1:j][::-1] 
"""

N, M = map(int, input().split())
baskets = [x for x in range(1,N+1)]

for m in range(M):
    i, j = map(int, input().split())
    # i번째 바구니부터 j번째 바구니의 순서를 역순으로
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(*baskets)