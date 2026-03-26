import sys
input = sys.stdin.readline
"""
.remove(), .del(), .pop(), .clear()
리스트에서 특정 값을 제거하는 함수
- remove: 리스트에 같은 값이 2개 있을 경우, 첫번째 요소만 삭제
- del: index 번호를 사용해서 값을 삭제
- pop: index 번호를 사용해서 값을 삭제, 미 지정 시 맨 끝에 있는 값 삭제
- clear: 모든 요소 제거

.sort()
리스트를 오름차순으로 정렬

.sort(reverse=True)
리스트를 내림차순으로 정렬 
"""

NUMS = [x for x in range(30,0,-1)]

# 입력은 28줄
for i in range(28):
   NUMS.remove(int(input()))

print(f"{NUMS.pop()}\n{NUMS.pop()}")