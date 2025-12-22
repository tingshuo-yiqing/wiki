months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(n):
    return n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)

def lead_zero(n, width):
    return str(n).zfill(width)  # 补前导0


for y in range(2000, 2025):
    months[2] = 28 + is_leap(y)  # 特判2月

    for m in range(1, 13):
        for d in range(1, months[m] + 1):
            
            date = f"{lead_zero(y, 4)}-{lead_zero(m, 2)}-{lead_zero(d, 2)}"
            print(date)