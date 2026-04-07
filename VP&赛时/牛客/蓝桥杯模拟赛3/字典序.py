import sys
from collections import Counter

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

    S = inp().split()

    T = []

    for s in S:
        cnt = Counter(s)
        a = sorted(cnt.keys())
        v = [0] * 26
        for i in range(26):
            c = chr(ord('a') + i)
            if c in a:
                v[i] = -cnt[c]
        # print(v)
        T.append((v, s))
    
    T.sort()

    for t in T:
        print(t[1], end=' ')
    

if __name__ == "__main__":
    main()
