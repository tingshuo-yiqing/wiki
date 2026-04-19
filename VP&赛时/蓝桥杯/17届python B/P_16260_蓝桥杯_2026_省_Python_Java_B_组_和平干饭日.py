import sys
sys.set_int_max_str_digits(10000)
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
    ans = 0

    r = ''
    for i in range(1, 2027):
        r += str(i)

        if int(r) % 26 == 0:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
