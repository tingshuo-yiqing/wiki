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
    a = LII()
    b = LII()
    c = LII()

    t = {4, 5, 6}

    ans = 0
    for i in a:
        for j in b:
            for k in c:
                s = set()
                s.add(i)
                s.add(j)
                s.add(k)
                if s == t:
                    ans += 1

    print(f'{ans / (6 * 6 * 6):.10f}')

if __name__ == "__main__":
    main()
