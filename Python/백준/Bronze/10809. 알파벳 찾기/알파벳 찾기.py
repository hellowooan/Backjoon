import sys
input = sys.stdin.readline
"""
.index() 등 1차원 배열의 함수는 문자열에도 적용할 수 있다.
- 만약 찾는 게 없으면 ValueError가 발생한다.
- BUT...

.find()
- 문자열에는 찾는 문자가 없을 때 -1을 반환하는 메서드가 있다.
- 예외 처리 없이 한 줄로 해결 가능

알파벳 리스트 모듈
import string
string.ascii_lowercase  #'abcderfhijklmnopqrstuvwxyz'

try, except
- 예외처리 구문
- (ex)
    try:
        실행할 코드
    except:
        예외가 발생할 때 처리하는 코드
"""

S = input().strip()     # 알파벳 소문자로만 이루어진 단어
"""
for i in range(ord('a'),ord('z')+1):
    try:
        letter_index = S.index(chr(i))
        print(letter_index, end=' ')
    except:
        print(-1, end=' ')
"""
import string
print(*[S.find(x) for x in string.ascii_lowercase])