import sys
input = sys.stdin.readline
"""
이미 등장했던 문자가 다시 나타났을 때, 바로 직전 문자였는가?
- (1) set에 원소 넣기
- (2) sorted(word, key=word.find)
    sorted(word, key)   : 이 기준에 맞춰서 줄 세우기
    word.find(문자)     : 문자가 word에 처음 나타나는 인덱스
    -> 문자열에 먼저 등장한 순서대로 정렬
"""

N = int(input())
group_count = 0

def is_group_word(word:str):
    seen = set()
    prev_letter = ''
    for char in word:
        if char in seen:
            if char != prev_letter:
                return False
        else: seen.add(char); prev_letter = char
    return True

for i in range(N):
    string = input().strip()
    if is_group_word(string): group_count += 1

print(group_count)