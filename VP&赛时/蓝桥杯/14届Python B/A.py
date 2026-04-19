import sys
from math import inf
from heapq import heappush, heappop

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())


def main():
    s = 12345678
    e = 98765433

    ans = 0

    target = '2023'
    for i in range(s, e):
        t = str(i)
        j = 0
        for c in t:
            if j < 4 and c == target[j]:
                j += 1
            if j == 4:
                break
        if j < 4:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
