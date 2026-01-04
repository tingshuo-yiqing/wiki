import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def get_index(idx, n, is_reverse):
    ret = idx
    if is_reverse:
        ret += n if idx < n else -n
    return ret

def main():
    n = int(input())
    s = list(input())
    
    is_reverse = 0
    for _ in range(int(input())):
        T = list(map(int, input().split()))

        if T[0] == 1:
            a = get_index(T[1] - 1, n, is_reverse)
            b = get_index(T[2] - 1, n, is_reverse)
            s[a], s[b] = s[b], s[a]
        else:
            is_reverse ^= 1
    
    s = ''.join(s)
    if is_reverse:
        s = s[n:] + s[:n]
    print(s)

if __name__ == "__main__":
    main()