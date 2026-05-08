# ABC337A - Scoreboard
# 题意：高桥队和青木队进行了N场比赛，每场比赛两队各自得分。
#       总分高的队伍获胜，总分相同则为平局。
# 思路：分别累加两队的总分，最后比较大小即可。

N = int(input())
sum_t = 0  # 高桥队总分
sum_a = 0  # 青木队总分

for _ in range(N):
    X, Y = map(int, input().split())
    sum_t += X
    sum_a += Y

if sum_t > sum_a:
    print("Takahashi")
elif sum_t < sum_a:
    print("Aoki")
else:
    print("Draw")