import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())


def main():
    n, m = MII()
    a = LII()
    b = LII()

    

if __name__ == "__main__":
    main()
