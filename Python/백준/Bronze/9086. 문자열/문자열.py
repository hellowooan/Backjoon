import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    S = input().strip()
    print(S[0],S[-1],sep="")