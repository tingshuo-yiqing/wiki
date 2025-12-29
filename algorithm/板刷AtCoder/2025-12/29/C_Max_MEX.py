import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int,input().split())

    nums = list(map(int, input().split()))

    cnt = set(nums)
    # print(cnt)
    for i in range(k):
        if i not in cnt:
            print(i)
            sys.exit(0)
    print(k)
if __name__ == "__main__":
    main()