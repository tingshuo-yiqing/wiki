import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n = II()
    coins = sorted(LII(), reverse=True)
    a, b, c = coins

    limit = 9999

    ans = inf
    for i in range(limit):
        val_i = i * a
        if val_i > n:
            break
        rem_i = n - val_i

        for j in range(limit-i+1):
            val_j = j * b
            if val_j > rem_i:
                break
            rem_ij = rem_i - val_j

            if rem_ij % c == 0:
                k = rem_ij // c
                total = i + j + k
                if total <= limit:
                    ans = Min(ans, total)

    print(ans)

if __name__ == "__main__":
    main()