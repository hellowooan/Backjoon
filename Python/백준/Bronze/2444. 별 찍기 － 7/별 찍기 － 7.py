import sys
input = sys.stdin.readline

N = int(input())

"""
line = [' ']*(2*N-1)   # index 0 ~ 2*N-2
                    # 중간(N번째) index : N-1
middle_index = N-1
for i in range(N):
    start_index = middle_index - i
    end_index   = middle_index + i + 1
    star_count = 1 + 2*i
    new_line = line[:]
    new_line[start_index:end_index] = ['*']*star_count
    print(*new_line)
"""

for i in range(1, N+1):
    spaces = N - i
    stars = 2*i - 1
    print(' '*spaces+'*'*stars)
for i in range(N-1, 0, -1):
    spaces = N - i
    stars = 2*i - 1
    print(' '*spaces+'*'*stars)