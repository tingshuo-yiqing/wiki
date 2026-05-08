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
    c = II()
    for case in range(c):
        a = LII()
        ans = 0

        n = len(a)
        for i in range(1, n):
            for j in range(i + 1, n):
                if a[j] < a[i]:
                    ans += 1
        print(f"Scenario #{case+1}:")
        print(ans)
        if case < c - 1:
            print()

if __name__ == "__main__":
    main()
