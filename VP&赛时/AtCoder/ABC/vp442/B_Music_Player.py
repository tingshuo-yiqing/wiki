import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    q = int(input())

    cur = 0
    play = False
    for _ in range(q):
        op = int(input())
        if op == 1:
            cur += 1
        elif op == 2:
            if cur > 0:
                cur -= 1
        else:
            if play:
                play = False
            else:
                play = True
        print("Yes" if cur >= 3 and play else "No")

if __name__ == "__main__":
    main()