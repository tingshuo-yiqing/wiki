import sys

input = lambda: sys.stdin.readline().strip()

def main():
    k = int(input())

    r = 0
    for i in range(2 * k):    
        r = (r * 10 + 7) % k  # 每次维护余数，不然大数运算会超时
        # if r == 0:
        #     print(i + 1)
        #     sys.exit(0)
        print(r)
    print(-1)

if __name__ == "__main__":
    main()