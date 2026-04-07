import sys
from collections import deque

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

        a = LII()

        st = []
        l = [-1] * n
        for i, x in enumerate(a):
            while st and a[st[-1]] <= x:
                st.pop()
            if st:
                l[i] = st[-1]
            st.append(i)
        
        st = []
        r = [n] * n
        for i in range(n-1, -1, -1):
            while st and a[st[-1]] < a[i]:
                st.pop()
            if st:
                r[i] = st[-1]
            st.append(i)
        
        ans = 0

        for i, x in enumerate(a):
            if r[i] - l[i] == x + 1:
                ans += 1

        print(ans)

if __name__ == "__main__":
    main()
