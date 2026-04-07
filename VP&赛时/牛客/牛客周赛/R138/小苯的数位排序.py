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

        def dig(num):
            return sum(map(int, str(num)))

        cnt = 0
        f = False
        for i in range(n-1, 0, -1):
            freq = 0
            while a[i] < a[i - 1]:
                if freq > 30:
                    f = True
                    break
                freq += 1
                a[i - 1] = dig(a[i - 1])
                cnt += 1
            if f:
                break
        
        print(cnt if not f else -1)

if __name__ == "__main__":
    main()
