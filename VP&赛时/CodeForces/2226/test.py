for i in range(1, 30):
    s = set()
    for j in range(1, 100000):
        s.add(i % j)
    print(f'{i}:', *s)