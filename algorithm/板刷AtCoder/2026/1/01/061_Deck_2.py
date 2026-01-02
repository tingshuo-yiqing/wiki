import sys
from collections import deque
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def slove_deque(data):
    outs = []

    d = deque()
    for o, x in data:
        if o == 1:
            d.appendleft(x)
        elif o == 2:
            d.append(x)
        else:
            outs.append(d[x-1])  # O(k)
    return outs


def slove_array(data):
    outs = []

    n = 2 * 10 ** 5 
    d = [0] * n

    l = n // 2
    r = l + 1

    for o, x in data:
        if o == 1:
            d[l] = x
            l -= 1
        elif o == 2:
            d[r] = x
            r += 1
        else:
            outs.append(d[l + x])  # O(1)
    return outs


def main():
    data = []
    for _ in range(int(input())):
        o, x = map(int, input().split())
        data.append((o, x))
    print(*slove_array(data), sep='\n')
    # print(*slove_deque(data), sep='\n')


if __name__ == "__main__":
    main()