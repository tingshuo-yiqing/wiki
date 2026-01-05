import sys
from collections import Counter, defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    cnt = Counter()
    char = ['M', 'A', 'R', 'C', 'H']

    for _ in range(n):
        s = input()
        if s[0] in "MARCH":
            cnt[s[0]] += 1
    
    ans = 0
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                ans = ans + cnt[char[i]] * cnt[char[j]] * cnt[char[k]]

    print(ans)

if __name__ == "__main__":
    main()