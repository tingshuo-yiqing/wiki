import sys
from bisect import bisect_left

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    n, m = MII()

    a = sorted(LII())
    b = sorted(LII())

    if n < m:
        target = b
        arr = a
    else:
        target = a
        arr = b

    # 从更多的一方寻找，对target进行二分

    vised = [False] * len(target)

    print(0)

if __name__ == "__main__":
    main()
