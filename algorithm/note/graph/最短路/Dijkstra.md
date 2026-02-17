## 应用

### 输出路径

```python
pre = [-1] * (n + 1)

hq = [(0, 1)]
while hq:
    d, u = heappop(hq)
    if d > dist[u]:
        continue
    for v, w in g[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            pre[v] = u  # 
            heappush(hq, (dist[v], v))

if dist[n] == inf:
    print(-1)
else:
    cur = n
    path = []
    while cur != -1:  # 起点是-1
        path.append(cur)
        cur = pre[cur]
    print(*path[::-1])

```

