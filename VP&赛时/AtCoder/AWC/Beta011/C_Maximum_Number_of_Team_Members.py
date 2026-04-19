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
    n, k = MII()
    a = LII()

    ans = 0
    cur = 0
    for x in a:
        if (x | k) == k:
            ans += 1
            cur |= x   #! 所选的数必须要包含k的所有位
    
    if ans and cur == k:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()
