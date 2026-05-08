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
    g = [LII() for _ in range(9)]

    for i in range(9):
        if len(set(g[i])) != 9:
            print("No")
            return
    
    col = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            col[i].add(g[j][i])

    for o in col:
        if len(o) != 9:
            print("No")
            return
    
    for i in range(3):
        for j in range(3):
            s = set()
            for x in range(i * 3, (i + 1) * 3):
                for y in range(j * 3, (j + 1) * 3):
                    s.add(g[x][y])
            if len(s) != 9:
                print("No")
                return

    print("Yes")

if __name__ == "__main__":
    main()
