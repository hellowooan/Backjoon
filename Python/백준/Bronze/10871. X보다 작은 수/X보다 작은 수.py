import sys
input = sys.stdin.readline
"""
List comprehension
- [표현식 for 항목 in 반복가능객체 if 조건]
- [표현식 if 조건 else 예외 for 항목 in 반복가능객체]
- 기존의 for loop보다 가독성이 좋고 속도가 빠르다.

Unpacking
리스트의 모든 요소를 개별 인자로 풀어서 print에 전달.

Join
리스트 안에 있는 요소들을 특정 문자(, \n)으로 연결.
- ",".join(map(str, 리스트))
"""
N, X = map(int, input().split())
LIST = list(map(int, input().split()))

results = [num for num in LIST if num<X]
print(*results)