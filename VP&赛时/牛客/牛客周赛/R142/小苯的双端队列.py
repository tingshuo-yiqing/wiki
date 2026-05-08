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
    for _ in range(II()):
        n = II()
        a = LII()

        l = 1
        r = n

        ok = True
        for x in a:
            if x == l:
                l += 1
            elif x == r:
                r -= 1
            else:
                print("NO")
                ok = False
                break
        
        if ok:
            print("YES")

if __name__ == "__main__":
    main()
