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
    L = II()

    def cross(a, b):
        x1, y1 = a
        x2, y2 = b
        return x1 * x2 + y2 * y1
    
    cnt = 0
    for i in range(1, 51):
        for j in range(1, 51):
            for k in range(1, 51):
                for l in range(1, 51):
                    t = cross((i, j), (k, l))
                    # print(f"({i}, {j}) X ({k}, {l}) = {t}")
                    if t <= L:
                        cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()
