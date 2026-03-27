import sys
input = sys.stdin.readline
"""
.replace(바꾸기 전, 바꾼 후)
- '특정 패턴을 찾아 하나로 취급하기'에 최적화됨.
- 두 글자나 세 글자가 모여 알파벳이 될 때 등...
"""

"""
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
(ex) ljes=njak -> lj, e, š, nj, a, k
"""

STRING = input().strip()

"""
LENGTH = len(STRING)
count = 0
i = 0
while i <= LENGTH-1: 
    if i <= LENGTH-3 and \
        STRING[i:i+3] == 'dz=':
        i += 3
    elif i <= LENGTH -2 and \
        STRING[i:i+2] in ['c=','c-','d-','lj','nj','s=','z=']:
        i += 2
    else:
        i += 1
    count += 1
print(count)
"""

CROATIAN = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for char in CROATIAN:
    STRING = STRING.replace(char, '*')
print(len(STRING))
