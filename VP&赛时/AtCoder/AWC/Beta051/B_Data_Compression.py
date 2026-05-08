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
    s = inp() + '#'
    n = len(s)

    cnt = []

    i = 0
    while i < n:
        j = i + 1
        while j < n and s[j - 1] == s[j]:
            j += 1
        cnt.append((s[i], j - i))
        i = j
    
    res = []
    for c, v in cnt:
        res.append(c if v == 1 else f'{c}{v}')
    
    res.pop()
    print(''.join(res))

if __name__ == "__main__":
    main()
