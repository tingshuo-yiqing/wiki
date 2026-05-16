import sys
from collections import Counter

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
    q, m = MII()
    C = [0] + LII()

    tot = 0
    for _ in range(q):
        n = MII()
        a = LII()

        cnt = Counter(a)

        for c, v in cnt.items():
            if v <= C[c]:
                tot += v
    
    print(tot)


if __name__ == "__main__":
    main()
