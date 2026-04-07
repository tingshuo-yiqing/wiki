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
    n, k = MII()

    a = LII()

    i = cnt = 0

    while i < n:
        j = i

        while j < n and a[j] == 1:
            j += 1

        cnt += 1 if (j - i) >= k else 0

        i = j + 1

    print(cnt) 

if __name__ == "__main__":
    main()
