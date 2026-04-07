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
    s = inp()
    n = len(s)

    def get_value(t):
        return sum(int(x) for x in t.split('.') if x != '')

    i = 0
    mx = 0
    while i < n:
        if s[i] == '(':
            j = i
            while j < n:
                j += 1
                if s[j] == '(':
                    break
                elif s[j] == ')':
                    mx = Max(mx, get_value(s[i+1:j]))
                    break
            i = j + 1
        else:
            i += 1

    print(mx)

if __name__ == "__main__":
    main()
