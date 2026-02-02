import sys
from math import atan2

if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

    dot = lambda x, y: x[0] * y[0] + x[1] * y[1] 
    cross = lambda x, y: x[0] * y[1] - x[1] * y[0] 

def main():
    n = II()

    a = [(MII()) for _ in range(n)]

    vector = []
    for i, (u, v) in enumerate(a):
        vector.append(((u, v), i + 1))
    
    vector.sort(key=lambda x: atan2(x[0][1], x[0][0]))

    P = None
    vl = vr = -1
    for i in range(n):
        u, v = vector[i][0], vector[(i + 1) % n][0]

        cur_dot = dot(u, v)
        cur_cross = abs(cross(u, v))

        if P is None:
            P = (cur_dot, cur_cross)
            vl, vr = vector[i][1], vector[(i + 1) % n][1]
            continue
        
        cur_p = (cur_dot, cur_cross)
        if cross(cur_p, P) > 0:
            P = cur_p
            vl, vr = vector[i][1], vector[(i + 1) % n][1]
    
    print(vl, vr)

if __name__ == "__main__":
    main()