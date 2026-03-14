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
    a = LII()

    if sum(a) != 0:
        print("YES")
        print(1, n)
    else:
        s = sum(a)
        cur = 0
        for i in range(n):
            cur += a[i]
            if s - cur != 0:
                print("YES")
                print(2)
                print(1, i + 1)
                print(i + 2, n)
                return
    print("NO")

if __name__ == "__main__":
    main()
