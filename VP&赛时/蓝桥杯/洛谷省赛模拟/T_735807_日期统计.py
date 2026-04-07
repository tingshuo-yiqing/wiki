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
    
    def is_leap(m):
        return m % 400 == 0 or (m % 4 == 0 and m % 100 != 0)
    
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    ans = 0
    for y in range(2239, 9876):
        for m in range(1, 13):
            if y == 2239 and m < 9:
                continue

            month[2] = 29 if is_leap(y) else 28

            for d in range(1, month[m] + 1):
                if y == 2239 and m == 9 and d < 9:
                    continue

                s = f"{y}{m}{d}"
                cnt = Counter(s)
                if len(set(cnt.values())) == 1:
                    print(f"{y}-{m}-{d}")
                    ans += 1
    print(ans)

    # print(210778)

if __name__ == "__main__":
    main()
