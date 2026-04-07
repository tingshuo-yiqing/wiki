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
    s = inp()

    n = len(s)

    cnt = 0

    i = 0
    while i < n:
        t = s[i:i+3]

        a = b = c = 1

        for x in t:
            if x == 'l':
                a -= 1
            elif x == 'q':
                b -= 1
            elif x == 'b':
                c -= 1
        
        if a == b == c == 0:
            cnt += 1
            i = i + 3
        else:
            i += 1
    
    print(cnt)

if __name__ == "__main__":
    main()
