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

    g = [inp() for _ in range(n)]

    def vaild(i, j, x, y):
        b = 0
        w = 0
        for k in range(6):
            a = i + x * k
            c = j + y * k
            if g[a][c] == '#':
                b += 1
            else:
                w += 1
        return w <= 2

    for i in range(n):
        for j in range(n):
                # 下
                if 0 <= i + 5 < n:
                    if vaild(i, j, 1, 0):
                        print("Yes")
                        return
                # 右
                if 0 <= j + 5 < n:
                    if vaild(i, j, 0, 1):
                        print("Yes")
                        return
                # 左下
                if 0 <= i + 5 < n and 0 <= j - 5 < n:
                    if vaild(i, j, 1, -1):
                        print("Yes")
                        return
                # 右下
                if 0 <= i + 5 < n and 0 <= j + 5 < n:
                    if vaild(i, j, 1, 1):
                        print("Yes")
                        return
    
    print("No")

if __name__ == "__main__":
    main()
