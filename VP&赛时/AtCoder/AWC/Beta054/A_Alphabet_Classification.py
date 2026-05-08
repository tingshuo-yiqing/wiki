import sys

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
    n = II()
    from collections import defaultdict

    cnt = defaultdict(list)

    for _ in range(n):
        s = inp()

        cnt[s[0]].append(s)
    
    print(max(len(v) for v in cnt.values()))

if __name__ == "__main__":
    main()
