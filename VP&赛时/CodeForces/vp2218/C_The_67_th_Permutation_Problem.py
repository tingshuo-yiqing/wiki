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
    for _ in range(II()):
        n = II()

        # res = []
        # strat = n

        # t = []
        # for i in range(strat, n * 3, 2):
        #     t.append(i + 1)

        # # print(*t)
        # for i in range(1, n + 1):
        #     res.append(i)
        #     res.append(t[i-1])
        #     res.append(t[i-1] + 1)
        
        # print(*res)

        for i in range(1, n + 1):
            print(i, n + 2 * i - 1, n + 2 * i, end=' ')
        print()

if __name__ == "__main__":
    main()
