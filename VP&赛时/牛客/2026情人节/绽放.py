import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    # print("5201314")
    ans = 0
    with open('a.txt', 'r') as f:
        for c in f.read():
            
            ans += ord(c) - ord('a')

if __name__ == "__main__":
    main()