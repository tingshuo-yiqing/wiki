import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def prod(x, y, z):
    return x * x + y * y + z * z + x * y + x * z + z * y

def main():
    n = int(input())

    mp = [0] * (n + 1)
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                t = prod(x, y, z)
                if t <= n:
                    mp[t] += 1

    print(*mp[1:], sep='\n')

if __name__ == "__main__":
    main()