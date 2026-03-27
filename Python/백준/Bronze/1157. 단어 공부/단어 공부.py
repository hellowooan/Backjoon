import sys
input = sys.stdin.readline
"""
collections.Counter, Counter()
.count()를 여러번 호출하지 않아도...
'개수 세기'가 나오면 무조건 떠올리는 게 좋다.
- 각 문자의 빈도수를 딕셔너리 형태로 계산 가능
- (ex)  Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
        >>> Counter({'hi': 3, 'hey': 2, 'hello': 1})

Counter().most_common()
- 빈도수가 높은 순서대로 정렬
- 튜플의 리스트로 반환
- (ex)  [('A', 2), ('B', 2), ('C', 1)]
"""

S = input().strip().upper()

"""
# 기존 방식의 문제: 더 큰 최댓값이 나올 수 있는데 미리 break
freq_letter = ''
freq_count = 0
for s in set(S):
    new_letter = s
    new_count = S.count(s)
    if freq_count == new_count:
        freq_letter = '?'
        break
    elif freq_count < new_count:
        freq_letter = s
        freq_count = new_count
print(freq_letter)
"""

from collections import Counter
count = Counter(S)
most_common = count.most_common()
if len(most_common) == 1:
    print(most_common[0][0])
elif most_common[0][1] == most_common[1][1]:
    print('?')
else:
    print(most_common[0][0])
