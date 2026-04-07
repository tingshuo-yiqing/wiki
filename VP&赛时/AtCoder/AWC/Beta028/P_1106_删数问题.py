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
    s = [int(c) for c in inp()]

    k = II()

    st = []
    for x in s:
        while k and st and st[-1] > x:
            st.pop()
            k -= 1
        st.append(x)
    
    for _ in range(k):
        st.pop()

    i = 0
    while i < len(st) and st[i] == 0:
        i += 1
    st = st[i:]
    
    if st:
        print(''.join(map(str, st)))
    else:
        print(0)

if __name__ == "__main__":
    main()
