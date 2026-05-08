"""
题意: n个球排成一列(可循环移位)，m个盒子(每个最多装k个同色球)。对每个循环移位x，
按顺序处理每个球：优先放入同色且不满的盒，否则放空盒，否则吃掉。求盒中球总数。
思路: 窗口内按颜色首次出现顺序分配盒子。每种颜色c需要ceil(cnt[c]/k)个盒子。
二分前缀和确定能完整分配的颜色，剩余盒子给下一个颜色部分分配。
用BIT按first_pos维护盒子数和球数，滑动窗口O(N log N)。
"""
import sys

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)
    def add(self, idx, val):
        i = idx + 1
        n = self.n
        while i <= n:
            self.bit[i] += val
            i += i & -i
    def sum(self, idx):
        if idx < 0: return 0
        i = min(idx + 1, self.n)
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    def total(self):
        return self.sum(self.n - 1)
    def upper_bound(self, limit):
        """largest idx such that sum(idx) <= limit. If none, return -1"""
        if limit < 0 or self.sum(0) > limit:
            return -1
        lo, hi = 0, self.n - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.sum(mid) <= limit:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
    def next_nonzero(self, lo):
        """smallest idx >= lo such that value at idx != 0. If none, return -1"""
        cur = self.sum(lo - 1) if lo > 0 else 0
        if cur >= self.total():
            return -1
        # find first idx where sum(idx) > cur
        target = cur
        lo2, hi2 = lo, self.n - 1
        while lo2 < hi2:
            mid = (lo2 + hi2) // 2
            if self.sum(mid) > target:
                hi2 = mid
            else:
                lo2 = mid + 1
        if lo2 < self.n and self.sum(lo2) > target:
            return lo2
        return -1

def solve() -> None:
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    c = list(map(int, input().split()))

    # 离散化
    uniq = sorted(set(c))
    comp = {x: i for i, x in enumerate(uniq)}
    arr = [comp[x] for x in c]
    C = len(uniq)

    # 倍长
    darr = arr * 2
    N = 2 * n

    # next_pos[i] = 下一个同色位置, -1表示无
    next_pos = [-1] * N
    last = [-1] * C
    for i in range(N - 1, -1, -1):
        col = darr[i]
        if last[col] != -1:
            next_pos[i] = last[col]
        last[col] = i

    # 窗口状态
    cnt = [0] * C
    first_pos = [-1] * C

    # BIT
    bit_box = BIT(N)   # 在first_pos存 ceil(cnt/k)
    bit_ball = BIT(N)  # 在first_pos存 cnt

    box_at = [0] * N
    ball_at = [0] * N

    def add(pos, boxes, balls):
        bit_box.add(pos, boxes)
        bit_ball.add(pos, balls)
        box_at[pos] = boxes
        ball_at[pos] = balls

    def rem(pos, boxes, balls):
        bit_box.add(pos, -boxes)
        bit_ball.add(pos, -balls)
        box_at[pos] = 0
        ball_at[pos] = 0

    def set_color(col, new_cnt, new_first):
        old_pos = first_pos[col]
        old_cnt = cnt[col]
        if old_pos != -1 and old_cnt > 0:
            old_boxes = (old_cnt + k - 1) // k
            rem(old_pos, old_boxes, old_cnt)
        cnt[col] = new_cnt
        first_pos[col] = new_first
        if new_first != -1 and new_cnt > 0:
            new_boxes = (new_cnt + k - 1) // k
            add(new_first, new_boxes, new_cnt)

    # 初始化第一个窗口
    for i in range(n):
        col = darr[i]
        if first_pos[col] == -1:
            first_pos[col] = i
        cnt[col] += 1
    for col in range(C):
        if first_pos[col] != -1:
            boxes = (cnt[col] + k - 1) // k
            add(first_pos[col], boxes, cnt[col])

    def calc_ans():
        if bit_box.total() == 0:
            return 0
        p = bit_box.upper_bound(m)  # sum_box(0..p) <= m
        if p == -1:
            return 0
        used_boxes = bit_box.sum(p)
        ans = bit_ball.sum(p)
        if used_boxes < m:
            q = bit_box.next_nonzero(p + 1)
            if q != -1:
                rem_boxes = m - used_boxes
                ans += min(ball_at[q], rem_boxes * k)
        return ans

    ans = [0] * n
    ans[0] = calc_ans()

    # 滑动窗口
    for l in range(1, n):
        out_pos = l - 1
        in_pos = l + n - 1
        out_col = darr[out_pos]
        in_col = darr[in_pos]

        if out_col == in_col:
            # cnt不变, 但first_pos可能右移
            if first_pos[out_col] == out_pos:
                new_first = next_pos[out_pos]  # 一定有next且≤in_pos
                set_color(out_col, cnt[out_col], new_first)
        else:
            # 移出 out_col
            new_cnt_out = cnt[out_col] - 1
            if new_cnt_out == 0:
                set_color(out_col, 0, -1)
            else:
                if first_pos[out_col] == out_pos:
                    new_first = next_pos[out_pos]  # 一定有next且≤in_pos
                    set_color(out_col, new_cnt_out, new_first)
                else:
                    set_color(out_col, new_cnt_out, first_pos[out_col])

            # 加入 in_col
            new_cnt_in = cnt[in_col] + 1
            if cnt[in_col] == 0:
                set_color(in_col, new_cnt_in, in_pos)
            else:
                set_color(in_col, new_cnt_in, first_pos[in_col])

        ans[l] = calc_ans()

    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    solve()