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
    s = str(n)

    if s == s[::-1]:
        t = int(n ** 0.5)
        if t * t == n and str(t) == str(t)[::-1]:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    main()
