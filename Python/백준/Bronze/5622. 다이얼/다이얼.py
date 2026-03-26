import sys
input = sys.stdin.readline
"""
for key, value in DICT.items()
- DICT의 key, value 를 한꺼번에 호출

DICT[new_key] = new_value
- DICT에 새 key-value 쌍 삽입
"""

WORD = input().strip()  # 알파벳 대문자로 이루어진 단어
PHONE_NUM_DICT = {
    'ABC':2,
    'DEF':3,
    'GHI':4,
    'JKL':5,
    'MNO':6,
    'PQRS':7,
    'TUV':8,
    'WXYZ':9
}

total_time = 0

"""
for letter in WORD:
    for key in PHONE_NUM_DICT:
        if letter in key:
            num = PHONE_NUM_DICT[key]
    total_time += 2 + (num-1)
"""
# 이중 반복문을 줄이려면?
# 매 글자마다 dict의 모든 key를 훑으며 if ~ in ~를 사용하지 말고,
# 각 알파벳을 key로, 숫자를 value로 하는 dict를 재구성하자.

DIAL_TIME = {}
for key, value in PHONE_NUM_DICT.items():
    for letter in key:
        DIAL_TIME[letter] = 2 + (value-1)

for letter in WORD:
    time = DIAL_TIME[letter]
    total_time += time

print(total_time)