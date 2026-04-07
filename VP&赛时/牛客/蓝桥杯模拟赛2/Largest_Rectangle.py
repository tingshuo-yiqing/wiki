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

    g = [LII() for _ in range(n)]

    mat = [[1 - x for x in g[0]]]
    for i in range(1, n):
        t = []
        for j in range(m):
            t.append(mat[i-1][j] + 1 if g[i][j] == 0 else 0)
        mat.append(t)

    ans = 0
    for a in mat:
        st = []
        mil = [-1] * m
        for i, x in enumerate(a):
            while st and a[st[-1]] >= x:
                st.pop()
            if st:
                mil[i] = st[-1]
            st.append(i)
        st = []
        mir = [m] * m
        for i in range(m-1, -1, -1):
            while st and a[st[-1]] >= a[i]:
                st.pop()
            if st:
                mir[i] = st[-1]
            st.append(i)
        for i in range(m):
            area = a[i] * (mir[i] - mil[i] - 1)
            ans = Max(ans, area)
    
    print(ans)

if __name__ == "__main__":
    main()
