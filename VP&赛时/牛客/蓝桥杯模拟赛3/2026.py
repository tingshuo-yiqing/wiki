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

    cnt = [0] * 11

    ans = 0
    for i in range(20262027):
        nums = i
        while nums:
            cnt[nums % 10] += 1
            nums //= 10

        if cnt[2] == 2 and cnt[0] == 1 and cnt[6] == 1:
            ans += 1

        cnt[2] = cnt[0] = cnt[6] = 0
    
    print(ans)

if __name__ == "__main__":
    main()
