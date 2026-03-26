import sys
input = sys.stdin.readline
"""
아스키 코드로 문자 표현
- ord()     : 문자를 아스키 코드 정수로 변환
- char()    : 아스키 코드 정수를 문자로 변환
"""

STRING = input().strip()
print(ord(STRING))