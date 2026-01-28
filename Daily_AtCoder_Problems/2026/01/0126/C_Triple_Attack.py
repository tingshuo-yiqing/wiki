import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n = int(input())

    a = list(map(int, input().split()))

    time = 0
    for x in a:
        p = x // 5
        x -= p * 5
        time += p * 3
        while x > 0:
            time += 1
            x -= (3 if time % 3 == 0 else 1)
    
    print(time)

if __name__ == "__main__":
    main()