import sys
from math import comb

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
        s, x = inp().split()
        if int(x) % 2 != 0:
            s = "Yes" if s == "No" else "No"
        print(s)

    print(comb(15, 7))
    print(comb(20, 10))
    print(2 ** 20)
          
if __name__ == "__main__":
    main()
