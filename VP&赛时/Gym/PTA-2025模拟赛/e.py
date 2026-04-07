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
    n, m = MII()

    w = []
    for _ in range(n):
        s = inp()
        if "qiandao" in s:
            continue
        if "easy" in s:
            continue
        w.append(s)
    
    if m >= len(w):
        print("Wo AK le")
    else:
        print(w[m])

if __name__ == "__main__":
    main()
