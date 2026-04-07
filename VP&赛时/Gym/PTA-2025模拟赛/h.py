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
    n, m, h = MII()

    g = [LII() for _ in range(n)]

    def good(x, y):
        cnt = 0

        for i in range(1, n + 1):
            a = x + i
            if 0 <= a < n:
                if g[a][y] >= h:
                    break
                if g[a][y] < 0:
                    cnt += 1
        
        for i in range(1, n + 1):
            a = x - i
            if 0 <= a < n:
                if g[a][y] >= h:
                    break
                if g[a][y] < 0:
                    cnt += 1
        
        for i in range(1, m + 1):
            a = y + i
            if 0 <= a < m:
                if g[x][a] >= h:
                    break
                if g[x][a] < 0:
                    cnt += 1

        for i in range(1, m + 1):
            a = y - i
            if 0 <= a < m:
                if g[x][a] >= h:
                    break
                if g[x][a] < 0:
                    cnt += 1

        return cnt >= 3, cnt
    
    mx = 0
    ai = aj = ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                ok, cnt = good(i, j)
                if ok:
                    ans += 1
                if ok and cnt > mx:
                    mx = cnt
                    ai = i
                    aj = j

    print(ans)
    print(ai, aj)

if __name__ == "__main__":
    main()
