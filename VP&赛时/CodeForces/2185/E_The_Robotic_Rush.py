import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

inf = 10 ** 10

def main():
    outs = []
    for _ in range(int(input())):
        n, m, k = map(int, input().split())

        a = list(map(int, input().split()))
        b = sorted(map(int, input().split()))
        op = list(input())

        first = defaultdict(int)
        step = 0
        for i in range(k):
            step += 1 if op[i] == 'R' else -1   # 这里可能产生负步数
            if step not in first:
                first[step] = i

        steps = [0] * k
        for i, pos in enumerate(a):
            idx = bisect_right(b, pos)
            times = k
            if idx < m:
                r = b[idx] - pos
                if r in first:
                    times = min(times, first[r])
            if idx > 0:
                l = pos - b[idx-1]
                if -l in first:   # 将正的步数转化为负的
                    times = min(times, first[-l])
    
            if times < k:
                steps[times] += 1
        cur = n
        ans = []
        for i in range(k):
            cur -= steps[i]
            ans.append(cur)
        outs.append(ans)

    for o in outs:
        print(*o)

if __name__ == "__main__":
    main()