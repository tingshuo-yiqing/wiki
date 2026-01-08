import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    outs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            outs.append(i)
            if n // i != i:
                outs.append(n // i)
    
    print(*sorted(outs), sep='\n')

if __name__ == "__main__":
    main()