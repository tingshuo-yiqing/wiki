import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    a, b, t = map(int, input().split())

    t *= 1000
    mx = 0
    mi = float('inf')

    # if t % (b - a) != 0:
    #     print("UNSATISFIABLE")
    #     sys.exit()
    
    print((t + a - 1) // a)
    print((t + b + 1) // b)

if __name__ == "__main__":
    main()