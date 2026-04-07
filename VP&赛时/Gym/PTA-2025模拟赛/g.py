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
    a, b, n = MII()

    arr = [a, b]

    if n <= 2:
        print(*arr[:n])
        return 0

    l = 0
    while len(arr) < n:        
        nxt = str(arr[l] * arr[l + 1])
        l += 1

        if len(nxt) == 1:
            arr.append(int(nxt))
        else:
            arr.append(int(nxt[0]))
            arr.append(int(nxt[1]))

    print(*arr[:n])

if __name__ == "__main__":
    main()
