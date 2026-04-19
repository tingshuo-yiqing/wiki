import sys
from collections import defaultdict

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

    st = []
    cur_xor = 0

    outs = []
    for _ in range(n):
        s = inp().split()

        op = s[0]
        if op == "PUT":
            v = int(s[1])
            st.append(v)
            cur_xor ^= v
        elif op == "LOOK":
            outs.append(cur_xor)
        else:
            v = st.pop()
            cur_xor ^= v

    vised = defaultdict(int)
    # print(*outs)

    ans = []
    for i, x in enumerate(outs):
        if x not in vised:
            ans.append(-1)
        else:
            ans.append(vised[x])
        vised[x] = i + 1
    
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
