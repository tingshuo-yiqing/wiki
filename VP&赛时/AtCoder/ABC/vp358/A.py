import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    s, t = inp().split()

    if s == "AtCoder" and t == "Land":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()