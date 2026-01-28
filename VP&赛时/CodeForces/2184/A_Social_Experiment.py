import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    outs = []
    for _ in range(int(input())):
        n = int(input())

        if n <= 3:
            outs.append(n)
        else:
            outs.append(n % 2)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()