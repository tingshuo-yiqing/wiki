import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    cntA = [0] * 46
    cntB = [0] * 46
    cntC = [0] * 46

    for x in A:
        cntA[x % 46] += 1
    for x in B:
        cntB[x % 46] += 1
    for x in C:
        cntC[x % 46] += 1

    ans = 0
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i + j + k) % 46 == 0:
                    ans += (cntA[i] * cntB[j] * cntC[k])

    print(ans)

if __name__ == "__main__":
    main()