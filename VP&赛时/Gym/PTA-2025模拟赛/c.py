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

    if n <= 100:
        if n % 10 == 0:
            n -= 10
        else:
            n -= n % 10
    else:
        n = 100
    
    print(f"Gong xi nin! Nin de ti zhong yue wei: {n} duo jin")

if __name__ == "__main__":
    main()
