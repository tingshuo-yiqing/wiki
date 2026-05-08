# ABC337B - Extended ABC
# 题意：判断一个仅由A、B、C组成的字符串是否满足：由0个或多个A、0个或多个B、
#       0个或多个C按顺序拼接而成（即形如 A...AB...BC...C）。
# 思路：合法的字符串中，字符顺序只能是非递减的（A→B→C），不会出现B在A前面、
#       C在A前面、C在B前面的情况。直接检查相邻字符是否违反这个顺序即可。

S = input().strip()

for i in range(len(S) - 1):
    if S[i] > S[i + 1]:  # 出现B→A、C→A、C→B都是非法的
        print("No")
        break
else:
    print("Yes")