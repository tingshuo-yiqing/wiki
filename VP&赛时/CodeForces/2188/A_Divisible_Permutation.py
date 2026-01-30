import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    for _ in range(II()):
        n = II()

        o = [0] * n
        b, c = 1, n

        for i in range(n):
            if i % 2 == 0:
               o[i] = b
               b += 1
            else:
               o[i] = c
               c -= 1
        
        print(*(o[::-1]))

if __name__ == "__main__":
    main()