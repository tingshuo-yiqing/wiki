import sys
from collections import Counter
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    outs = []

    for _ in range(int(input())):
        n = int(input())

        arr = list(map(int, input().split()))

        if arr[0] == 1 or arr[n - 1] == 1:
            outs.append("Alice")
        else:
            outs.append("Bob")

    print(*outs, sep='\n')
if __name__ == "__main__":
    main()