import sys
input = sys.stdin.readline

KING, QUEEN, ROOK, VISHOP, KNIGHT, PAWN \
= map(int, input().strip().split())

print(1-KING,
      1-QUEEN,
      2-ROOK,
      2-VISHOP,
      2-KNIGHT,
      8-PAWN,
      sep=' ')