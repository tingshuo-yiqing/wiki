import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    nums = sorted(list(map(int, input().split())), reverse=True)

    total = 0
    for i in range(1, 2 * n + 1, 2):
        total += nums[i]

    print(total)

if __name__ == "__main__":
    main()