import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    a, b, t = map(int, input().split())

    t *= 1000
    mx = 0
    mi = float('inf')

    for i in range(1, 1000001):   # 枚举答案
        if a * i <= t and b * i >= t:
            mi = min(mi, i)
            mx = max(mx, i)
    if mx == 0:
        print("UNSATISFIABLE")
    else:
        print(mi, mx)

if __name__ == "__main__":
    main()