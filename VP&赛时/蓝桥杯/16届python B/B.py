import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    words = []
    with open('words.txt', 'r') as file:
        for w in file.readlines():
            words.append(''.join(sorted(list(w[:-1]))))
    
    n = len(words)

    words.sort()

    for o in words[700:900]:
        print(o)

if __name__ == "__main__":
    main()
