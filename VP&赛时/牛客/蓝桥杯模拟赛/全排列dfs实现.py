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

    path = []
    vised = [False] * (n + 1)
    def dfs(u):
        if u == n:

        for i in range(1, n + 1):
            if not vised[i]:
                vised[i] = True
                dfs(i + 1)
                vised[i] = False

if __name__ == "__main__":
    main()
