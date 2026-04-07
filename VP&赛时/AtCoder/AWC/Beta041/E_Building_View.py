import sys
from bisect import bisect_left

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())


def main():
    n, q = MII()
    a = LII()

    L = [-1] * n
    st = []
    for i, x in enumerate(a):
        while st and a[st[-1]] <= x:
            st.pop()
        if st:
            L[i] = st[-1]
        st.append(i)

    R = [n] * n
    st = []
    for i in range(n-1, -1, -1):
        while st and a[st[-1]] <= a[i]:
            st.pop()
        if st:
            R[i] = st[-1]
        st.append(i)

    # print(*L)
    # print(*R)

    T = []
    for i in range(n):
        if L[i] != -1 and R[i] != n:
            T.append(R[i] - L[i] - 1)
        elif L[i] == -1 and R[i] != n:
            T.append(R[i])
        elif L[i] != -1 and R[i] == n:
            T.append(n - L[i] - 1)
        else:
            T.append(n)

    T.sort()

    outs = []
    for _ in range(q):
        x = II()
        
        i = bisect_left(T, x)

        outs.append(n - i)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
    
