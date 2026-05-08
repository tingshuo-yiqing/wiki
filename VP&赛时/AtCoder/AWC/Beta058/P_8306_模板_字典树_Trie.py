import sys

def solve():
    # 算法竞赛必用的 Fast I/O：一次性读取全部输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        T = int(next(iterator))
    except StopIteration:
        return

    out =[]
    
    for _ in range(T):
        n = int(next(iterator))
        q = int(next(iterator))
        
        # === 核心模板应用 ===
        trie = [{}]
        cnts = [0]
        
        # 1. 构建字典树，插入所有模式串
        for _ in range(n):
            s = next(iterator)
            cur = 0
            for c in s:
                # 【微优化】：在 Python 中，使用 get 避免了 "not in" + "[]" 的两次哈希计算，速度提升明显
                nxt = trie[cur].get(c) 
                if nxt is None:
                    nxt = len(trie)
                    trie[cur][c] = nxt
                    trie.append({})
                    cnts.append(0)
                cur = nxt
                cnts[cur] += 1  # 经过该节点的前缀数量 + 1
                
        # 2. 查询前缀数量
        for _ in range(q):
            t = next(iterator)
            cur = 0
            for c in t:
                # 同样使用 get，如果找不到字符，返回 -1
                cur = trie[cur].get(c, -1)
                if cur == -1:
                    break
            
            # 如果顺利跑完了整个查询串，cnts[cur] 就是有这个前缀的模式串数量
            if cur != -1:
                out.append(str(cnts[cur]))
            else:
                out.append("0")
                
    # 一次性输出所有结果
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()