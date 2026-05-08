# ABC337F - Usual Color Ball Problems
# 题意：n 个球排成一列，m 个盒子，每个盒子容量为 k（同色）。对每个循环移位 x
#       (0 ≤ x < n)，贪心地处理每个球：优先放同色未满盒子，其次放空盒子，否则丢弃。
#       输出每次移位后最终在盒子里的球的总数。
# 思路：将原数组复制一份（长度 2n），用滑动窗口模拟。维护每个颜色在盒子中的球数。
#       当窗口滑动时，先移除左端点球的贡献（若它在盒子中），再尝试将新进入的右端点
#       球放入。用队列追踪被丢弃的球，以便有空间时重新填充。

import sys
from collections import deque

def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    c = list(map(int, sys.stdin.readline().split()))
    # 复制数组，方便处理循环
    balls = c + c

    # box[c] = 该颜色在盒子中的球数（等价于已分配 box 数 * k + 部分填充）
    box = {}
    # discarded[c] = 该颜色被丢弃的球的位置队列
    discarded = {}
    # 当前窗口内盒子中的球总数
    total_in_boxes = 0
    # 当前使用的盒子数
    boxes_used = 0

    ans = []

    # 处理初始窗口 [0, n-1]
    l = 0
    for r in range(n):
        color = balls[r]
        if color not in box:
            box[color] = 0
            discarded[color] = deque()
        
        if box[color] > 0 and box[color] % k != 0:
            # 同色盒子还有空位
            box[color] += 1
            total_in_boxes += 1
        elif boxes_used < m:
            # 分配新盒子
            box[color] += 1
            boxes_used += 1
            total_in_boxes += 1
        else:
            # 丢弃
            discarded[color].append(r)

    ans.append(str(total_in_boxes))

    # 滑动窗口
    for l in range(1, n):
        # 移除左端点
        left_color = balls[l]
        # 检查左端点是否在盒子中
        if left_color in box and box[left_color] > 0:
            # 需要判断左端点是否确实被放进盒子（而非被丢弃）
            # 如果左端点位置在 discarded 队列前面，则它被丢弃了
            if not discarded[left_color] or discarded[left_color][0] != l - 1:
                # 左端点在盒子中，移除
                box[left_color] -= 1
                total_in_boxes -= 1
                if box[left_color] % k == 0 and box[left_color] > 0:
                    # 一个盒子变空了
                    boxes_used -= 1 if box[left_color] // k < (box[left_color] + 1) // k else 0
            else:
                # 左端点被丢弃了，从丢弃队列移除
                discarded[left_color].popleft()

        # 添加右端点
        r = l + n - 1
        right_color = balls[r]
        if right_color not in box:
            box[right_color] = 0
            discarded[right_color] = deque()

        if box[right_color] > 0 and box[right_color] % k != 0:
            # 同色盒子有空位
            box[right_color] += 1
            total_in_boxes += 1
        elif boxes_used < m:
            box[right_color] += 1
            boxes_used += 1
            total_in_boxes += 1
        else:
            discarded[right_color].append(r)

        ans.append(str(total_in_boxes))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()