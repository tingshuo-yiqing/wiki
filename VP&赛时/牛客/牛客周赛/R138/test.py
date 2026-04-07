import sys
sys.setrecursionlimit(20000)
from collections import Counter, deque, defaultdict

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: [MII()]


def main():
    ...


if __name__ == "__main__":
    main()