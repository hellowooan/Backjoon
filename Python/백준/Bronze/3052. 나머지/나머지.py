import sys
input = sys.stdin.readline
"""
리스트에서 '다른 값 찾기': Set
집합은 중복된 요소를 합쳐준다.
- 순서가 없고, 인덱스가 없는 모음
- 기존의 값을 어떤 값으로 수정할 수 없다. (remove는 가능)
- .remove() : 빼고 싶은 원소를 뺌
- .add()    : 더하고 싶은 원소를 추가함
- .update() : 한꺼번에 여러 원소를 추가함
"""

num_set = set()
# 1~10번째 줄까지 숫자가 주어짐
for i in range(10):
    num_set.add(int(input())%42)
print(len(num_set))