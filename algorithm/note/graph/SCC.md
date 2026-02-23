



```python
dfn = [-1] * (n + 1)
low = [-1] * (n + 1)
st = []
inst = [False] * (n + 1)
scc_id = [-1] * (n + 1)
scc = 1
timer = 1

def tarjan(x):
    nonlocal timer, scc
    dfn[x] = low[x] = timer
    timer += 1
    st.append(x)
    inst[x] = True

    for y in g[x]:
        if dfn[y] == -1:
            tarjan(y)
            low[x] = Min(low[x], low[y])
        elif inst[y]:
            low[x] = Min(low[x], dfn[y])

    if dfn[x] == low[x]:
        while True:
            cur = st.pop()
            inst[cur] = False
            scc_id[cur] = scc
            if cur == x:
                break
        scc += 1
# 测试链接: https://cses.fi/problemset/task/1683，
```

