import sys

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

def border(s):
    n = len(s)
    L = 0
    for i in range(1, n):
        if s[:i] == s[n-i:n]:
            L = i
    return L

def main():
    n, k = MII()
    
    s = inp()

    pi = [0] * n

    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    
    L = pi[n - 1]
    
    print(s + (k - 1) * (s[L:]))

if __name__ == "__main__":
    main()
