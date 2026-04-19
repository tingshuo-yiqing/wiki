import sys
from array import array

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num >= 2

def main():
    n = II()
    a = LII()

    def getvalue(num):
        divs = []
        for i in range(2, int(num **0.5) + 1):
            while num % i == 0:
                num //= i
                divs.append(i)
        if num != 1:
            divs.append(num)
        mi = mx = 1
        m = len(divs)
        cur = 1
        for i in range(m-1):
            cur *= divs[i]
            mi += cur
        cur = 1
        for i in range(m-1, 0, -1):
            cur *= divs[i]
            mx += cur
        return mi, mx

    mi = mx = 0
    for x in a:
        if x == 1:
            continue
        elif is_prime(x):
            mx += 1
            mi += 1
        else:
            c, d = getvalue(x)
            mi += c
            mx += d

    print(mi, mx)
        

if __name__ == "__main__":
    main()
