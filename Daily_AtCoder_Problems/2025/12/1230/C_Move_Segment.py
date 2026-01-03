import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    s = input()

    segs = []

    i = 0
    while i < n:
        if s[i] == '1':
            j = i
            while j < n and s[j] == '1':
                j += 1
            segs.append((i, j))
            i = j + 1
        else:
            i += 1

    # print(segs)
    a, b = segs[k-2]
    c, d = segs[k-1]
    print(s[:b] + s[c:d] + s[b:c] + s[d:])

if __name__ == "__main__":
    main()